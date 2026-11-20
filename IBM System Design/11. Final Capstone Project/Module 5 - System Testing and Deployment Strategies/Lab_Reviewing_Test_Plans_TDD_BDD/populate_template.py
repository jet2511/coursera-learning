import docx

src_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Reviewing_Test_Plans_TDD_BDD\Template.docx"
out_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Reviewing_Test_Plans_TDD_BDD\Completed_Template_Reviewing_Test_Plans_and_Creating_TDDBDD_Test_Cases.docx"

doc = docx.Document(src_path)

# Task 1: Findings
findings = [
    "1. Missing Negative & Failure Testing for MFA: The plan specifies MFA in security scope, but defines zero test cases for expired OTPs, account lockout after repeated failures, or token replay.",
    "2. Missing Negative Tests for Invalid/Fraudulent KYC Documents: Only successful document validation is covered; completely lacks tests for expired IDs, corrupted uploads, and synthetic fraud.",
    "3. No Test Cases Validating AML Thresholds & Fraud Scoring: AML monitoring is in-scope, but the plan omits test cases for transactions exceeding $10,000, smurfing/structuring patterns, and automated freezing.",
    "4. Duplicate Test Cases for Account Balance Retrieval: Redundant scenarios test balance retrieval via API and DB query without differentiating between cached vs ledger-settled balance.",
    "5. Weak Acceptance Criteria for Microservice Resilience: Inter-service communication (KYC -> Account -> Loan -> Fraud -> Ledger) lacks latency limits, timeout handling, and Kafka DLQ verification.",
    "6. Missing Compensating Actions & SAGA Rollback Scenarios: No tests validate automated rollbacks when a downstream service fails during multi-step customer journeys.",
    "7. Omission of Audit Log Immutability and Compliance Verification: No test cases assert that financial logs are tamper-evident, non-repudiable, and mask sensitive PII."
]

insert_point = doc.paragraphs[4]
for f in reversed(findings):
    insert_point.insert_paragraph_before(f)

# Table 0: RTM
t0 = doc.tables[0]
rtm_data = [
    ("RQ-AUTH-01", "Multi-Factor Authentication (MFA) must be enforced for login and high-value transfers.", "TC-SEC-0101", "No", "Missing negative test cases: only positive login is mapped; lacks OTP expiry and lockout."),
    ("RQ-KYC-02", "Customer identity documents must be validated against national registry before activation.", "TC-KYC-0201", "No", "Requires additional negative testing: lacks invalid/expired ID rejection scenarios."),
    ("RQ-ACCT-03", "Core account creation must assign unique IBAN and initialize zero-balance ledger.", "TC-ACC-0101, TC-ACC-0102", "No", "Outdated mapping: TC-ACC-0102 is a duplicate balance query, not account creation."),
    ("RQ-TXN-04", "Real-time internal fund transfers must complete within 500ms with ACID ledger update.", "TC-TXN-0301, TC-TXN-0302", "Yes", "Fully covered for internal debit/credit ledger balance updates."),
    ("RQ-AML-05", "Transactions exceeding $10,000 or high velocity must trigger automated AML hold.", "None", "No", "Missing test case: critical compliance gap for AML detection and reporting."),
    ("RQ-LOAN-06", "Loan engine evaluates DTI ratio <= 43% and credit score >= 650 for loan approval.", "TC-LOAN-0401, TC-LOAN-0402", "Yes", "Covered for approval and rejection criteria."),
    ("RQ-AUDIT-07", "All financial transactions and state changes must emit immutable audit events.", "TC-AUD-0501", "Yes", "Covers audit event emission to secure datastore.")
]

for i, data in enumerate(rtm_data):
    if i + 1 < len(t0.rows):
        row = t0.rows[i + 1]
    else:
        row = t0.add_row()
    for col_idx, text in enumerate(data):
        row.cells[col_idx].text = text

# Table 1: TDD Case 1
t1 = doc.tables[1]
t1.rows[1].cells[1].text = "TC-TDD-LOAN-001"
t1.rows[2].cells[1].text = "Loan Eligibility Engine"
t1.rows[3].cells[1].text = "Validate applicants meeting minimum income ($30k) and credit score (>=650) are eligible."
t1.rows[4].cells[1].text = "Loan rule engine initialized with baseline risk parameters."
t1.rows[5].cells[1].text = "annualIncome: 45000, creditScore: 720, monthlyDebt: 500, loanAmount: 15000"
t1.rows[6].cells[1].text = "1. Call evaluateEligibility(request)\n2. Assert status == ELIGIBLE\n3. Assert maxApprovedAmount == 15000"
t1.rows[7].cells[1].text = "status: 'ELIGIBLE', maxApprovedAmount: 15000, rejectionReasons: []"
t1.rows[8].cells[1].text = "Exact boundary values: annualIncome == 30000, creditScore == 650."

# Table 2: TDD Case 2
t2 = doc.tables[2]
t2.rows[1].cells[1].text = "TC-TDD-LOAN-002"
t2.rows[2].cells[1].text = "Loan Eligibility Engine"
t2.rows[3].cells[1].text = "Validate rejection when Debt-to-Income (DTI) ratio exceeds 43%."
t2.rows[4].cells[1].text = "Loan rule engine active with standard underwriting policies."
t2.rows[5].cells[1].text = "annualIncome: 60000, creditScore: 750, monthlyDebt: 2300, loanAmount: 20000"
t2.rows[6].cells[1].text = "1. Calculate monthly debt + proposed loan payment ($2700/mo)\n2. Compute DTI: 54%\n3. Call evaluateEligibility(request)"
t2.rows[7].cells[1].text = "status: 'NOT_ELIGIBLE', rejectionReasons: ['ERR_DTI_EXCEEDED_THRESHOLD_43']"
t2.rows[8].cells[1].text = "Boundary testing: DTI at exactly 43.00% (pass) vs 43.01% (reject)."

# Table 3: TDD Case 3
t3 = doc.tables[3]
t3.rows[1].cells[1].text = "TC-TDD-LOAN-003"
t3.rows[2].cells[1].text = "Loan Eligibility Engine"
t3.rows[3].cells[1].text = "Defensively handle invalid or zero income inputs with domain validation exception."
t3.rows[4].cells[1].text = "Engine initialized."
t3.rows[5].cells[1].text = "annualIncome: 0, creditScore: 600, monthlyDebt: 100, loanAmount: 5000"
t3.rows[6].cells[1].text = "1. Invoke evaluateEligibility(request) with annualIncome <= 0\n2. Intercept exception"
t3.rows[7].cells[1].text = "Throws InvalidFinancialDataException('Annual income must be > 0')"
t3.rows[8].cells[1].text = "Negative income values, division by zero, null inputs."

# Table 4: BDD Scenario 1
t4 = doc.tables[4]
t4.rows[0].cells[0].text = """BDD Scenario 1: Customer transfers funds successfully

Given an authenticated customer with account "ACC-12345" has a balance of $500.00
And the beneficiary account "ACC-67890" is active and valid
When the customer initiates a transfer of $200.00 to account "ACC-67890"
And verifies the transfer with a valid MFA passcode
Then the transaction should be approved
And the new balance of account "ACC-12345" should be $300.00
And an immutable audit event should be logged with status "SUCCESS"
"""

# Table 5: BDD Scenario 2
t5 = doc.tables[5]
t5.rows[0].cells[0].text = """BDD Scenario 2: Transfer failure due to insufficient funds

Given an authenticated customer with account "ACC-12345" has a balance of $150.00
And no overdraft facility is enabled on the account
When the customer attempts to transfer $250.00 to account "ACC-67890"
Then the transaction should be declined with error "INSUFFICIENT_FUNDS"
And the balance of account "ACC-12345" should remain unchanged at $150.00
And no balance deduction or ledger debit should occur
"""

# Table 6: Checklist
t6 = doc.tables[6]
checklist_answers = ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
for idx, ans in enumerate(checklist_answers):
    t6.rows[idx + 1].cells[1].text = ans

doc.save(out_path)
print("Successfully generated completed docx!")
