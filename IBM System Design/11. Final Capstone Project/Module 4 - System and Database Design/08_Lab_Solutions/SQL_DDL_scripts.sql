-- ============================================================================
-- Retail Bank Digital Core - Production Database DDL Script
-- Database Engine: PostgreSQL 14+ / Enterprise Compatible
-- Author: Systems and Solutions Architect
-- Standards: PCI-DSS, SOC 2, ACID Compliant
-- File: SQL_DDL_scripts.sql
-- ============================================================================

-- 0. Dọn dẹp môi trường thử nghiệm (Clean up)
DROP TABLE IF EXISTS compliance_logs CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS cards CASCADE;
DROP TABLE IF EXISTS loans CASCADE;
DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS branches CASCADE;

-- ----------------------------------------------------------------------------
-- 1. BẢNG BRANCHES (Mạng lưới chi nhánh)
-- ----------------------------------------------------------------------------
CREATE TABLE branches (
    branch_id SERIAL PRIMARY KEY,
    branch_code VARCHAR(20) NOT NULL UNIQUE,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ----------------------------------------------------------------------------
-- 2. BẢNG CUSTOMERS (Hồ sơ khách hàng định danh eKYC)
-- ----------------------------------------------------------------------------
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    branch_id INT NOT NULL,
    national_id VARCHAR(30) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    kyc_status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    risk_level VARCHAR(10) NOT NULL DEFAULT 'LOW',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_customer_branch FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE RESTRICT,
    CONSTRAINT chk_kyc_status CHECK (kyc_status IN ('Pending', 'Verified', 'Rejected')),
    CONSTRAINT chk_risk_level CHECK (risk_level IN ('LOW', 'MEDIUM', 'HIGH')),
    CONSTRAINT chk_customer_dob CHECK (dob <= CURRENT_DATE - INTERVAL '18 years') -- Phải từ 18 tuổi trở lên
);

-- ----------------------------------------------------------------------------
-- 3. BẢNG ACCOUNTS (Tài khoản thanh toán / Tiết kiệm)
-- ----------------------------------------------------------------------------
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    account_number VARCHAR(34) NOT NULL UNIQUE, -- Chuẩn IBAN / Số TK ngân hàng
    customer_id INT NOT NULL,
    branch_id INT NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    balance NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    opened_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    CONSTRAINT fk_account_branch FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE RESTRICT,
    CONSTRAINT chk_account_type CHECK (account_type IN ('CHECKING', 'SAVINGS', 'PAYROLL')),
    CONSTRAINT chk_account_status CHECK (status IN ('ACTIVE', 'FROZEN', 'DORMANT', 'CLOSED')),
    CONSTRAINT chk_account_balance CHECK (balance >= 0.00) -- Chặn âm tài khoản nếu không có thấu chi
);

-- ----------------------------------------------------------------------------
-- 4. BẢNG CARDS (Thẻ phát hành liên kết tài khoản)
-- ----------------------------------------------------------------------------
CREATE TABLE cards (
    card_id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    card_number_masked VARCHAR(19) NOT NULL, -- Không bao giờ lưu số PAN thô (Tuân thủ PCI-DSS)
    card_type VARCHAR(20) NOT NULL,
    expiry_date DATE NOT NULL,
    card_status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    issued_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_card_account FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE,
    CONSTRAINT chk_card_type CHECK (card_type IN ('DEBIT', 'CREDIT', 'VIRTUAL')),
    CONSTRAINT chk_card_status CHECK (card_status IN ('ACTIVE', 'BLOCKED', 'EXPIRED'))
);

-- ----------------------------------------------------------------------------
-- 5. BẢNG LOANS (Quản mục hợp đồng tín dụng và khoản vay)
-- ----------------------------------------------------------------------------
CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    loan_type VARCHAR(30) NOT NULL,
    principal_amount NUMERIC(15, 2) NOT NULL,
    interest_rate NUMERIC(5, 2) NOT NULL, -- Lãi suất %/năm (vd: 8.50%)
    term_months INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    loan_status VARCHAR(20) NOT NULL DEFAULT 'APPROVED',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_loan_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    CONSTRAINT chk_loan_principal CHECK (principal_amount > 0),
    CONSTRAINT chk_loan_interest CHECK (interest_rate >= 0),
    CONSTRAINT chk_loan_term CHECK (term_months >= 1),
    CONSTRAINT chk_loan_status CHECK (loan_status IN ('PENDING', 'APPROVED', 'ACTIVE', 'PAID_OFF', 'DEFAULTED'))
);

-- ----------------------------------------------------------------------------
-- 6. BẢNG TRANSACTIONS (Sổ cái giao dịch tài chính - OLTP)
-- ----------------------------------------------------------------------------
CREATE TABLE transactions (
    transaction_id VARCHAR(64) PRIMARY KEY, -- Sử dụng UUID hoặc mã tham chiếu tài chính toàn cầu
    account_id INT NOT NULL,
    destination_account VARCHAR(34) NOT NULL,
    transaction_type VARCHAR(30) NOT NULL,
    amount NUMERIC(15, 2) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT fk_transaction_account FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE RESTRICT,
    CONSTRAINT chk_transaction_type CHECK (transaction_type IN ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER', 'LOAN_DISBURSEMENT', 'LOAN_REPAYMENT')),
    CONSTRAINT chk_transaction_amount CHECK (amount > 0),
    CONSTRAINT chk_transaction_status CHECK (status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'FAILED', 'REVERSED'))
);

-- ----------------------------------------------------------------------------
-- 7. BẢNG COMPLIANCE_LOGS (Nhật ký kiểm toán, giám sát AML và gian lận)
-- ----------------------------------------------------------------------------
CREATE TABLE compliance_logs (
    log_id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(64),
    customer_id INT,
    event_type VARCHAR(50) NOT NULL,
    risk_score INT NOT NULL,
    action_taken VARCHAR(50) NOT NULL,
    details TEXT,
    logged_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_log_transaction FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id) ON DELETE SET NULL,
    CONSTRAINT fk_log_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL,
    CONSTRAINT chk_risk_score CHECK (risk_score BETWEEN 0 AND 100),
    CONSTRAINT chk_log_event CHECK (event_type IN ('AML_SUSPICIOUS_TXN', 'LARGE_CASH_TRANSACTION', 'FAILED_MFA_ATTEMPT', 'UNAUTHORIZED_ACCESS_ATTEMPT'))
);

-- ----------------------------------------------------------------------------
-- CHỈ MỤC TỐI ƯU TRUY VẤN (INDEXES FOR HIGH-THROUGHPUT PERFORMANCE)
-- ----------------------------------------------------------------------------
-- Tối ưu tìm kiếm khách hàng
CREATE INDEX idx_customers_national_id ON customers(national_id);
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_kyc_status ON customers(kyc_status);

-- Tối ưu tra cứu tài khoản và số dư
CREATE INDEX idx_accounts_customer_id ON accounts(customer_id);
CREATE INDEX idx_accounts_account_number ON accounts(account_number);

-- Tối ưu sổ cái giao dịch theo thời gian và tài khoản (Query Statement History)
CREATE INDEX idx_transactions_account_date ON transactions(account_id, created_at DESC);
CREATE INDEX idx_transactions_status ON transactions(status);

-- Tối ưu kiểm toán và tra soát AML
CREATE INDEX idx_compliance_transaction ON compliance_logs(transaction_id);
CREATE INDEX idx_compliance_risk_logged ON compliance_logs(risk_score DESC, logged_at DESC);
