import docx
from docx.shared import Inches
import os

src_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_APIs_and_Data_Flows\Template.docx"
out_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_APIs_and_Data_Flows\Completed_Template_Documenting_APIs_and_data_flows.docx"
img_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_APIs_and_Data_Flows\API_dataflow for retail bank.png"

doc = docx.Document(src_path)

# Task 1: Table 0 (Inventory of Key APIs)
t0 = doc.tables[0]
task1_data = [
    ("Authentication & IAM API", "User authentication, MFA challenge/verify, OAuth2 token issuance", "Internal / Edge", "Web & Mobile Banking Apps, Internal Microservices", "OAuth2.0 + PKCE; issues short-lived JWT tokens (5m TTL)."),
    ("Transaction Processing API", "Real-time fund transfers, bill payments, and balance debit/credits", "Internal", "Mobile App, Web Portal, ATM Switch, Open Banking API", "Core transactional engine; enforces strict idempotency and ACID commits."),
    ("Customer Onboarding & KYC API", "Collects applicant profile, triggers ID verify, and account creation", "Internal / Edge", "Prospective Banking Customers, Branch Operators", "Encrypts sensitive PII; manages onboarding state machine."),
    ("Fraud Detection & AML API", "Real-time transaction risk scoring, AML threshold evaluation, sanctions", "Internal", "Transaction Service, Loan Servicing Engine", "Latency SLA < 150ms; synchronous scoring before payment authorization."),
    ("Loan Servicing & Eligibility API", "Evaluates credit limits, DTI ratio, and loan repayment schedules", "Internal", "Customer Loan Portal, Credit Operations Team", "Orchestrates internal financial history and external credit scores."),
    ("Notifications API", "Sends transactional alerts, OTP passcodes, and statements via SMS/Email/Push", "Internal", "Auth Service, Transaction Core, Marketing Systems", "Asynchronous Kafka event consumer with guaranteed delivery retries."),
    ("Third-Party Credit Bureau API", "Retrieves external credit scores (FICO / Experian) and credit history", "External", "Loan Servicing Engine, Fraud Service", "Consumed via REST/JSON with API Key, mTLS, and egress IP whitelisting.")
]

for idx, data in enumerate(task1_data):
    if idx + 1 < len(t0.rows):
        row = t0.rows[idx + 1]
    else:
        row = t0.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 2: Fill API 1 and API 2 in paragraphs & tables
for p in doc.paragraphs:
    if p.text.startswith("API Name:"):
        p.text = "API Name: Transaction Processing API"
    elif p.text.startswith("Base URL:"):
        p.text = "Base URL: https://api.retailbank.com/v1/transactions"

# Table 1: Endpoint 1 of API 1
t1 = doc.tables[1]
t1.rows[0].cells[0].text = """Endpoint 1.1: Initiate Internal Fund Transfer
Method: POST
Path: /transfers
Headers:
  Content-Type: application/json
  Authorization: Bearer <JWT_ACCESS_TOKEN>
  X-Idempotency-Key: 7b9a528e-8a21-4f76-bc34-45300fbf5632
  X-Correlation-ID: corr-txn-984210
Authentication Required: OAuth 2.0 / JWT (scope: transfers:write)
Request Body:
{
  "sourceAccountNumber": "ACC-10029384",
  "destinationAccountNumber": "ACC-50019283",
  "amount": 250.00,
  "currency": "USD",
  "paymentReference": "Invoice #4928 payment",
  "transferType": "INTERNAL_TRANSFER"
}
Success Response (201 Created):
{
  "transactionId": "TXN-88492019",
  "status": "COMPLETED",
  "amount": 250.00,
  "currency": "USD",
  "remainingBalance": 1250.75,
  "timestamp": "2026-11-19T14:52:00Z"
}
Error Responses:
  400 Bad Request: ERR_INSUFFICIENT_FUNDS
  401 Unauthorized: ERR_INVALID_TOKEN
  409 Conflict: ERR_DUPLICATE_IDEMPOTENCY_KEY"""

# Table 2: Endpoint 2 of API 1
t2 = doc.tables[2]
t2.rows[0].cells[0].text = """Endpoint 1.2: Get Transaction Details by ID
Method: GET
Path: /transfers/{transactionId}
Headers:
  Authorization: Bearer <JWT_ACCESS_TOKEN>
  Accept: application/json
Authentication Required: OAuth 2.0 / JWT (scope: transfers:read)
Request Parameters: Path param 'transactionId' (e.g. TXN-88492019)
Success Response (200 OK):
{
  "transactionId": "TXN-88492019",
  "status": "COMPLETED",
  "amount": 250.00,
  "currency": "USD",
  "timestamp": "2026-11-19T14:52:00Z",
  "settlementStatus": "SETTLED_ON_LEDGER"
}
Error Responses:
  404 Not Found: ERR_TRANSACTION_NOT_FOUND
  403 Forbidden: ERR_ACCESS_DENIED"""

# Table 3: API 2 (Authentication & IAM API)
t3 = doc.tables[3]
t3.rows[0].cells[0].text = """API Name: Authentication & IAM API
Base URL: https://auth.retailbank.com/v1/oauth2

Endpoint 2.1: User Login & Token Grant
Method: POST
Path: /token
Headers: Content-Type: application/x-www-form-urlencoded
Authentication: OAuth 2.0 PKCE Authorization Code Grant
Request Body: grant_type=authorization_code&code=splat923847&redirect_uri=https://app.retailbank.com/callback&client_id=retail-mobile-app&code_verifier=dBjftJeZ4...
Success Response (200 OK):
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 300,
  "refresh_token": "r_9921849182390123",
  "scope": "openid profile transfers:write"
}
Error Responses: 401 Unauthorized (ERR_INVALID_CREDENTIALS), 400 Bad Request (ERR_INVALID_PKCE)

------------------------------------------------------------------------------------------------------

Endpoint 2.2: Multi-Factor Authentication (MFA) Verification
Method: POST
Path: /mfa/verify
Headers: Content-Type: application/json, X-MFA-Session-Token: mfa_sess_8892193
Request Body: {"otpCode": "849201", "mfaType": "TOTP"}
Success Response (200 OK): {"status": "VERIFIED", "access_token": "eyJhbGciOiJSUzI1NiIsIm1mYSI6dHJ1ZX0...", "expires_in": 300}
Error Responses: 400 Bad Request (ERR_MFA_INVALID_OR_EXPIRED), 429 Too Many Requests"""

# Task 3: Table 4 (Status Codes & Error Handling)
t4 = doc.tables[4]
task3_data = [
    ("200 OK", "Request Succeeded", "Standard read queries, balance checks, successful verification.", "{\"status\": \"SUCCESS\", \"data\": {...}}"),
    ("201 Created", "Resource Created", "Fund transfer executed, new account created.", "{\"transactionId\": \"TXN-88492019\", \"status\": \"COMPLETED\"}"),
    ("400 Bad Request", "Invalid Input Data", "Malformed JSON payload, negative transfer amounts.", "{\"errorCode\": \"ERR_INVALID_PAYLOAD\", \"message\": \"Amount must be > 0.\", \"traceId\": \"tr-492\"}"),
    ("401 Unauthorized", "Authentication Failed", "Missing, invalid, or expired JWT access token.", "{\"errorCode\": \"ERR_UNAUTHORIZED\", \"message\": \"JWT token expired.\", \"traceId\": \"tr-493\"}"),
    ("403 Forbidden", "Authorization Denied", "Caller lacks RBAC role or attempts to access another's account.", "{\"errorCode\": \"ERR_FORBIDDEN\", \"message\": \"Access denied to target account.\", \"traceId\": \"tr-494\"}"),
    ("404 Not Found", "Resource Not Found", "Target transaction ID or account does not exist.", "{\"errorCode\": \"ERR_ACCOUNT_NOT_FOUND\", \"message\": \"Account does not exist.\", \"traceId\": \"tr-495\"}"),
    ("409 Conflict", "Duplicate / Concurrency", "Replay of existing X-Idempotency-Key or concurrency lock.", "{\"errorCode\": \"ERR_DUPLICATE_IDEMPOTENCY\", \"message\": \"Transaction already processed.\", \"traceId\": \"tr-496\"}"),
    ("422 Unprocessable", "Business Rule Violation", "Insufficient funds or blocked by real-time AML/Fraud check.", "{\"errorCode\": \"ERR_INSUFFICIENT_FUNDS\", \"message\": \"Available balance is insufficient.\", \"traceId\": \"tr-497\"}"),
    ("500 Server Error", "Internal Engine Error", "Database connection loss, unhandled ledger exception.", "{\"errorCode\": \"ERR_INTERNAL_ERROR\", \"message\": \"Ledger error; transaction rolled back.\", \"traceId\": \"tr-498\"}"),
    ("503 Unavailable", "Service Down", "Core banking service circuit breaker open.", "{\"errorCode\": \"ERR_SERVICE_UNAVAILABLE\", \"message\": \"Core ledger busy. Retry later.\", \"traceId\": \"tr-499\"}")
]

for idx, data in enumerate(task3_data):
    if idx + 1 < len(t4.rows):
        row = t4.rows[idx + 1]
    else:
        row = t4.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 4: Table 5 (Diagram image insertion)
t5 = doc.tables[5]
cell5 = t5.rows[0].cells[0]
cell5.text = ""
p_diag = cell5.paragraphs[0]
p_diag.text = "Retail Bank - End-to-End API & Data Flow Diagram:\n"
run_diag = p_diag.add_run()
run_diag.add_picture(img_path, width=Inches(6.0))

# Task 5: Table 6 (Auth & Authorization Mechanisms)
t6 = doc.tables[6]
task5_data = [
    ("Authentication & IAM API", "OAuth 2.0 + PKCE + JWT", "Authorization Code Flow with PKCE S256; short-lived access token TTL = 5 mins; refresh token TTL = 30 mins with single-use rotation."),
    ("Transaction Processing API", "OAuth 2.0 Bearer JWT + mTLS", "Requires JWT token with claims: 'sub', 'scope: transfers:write', 'mfa_verified: true'. Gateway-to-backend communication strictly enforced via mutual TLS (mTLS)."),
    ("Customer Onboarding & KYC API", "OAuth 2.0 + TLS 1.3 + PII Encryption", "Authenticated via onboarding session token; all PII fields (SSN, Passport) field-level encrypted via AES-GCM-256 before persistence."),
    ("Fraud Detection & AML API", "Internal mTLS + Service Mesh RBAC", "Internal inter-service API; accessible only by Transaction Service via mutual TLS with SPIFFE/SPIRE x509 service identities and Envoy authorization."),
    ("Loan Servicing API", "RBAC + Scope Enforcement", "Role-Based Access Control enforcing roles: ['LOAN_OFFICER', 'CREDIT_ANALYST'] or customer ownership claim for read-only self-service."),
    ("Third-Party Credit Bureau API", "API Key + Static IP Whitelist + mTLS", "External egress traffic routed through dedicated NAT Gateways with static public IP whitelisting; credentials stored in HashiCorp Vault; TLS 1.3 certificate pinning.")
]

for idx, data in enumerate(task5_data):
    if idx + 1 < len(t6.rows):
        row = t6.rows[idx + 1]
    else:
        row = t6.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 6: Table 7 (Validation Checklist)
t7 = doc.tables[7]
for row in t7.rows[1:]:
    row.cells[1].text = "Yes"

doc.save(out_path)
print("Successfully generated completed docx for API Documentation Lab!")
