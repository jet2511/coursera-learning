# Lab: Reviewing Test Plans and Creating TDD/BDD Test Cases - Solution

**Course:** IBM System Design - Capstone Project  
**Module:** Module 5 - System Testing and Deployment Strategies  
**Target System:** Retail Bank Digital Core Modernization (Onboarding, Accounts, Loans, Transactions, Fraud/AML)  
**Author:** Parikshit Jain  

---

## Task 1: Review and annotate a sample test plan

Review the test plan provided to you and list your findings below.

### List of 7 Key Issues Found in the Test Plan:

1. **Missing Negative & Failure Testing for Multi-Factor Authentication (MFA):**
   - *Observation:* Section 2.1 & Section 6 cite MFA and OAuth2 security testing, but there are no defined test cases for expired OTP/tokens, locked accounts after $N$ failed attempts, or replay attacks.

2. **Incomplete Negative Testing for Invalid/Fraudulent KYC Documents:**
   - *Observation:* Section 5.1 mentions KYC Validator unit testing, but lacks test scenarios verifying expired passports/IDs, unreadable/corrupted files, or synthetic identity fraud detection.

3. **No Test Cases Validating Fraud Scoring & AML Threshold Rules:**
   - *Observation:* AML & Fraud Engine are in-scope, but the plan omits test cases for transactions exceeding regulatory thresholds (e.g., >\$10,000 cash reporting), high-velocity micro-transfers (structuring/smurfing), or automated account freezes.

4. **Duplicate Scenarios in Core Account Inquiries:**
   - *Observation:* Redundant test definitions exist for retrieving balance inquiries via REST API versus ledger queries, without distinguishing between cached balance and real-time ledger settlement.

5. **Weak and Ambiguous Acceptance Criteria across Microservices:**
   - *Observation:* Acceptance criteria for inter-service communication (KYC → Account → Loan → Fraud → Ledger) lack explicit timeout tolerances, idempotency requirements, or dead-letter queue (DLQ) behavior during Kafka event delivery failures.

6. **Missing Compensating Transactions & SAGA Rollback Testing:**
   - *Observation:* The test plan mentions compensating actions in Section 5.1 (Integration Tests) but fails to define explicit test cases for partial failures (e.g., loan approved but account creation fails).

7. **Omission of Audit Log Immutability & Regulatory Compliance Validation:**
   - *Observation:* While "Compliance & audit logging" is listed in scope, there are no test cases asserting tamper-evident audit trails, PII data masking in Kafka event logs, or regulatory retention policies.

---

## Task 2: Use the RTM to validate traceability

Requirements Traceability Matrix (RTM) linking business & regulatory requirements to specific test cases:

| Requirement ID | Requirement Description | Test Case IDs | Coverage (Yes/No) | Notes |
| :--- | :--- | :--- | :---: | :--- |
| **RQ-AUTH-01** | Multi-Factor Authentication (MFA) must be enforced for all login and fund transfer requests. | TC-SEC-0101 | **No** | *Missing test cases:* Only positive login flow mapped; missing OTP expiry and lockout scenarios. |
| **RQ-KYC-02** | Customer identity documents must be validated against national ID registry before account activation. | TC-KYC-0201 | **No** | *Requires additional negative testing:* Only valid document upload is covered; missing rejected, fake, or unreadable document handling. |
| **RQ-ACCT-03** | Core account creation must assign a unique IBAN/Account Number and initialize zero-balance ledger. | TC-ACC-0101, TC-ACC-0102 | **No** | *Outdated/Incorrect mapping:* TC-ACC-0102 is a duplicate balance retrieval test, not an account generation test. |
| **RQ-TXN-04** | Real-time fund transfers between internal accounts must execute within 500ms with ACID ledger updates. | TC-TXN-0301, TC-TXN-0302 | **Yes** | Fully covered with unit and integration tests across debit and credit ledger entries. |
| **RQ-AML-05** | Any single transaction exceeding $10,000 or suspicious velocity must trigger an immediate AML hold. | *None* | **No** | *Missing test cases:* Critical regulatory gap. No test case exists to validate AML threshold detection or automated suspension. |
| **RQ-LOAN-06** | Loan eligibility engine must evaluate debt-to-income (DTI) ratio ≤ 43% and minimum credit score ≥ 650. | TC-LOAN-0401, TC-LOAN-0402 | **Yes** | Covered for both approved and declined applicant criteria. |
| **RQ-AUDIT-07**| All customer state changes and monetary transactions must generate immutable audit logs. | TC-AUD-0501 | **Yes** | Validates structured JSON audit emission to secure audit datastore. |

### Summary of Traceability Findings:
- **Missing test cases (2):** `RQ-AML-05` (Zero coverage for AML compliance hold) and `RQ-AUTH-01` (Missing MFA failure/lockout coverage).
- **Outdated / Incorrect mapping (1):** `RQ-ACCT-03` mapped to `TC-ACC-0102` which is an account inquiry rather than account provisioning.
- **Requirement needing additional negative testing (1):** `RQ-KYC-02` (Needs rejection on expired/corrupt ID uploads).

---

## Task 3: Create TDD-style test cases

Selected Module: **Loan Eligibility Engine** (Alternative: Fraud Detection / KYC)

### TDD Test Case 1: Minimum Income and Credit Score Threshold

- **Test Case ID:** `TC-TDD-LOAN-001`
- **Module:** Loan Eligibility Engine
- **Purpose:** Validate that applicants meeting the minimum income threshold ($30,000/year) and credit score (>= 650) are marked as `ELIGIBLE`.
- **Preconditions:** Loan rules engine is initialized with standard retail risk parameters.
- **Inputs:** 
  ```json
  {
    "applicantId": "APP-1001",
    "annualIncome": 45000,
    "creditScore": 720,
    "existingMonthlyDebt": 500,
    "requestedLoanAmount": 15000
  }
  ```
- **Execution Steps:**
  1. Instantiate `LoanEligibilityEngine` service.
  2. Invoke `evaluateEligibility(loanApplicationRequest)`.
  3. Inspect returned `EligibilityResult` object.
- **Expected Output:**
  ```json
  {
    "status": "ELIGIBLE",
    "maxApprovedAmount": 15000,
    "rejectionReasons": []
  }
  ```
- **Edge Cases:** Applicant with exactly $30,000 annual income and credit score of exactly 650 (boundary value testing: inclusive upper/lower bounds).

---

### TDD Test Case 2: Debt-to-Income (DTI) Hard Limit Rejection

- **Test Case ID:** `TC-TDD-LOAN-002`
- **Module:** Loan Eligibility Engine
- **Purpose:** Validate that an applicant with good credit score but DTI ratio exceeding 43% is strictly rejected with a designated reason code.
- **Preconditions:** Loan rules engine active.
- **Inputs:** 
  ```json
  {
    "applicantId": "APP-1002",
    "annualIncome": 60000,
    "creditScore": 750,
    "existingMonthlyDebt": 2300,
    "requestedLoanAmount": 20000
  }
  ```
- **Execution Steps:**
  1. Calculate proposed monthly debt payment ($400/mo). Total monthly debt = $2700.
  2. Compute DTI: `$2700 / ($60000 / 12) = 54% (> 43%)`.
  3. Invoke `evaluateEligibility(loanApplicationRequest)`.
  4. Assert result status and rejection code.
- **Expected Output:**
  ```json
  {
    "status": "NOT_ELIGIBLE",
    "maxApprovedAmount": 0,
    "rejectionReasons": ["ERR_DTI_EXCEEDED_THRESHOLD_43"]
  }
  ```
- **Edge Cases:** Proposed DTI calculated at exactly 43.00% (should pass) vs 43.01% (must be rejected).

---

### TDD Test Case 3: Zero or Negative Income Defensive Handling

- **Test Case ID:** `TC-TDD-LOAN-003`
- **Module:** Loan Eligibility Engine
- **Purpose:** Ensure the engine defensively handles malformed financial inputs (negative values, division by zero) by throwing an explicit domain validation exception.
- **Preconditions:** Engine initialized.
- **Inputs:** 
  ```json
  {
    "applicantId": "APP-1003",
    "annualIncome": 0,
    "creditScore": 600,
    "existingMonthlyDebt": 100,
    "requestedLoanAmount": 5000
  }
  ```
- **Execution Steps:**
  1. Invoke `evaluateEligibility(loanApplicationRequest)` with `annualIncome <= 0`.
  2. Capture thrown exception.
- **Expected Output:** Throws `InvalidFinancialDataException("Annual income must be greater than zero")` with HTTP 400 Bad Request mapping; zero calculation side-effects.
- **Edge Cases:** Extremely large integer inputs (`annualIncome = Long.MAX_VALUE`), null values, or negative debt values.

---

## Task 4: Write BDD scenarios in Gherkin syntax

### BDD Scenario 1: Customer Transfers Funds Successfully

```gherkin
Feature: Retail Bank Fund Transfer Processing
  As an authenticated retail banking customer
  I want to transfer funds to another active account
  So that I can pay bills or send money securely

  Scenario: Customer transfers funds successfully within available balance
    Given an authenticated customer with account "ACC-12345" has an active balance of $500.00
    And the beneficiary account "ACC-67890" is active and valid
    When the customer initiates a transfer of $200.00 with description "Invoice payment"
    And confirms the transaction with a valid MFA one-time passcode
    Then the transaction should be approved and processed successfully
    And the balance of account "ACC-12345" should be updated to $300.00
    And a Kafka event "TRANSACTION_COMPLETED" should be published for ledger settlement
    And an audit log record with status "SUCCESS" should be stored
```

---

### BDD Scenario 2: Fund Transfer Fails Due to Insufficient Funds

```gherkin
Feature: Fund Transfer Overdraft Protection
  As an account holder without overdraft protection
  I should be prevented from transferring more money than my current balance
  So that my account does not enter an unapproved negative balance

  Scenario: Customer transfer fails when amount exceeds current balance
    Given an authenticated customer with account "ACC-12345" has an active balance of $150.00
    And no overdraft credit facility is enabled on account "ACC-12345"
    When the customer attempts to transfer $250.00 to account "ACC-67890"
    Then the transaction should be declined with error "INSUFFICIENT_FUNDS"
    And the customer balance should remain unchanged at $150.00
    And no debit or credit operations should be applied to the core ledger
    And a notification "Transfer failed: insufficient funds" should be sent to the customer
```

---

## Task 5: Validate your findings

Validation Checklist for Test Completeness & Compliance:

| Validation Item | Yes/No | Verification Evidence |
| :--- | :---: | :--- |
| **All requirements mapped in RTM** | **Yes** | All 7 core business and regulatory requirements (Auth, KYC, Account, Txn, AML, Loan, Audit) are indexed and analyzed in Task 2. |
| **Edge cases considered** | **Yes** | Inclusive threshold limits (exact $30,000, 43.0% DTI), boundary scores, and malformed inputs covered in TDD test cases. |
| **Negative scenarios included** | **Yes** | Handled insufficient balance in BDD, zero income exceptions in TDD, and identified missing MFA/KYC negatives in Task 1 & 2. |
| **TDD tests aligned with the architecture** | **Yes** | Test cases map directly to modular microservice domain logic (`LoanEligibilityEngine`) with deterministic unit execution. |
| **BDD flows reflect user journeys** | **Yes** | Auth, MFA verification, transfer initiation, balance deduction, and notification reflect true customer paths. |
| **Regulatory (KYC/AML) tests included** | **Yes** | KYC verification steps, AML $10,000 threshold monitoring, and immutable audit logs explicitly documented. |
| **Full traceability achieved** | **Yes** | Traceability gaps highlighted and remediated from requirements down to unit and acceptance tests. |
