# Lab: Documenting APIs and Data Flows - Solution

**Course:** IBM System Design - Capstone Project  
**Module:** Module 5 - System Testing and Deployment Strategies  
**Target System:** Retail Bank Digital Core Platform (Onboarding, Payments, Loans, Fraud/AML, Identity)  
**Author:** Parikshit Jain  

---

## Task 1: Identify Key APIs

Comprehensive inventory of internal and external APIs across the retail bank architecture:

| API Name | Purpose | Internal / External | Primary Consumer | Notes |
| :--- | :--- | :---: | :--- | :--- |
| **Authentication & IAM API** | User authentication, MFA challenge/verify, OAuth2 token issuance, and session management. | Internal / Edge | Web & Mobile Banking Apps, Internal Services | Enforces OAuth2 + PKCE; issues short-lived JWT tokens (5m TTL). |
| **Transaction Processing API** | Executes real-time fund transfers, bill payments, and balance debit/credits. | Internal | Mobile App, Web Portal, ATM Switch, Open Banking API | Core transactional engine; enforces strict idempotency and ACID ledger commits. |
| **Customer Onboarding & KYC API** | Collects applicant profile details, triggers identity verification, and initiates account setup. | Internal / Edge | Prospective Banking Customers, Branch Operators | Encrypts sensitive PII; manages multi-step onboarding state machine. |
| **Fraud Detection & AML API** | Real-time transaction risk scoring, AML threshold evaluation, and sanctions checks. | Internal | Transaction Service, Loan Servicing Engine | Latency SLA < 150ms; synchronous scoring before payment authorization. |
| **Loan Servicing & Eligibility API**| Assesses credit limits, debt-to-income (DTI) ratio, and manages loan disbursement schedules. | Internal | Customer Loan Portal, Credit Operations Team | Orchestrates internal financial history and external credit scores. |
| **Notifications API** | Sends transactional alerts, OTP passcodes, and statement notices via SMS, Email, and Push. | Internal | Auth Service, Transaction Core, Marketing Systems | Asynchronous Kafka event consumer with guaranteed delivery retries. |
| **Third-Party Credit Bureau API** | Retrieves external credit scores (e.g., FICO / Experian) and credit history reports. | **External** | Loan Servicing Engine, Fraud Service | Consumed via REST/JSON with API Key, mutual TLS, and egress IP whitelisting. |

---

## Task 2: Document API Endpoints (2 Core APIs)

### API 1: Transaction Processing API

- **API Name:** Transaction Processing API
- **Base URL:** `https://api.retailbank.com/v1/transactions`

#### Endpoint 1.1: Initiate Internal Fund Transfer
- **Method:** `POST`
- **Path:** `/transfers`
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer <JWT_ACCESS_TOKEN>`
  - `X-Idempotency-Key: 7b9a528e-8a21-4f76-bc34-45300fbf5632`
  - `X-Correlation-ID: corr-txn-984210`
- **Authentication Required:** OAuth 2.0 / JWT (`scope: transfers:write`)
- **Request Parameters:** None (URL path)
- **Request Body:**
  ```json
  {
    "sourceAccountNumber": "ACC-10029384",
    "destinationAccountNumber": "ACC-50019283",
    "amount": 250.00,
    "currency": "USD",
    "paymentReference": "Invoice #4928 payment",
    "transferType": "INTERNAL_TRANSFER"
  }
  ```
- **Success Response (201 Created):**
  ```json
  {
    "transactionId": "TXN-88492019",
    "status": "COMPLETED",
    "sourceAccountNumber": "ACC-10029384",
    "destinationAccountNumber": "ACC-50019283",
    "amount": 250.00,
    "currency": "USD",
    "fee": 0.00,
    "timestamp": "2026-11-19T14:52:00Z",
    "remainingBalance": 1250.75,
    "traceId": "corr-txn-984210"
  }
  ```
- **Error Responses:**
  - `400 Bad Request`: `ERR_INSUFFICIENT_FUNDS`
  - `401 Unauthorized`: `ERR_INVALID_OR_EXPIRED_TOKEN`
  - `409 Conflict`: `ERR_DUPLICATE_IDEMPOTENCY_KEY`
  - `422 Unprocessable Entity`: `ERR_FRAUD_HOLD_TRIGGERED`
- **Example cURL Request:**
  ```bash
  curl -X POST "https://api.retailbank.com/v1/transactions/transfers" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..." \
    -H "X-Idempotency-Key: 7b9a528e-8a21-4f76-bc34-45300fbf5632" \
    -d '{
      "sourceAccountNumber": "ACC-10029384",
      "destinationAccountNumber": "ACC-50019283",
      "amount": 250.00,
      "currency": "USD",
      "paymentReference": "Invoice #4928 payment",
      "transferType": "INTERNAL_TRANSFER"
    }'
  ```

#### Endpoint 1.2: Get Transaction Details by ID
- **Method:** `GET`
- **Path:** `/transfers/{transactionId}`
- **Headers:**
  - `Authorization: Bearer <JWT_ACCESS_TOKEN>`
  - `Accept: application/json`
- **Authentication Required:** OAuth 2.0 / JWT (`scope: transfers:read`)
- **Request Parameters:** Path parameter `transactionId` (string, e.g. `TXN-88492019`)
- **Success Response (200 OK):**
  ```json
  {
    "transactionId": "TXN-88492019",
    "status": "COMPLETED",
    "amount": 250.00,
    "currency": "USD",
    "timestamp": "2026-11-19T14:52:00Z",
    "settlementStatus": "SETTLED_ON_LEDGER"
  }
  ```
- **Error Responses:**
  - `404 Not Found`: `ERR_TRANSACTION_NOT_FOUND`
  - `403 Forbidden`: `ERR_ACCESS_DENIED_TO_ACCOUNT`

---

### API 2: Authentication & IAM API

- **API Name:** Authentication & IAM API
- **Base URL:** `https://auth.retailbank.com/v1/oauth2`

#### Endpoint 2.1: User Login & Initial Challenge
- **Method:** `POST`
- **Path:** `/token`
- **Headers:**
  - `Content-Type: application/x-www-form-urlencoded`
- **Authentication Required:** Client Credentials / OAuth 2.0 PKCE
- **Request Body (Form URL-Encoded):**
  ```
  grant_type=authorization_code&code=splat923847&redirect_uri=https://app.retailbank.com/callback&client_id=retail-mobile-app&code_verifier=dBjftJeZ4CVP-mB92K...
  ```
- **Success Response (200 OK):**
  ```json
  {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "Bearer",
    "expires_in": 300,
    "refresh_token": "r_9921849182390123",
    "scope": "openid profile accounts:read transfers:write",
    "requiresMfa": false
  }
  ```
- **Error Responses:**
  - `401 Unauthorized`: `ERR_INVALID_CREDENTIALS` (or `ERR_ACCOUNT_LOCKED_5_ATTEMPTS`)
  - `400 Bad Request`: `ERR_INVALID_PKCE_VERIFIER`

#### Endpoint 2.2: Multi-Factor Authentication (MFA) Verification
- **Method:** `POST`
- **Path:** `/mfa/verify`
- **Headers:**
  - `Content-Type: application/json`
  - `X-MFA-Session-Token: mfa_sess_8892193`
- **Authentication Required:** MFA Session Token
- **Request Body:**
  ```json
  {
    "otpCode": "849201",
    "mfaType": "TOTP"
  }
  ```
- **Success Response (200 OK):**
  ```json
  {
    "status": "VERIFIED",
    "access_token": "eyJhbGciOiJSUzI1NiIsIm1mYSI6dHJ1ZX0...",
    "expires_in": 300
  }
  ```
- **Error Responses:**
  - `400 Bad Request`: `ERR_MFA_EXPIRED_OR_INVALID`
  - `429 Too Many Requests`: `ERR_MFA_RATE_LIMIT_EXCEEDED`

---

## Task 3: Define Status Codes and Error Handling

Standardized HTTP status codes and uniform error payload contract across all core banking services:

| Status Code | Meaning | Trigger Condition | Example Error Payload |
| :--- | :--- | :--- | :--- |
| **200 OK** | Request Succeeded | Normal query completion, balance checks, successful verification. | *N/A (Standard data payload)* |
| **201 Created** | Resource Created | Successful fund transfer execution, new account creation. | `{"transactionId": "TXN-88492019", "status": "COMPLETED"}` |
| **400 Bad Request** | Invalid Input Data | Malformed JSON, negative transfer amounts, missing required fields. | `{"errorCode": "ERR_INVALID_PAYLOAD", "message": "Transfer amount must be greater than zero.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-492"}` |
| **401 Unauthorized**| Authentication Failed | Missing or expired JWT access token, invalid client credentials. | `{"errorCode": "ERR_UNAUTHORIZED", "message": "JWT token has expired. Please re-authenticate.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-493"}` |
| **403 Forbidden** | Authorization Denied | User attempts to access an account owned by another customer. | `{"errorCode": "ERR_FORBIDDEN", "message": "Insufficient permissions to debit account.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-494"}` |
| **404 Not Found** | Resource Missing | Non-existent transaction ID or beneficiary account number. | `{"errorCode": "ERR_ACCOUNT_NOT_FOUND", "message": "Target account ACC-50019283 does not exist.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-495"}` |
| **409 Conflict** | Concurrency / Duplicate | Replay of existing `X-Idempotency-Key` or concurrent balance write. | `{"errorCode": "ERR_DUPLICATE_IDEMPOTENCY", "message": "Transaction already processed.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-496"}` |
| **422 Unprocessable**| Business Rule Violation | Transfer exceeds available balance or blocked by AML/Fraud rules. | `{"errorCode": "ERR_INSUFFICIENT_FUNDS", "message": "Available balance $150.00 is less than $250.00.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-497"}` |
| **500 Server Error**| Internal Engine Failure | Database connection failure, unhandled microservice exception. | `{"errorCode": "ERR_INTERNAL_ERROR", "message": "Ledger processing failed. Rollback executed.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-498"}` |
| **503 Unavailable** | Temporary Outage | Downstream core banking service circuit breaker is open. | `{"errorCode": "ERR_SERVICE_UNAVAILABLE", "message": "Core ledger undergoing maintenance. Retry later.", "timestamp": "2026-11-19T14:52:00Z", "traceId": "tr-499"}` |

---

## Task 4: API Data Flow Diagram

```
+-------------------------------------------------------------------------------------------------------------------------------+
|                                      RETAIL BANK END-TO-END TRANSACTION DATA FLOW                                              |
+-------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                               |
|  [1. Client Apps]              [2. API Gateway]               [3. Transaction Service]           [4. Fraud & Risk Engine]     |
|  +-------------------+         +--------------------+         +------------------------+         +-----------------------+    |
|  | Mobile / Web App  |         | Kong Edge Gateway  |         | Payment Core Orchestr. |         | AI Real-Time Scoring  |    |
|  | - Initiates $250  | ------> | - Terminates TLS1.3| ------> | - Validates Idempotency| ------> | - Real-time ML rules  |    |
|  |   transfer        |         | - Verifies JWT     |         | - Coordinates SAGA     |         | - Sanctions screening |    |
|  | - Sends Bearer JWT|         | - Rate limits req  |         |   transaction          |         | - Returns Approved/   |    |
|  +-------------------+         +--------------------+         +------------------------+         |   Hold in < 150ms     |    |
|           ^                              ^                                 |                     +-----------------------+    |
|           |                              |                                 v                                 |                |
|           | (HTTP 201 Created)           | (HTTP 201)             [5. Core Banking Ledger]                   |                |
|           +------------------------------+                        +------------------------+                 |                |
|                                                                   | PostgreSQL / Spanner   | <---------------+ (Risk Score OK)|
|                                                                   | - ACID Double Entry    |                                  |
|                                                                   | - Debit Account A      |                                  |
|                                                                   | - Credit Account B     |                                  |
|                                                                   | - Generates Ledger Hash|                                  |
|                                                                   +------------------------+                                  |
|                                                                                |                                              |
|                                                                                v                                              |
|                                                                   [6. Notification & External]                                |
|                                                                   +--------------------------+                                |
|                                                                   | Kafka Event Bus          |                                |
|                                                                   | - Publishes Txn Completed|                                |
|                                                                   | - Sends SMS / Push Alert |                                |
|                                                                   | - External SWIFT / ACH   |                                |
|                                                                   | - Audit Trail to WORM S3 |                                |
|                                                                   +--------------------------+                                |
|                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------+
```
*(Sơ đồ đồ họa PDF và PNG độ phân giải cao đã được xuất lưu tại `API_dataflow for retail bank.pdf` và `API_dataflow for retail bank.png`).*

---

## Task 5: Specify Authentication and Authorization Mechanisms

Summary of security specifications for all core banking APIs:

| API | Security Mechanism | Technical Implementation Details |
| :--- | :--- | :--- |
| **Authentication & IAM API** | **OAuth 2.0 + PKCE + JWT** | Authorization Code Flow with Proof Key for Code Exchange (PKCE S256). Short-lived access token TTL = 5 minutes. Refresh token TTL = 30 minutes with single-use rotation and replay detection. |
| **Transaction Processing API** | **OAuth 2.0 Bearer JWT + mTLS** | Requires JWT token containing claims: `sub`, `scope: transfers:write`, `account_id`, `mfa_verified: true`. Gateway to service communication strictly enforced via mutual TLS (mTLS). |
| **Customer Onboarding & KYC API** | **OAuth 2.0 + TLS 1.3 + PII Encryption** | Authenticated via temporary onboarding session token; all payload fields containing PII (SSN, Passport) are field-level encrypted using AES-GCM-256 before persistence. |
| **Fraud Detection & AML API** | **Internal mTLS + Service Mesh RBAC** | Internal inter-service API. Accessible only by Transaction Service via mutual TLS with SPIFFE/SPIRE x509 service identities and Envoy mesh authorization policies. |
| **Loan Servicing API** | **RBAC + Scope Enforcement** | Role-Based Access Control enforcing `roles: ["LOAN_OFFICER", "CREDIT_ANALYST"]` or matching customer ID claim for read-only self-service applicant views. |
| **Third-Party Credit Bureau API** | **API Key + Static IP Whitelist + mTLS** | External egress traffic routed through dedicated NAT Gateways with static public IP whitelisting; credentials stored in HashiCorp Vault; TLS 1.3 certificate pinning. |

---

## Task 6: Validate Checklist

| Validation Item | Yes/No | Verification Evidence |
| :--- | :---: | :--- |
| **APIs identified clearly** | **Yes** | 7 core internal and external APIs inventoried and classified in Task 1. |
| **Endpoints fully documented** | **Yes** | Full endpoint specification (Methods, Paths, Headers, Auth, Payloads, Responses) documented in Task 2. |
| **Request/response examples included** | **Yes** | Practical cURL examples, 200/201 JSON success bodies, and error bodies provided. |
| **Error handling defined** | **Yes** | Standardized HTTP status codes (200, 201, 400, 401, 403, 404, 409, 422, 500, 503) mapped to uniform error contracts in Task 3. |
| **Data flow diagram added** | **Yes** | Multi-tier end-to-end data flow illustrated with diagram exported to PDF/PNG and embedded into Word document. |
| **Authentication and authorization are documented** | **Yes** | Addressed OAuth2 PKCE, JWT claims, 5-minute token TTL, mTLS, API keys, and IP whitelisting in Task 5. |
| **Documentation is clear and testable** | **Yes** | All request and response structures follow RFC standards and are directly importable into Postman or OpenAPI 3.0. |
