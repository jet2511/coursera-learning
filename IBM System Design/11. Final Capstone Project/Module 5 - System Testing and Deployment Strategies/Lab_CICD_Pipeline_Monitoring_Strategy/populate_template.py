import docx

src_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_CICD_Pipeline_Monitoring_Strategy\Template.docx"
out_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_CICD_Pipeline_Monitoring_Strategy\Completed_Template_Create_a_CICD_Pipeline_and_Monitoring_Strategy.docx"

doc = docx.Document(src_path)

# Task 1: Table 0 (Diagram & Stages)
t0 = doc.tables[0]
diagram_text = """[RETAIL BANK DIGITAL CORE - ENTERPRISE REGULATED CI/CD PIPELINE]

1. Code Commit (Developer): Git feature push, pre-commit secret scanning (Gitleaks).
2. Build Stage (Developer/DevOps): Compile binaries, run isolated TDD unit tests, package container images.
3. DevSecOps Security Gate (DevSecOps Engineer): SAST scan (SonarQube), SCA dependency analysis (Snyk), Container image scanning (Trivy). Blocks on High/Critical vulnerabilities.
4. Automated Testing Stage (QA Engineer): Integration tests (Kafka/PostgreSQL), API contract tests (Pact), automated regression suites.
5. Staging Deployment (DevOps Engineer): Deploy to staging Kubernetes cluster, run synthetic smoke tests, dynamic security testing (DAST).
6. Change Approval Gate (Architect & Release Manager): Architecture review, QA sign-off verification, Change Advisory Board (CAB) approval.
7. Production Deployment (DevOps & Release Manager): Canary release (10% -> 50% -> 100%) or Blue-Green traffic swap; runtime secrets injection via Vault/KMS.
8. Automated Rollback Strategy (SRE / Automated Pipeline): Health checks & error rate monitoring. Auto-revert traffic to previous stable version if error rate > 1% or latency spikes.
9. Audit & Compliance Logging (Compliance & SecOps): Immutable deployment logs, commit hashes, security scan reports preserved for FFIEC, PCI-DSS compliance audits."""
t0.rows[0].cells[0].text = diagram_text

# Task 2: Table 1 (Deployment Risks)
t1 = doc.tables[1]
risk_data = [
    ("Service Crash / Deployment Failure", 
     "Container restart loops (CrashLoopBackOff) or failed Kubernetes health checks within 60s of release.", 
     "Canary deployment (10% pod slice); automated container health check gates before scaling.", 
     "Automated rollback via ArgoCD/Kubernetes: immediately re-route 100% ingress traffic to previous stable ReplicaSet."),
    ("API Contract Incompatibility", 
     "Spike in HTTP 400/404 errors (>2% total traffic) between frontend and core banking microservices.", 
     "Enforce consumer-driven contract testing (Pact) in CI; maintain backward-compatible API versioning (/v1, /v2).", 
     "Instant Blue-Green router switch at API Gateway to the previous stable Blue target group within 5 seconds."),
    ("Configuration / Secret Injection Error", 
     "Spike in HTTP 500 errors, database authentication failures, or missing HashiCorp Vault secrets.", 
     "Strict 12-Factor App separation of config and code; automated secret validation pre-flight check.", 
     "Redeploy previous known-good config map revision from GitOps repository; trigger rolling pod restart."),
    ("Database Migration Lock / Schema Error", 
     "DB migration lock timeout, connection pool exhaustion, or DB query latency > 2,000ms.", 
     "Follow Expand-Contract (parallel-run) migration pattern; non-blocking DDL migrations.", 
     "Execute automated Flyway/Liquibase rollback script; re-point DB connection pool to previous schema revision.")
]

for idx, data in enumerate(risk_data):
    row = t1.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 3: Table 2 (Step 1: Define KPIs)
t2 = doc.tables[2]
kpi_text = """Key Performance Indicators (KPIs) for Retail Banking Core Services:
1. Latency (API Response Time): Measures p95 and p99 response duration across critical banking APIs (e.g., balance check, fund transfers).
2. Availability (%): Percentage of total uptime and successful requests across all digital core endpoints (Target SLA: 99.99%).
3. Transaction Throughput (TPS): Volume of financial transactions successfully processed per second through core ledger.
4. Error Rate (%): Percentage of failed transactions (HTTP 5xx server errors, unhandled exceptions) relative to total volume.
5. Fraud Rule Engine Execution Time: Real-time fraud detection and risk assessment processing duration per transaction (Target: < 150ms).
6. Database Replication Lag: Latency in milliseconds between primary transactional DB (PostgreSQL/Spanner) and read replicas."""
t2.rows[0].cells[0].text = kpi_text

# Task 3: Table 3 (Step 2: Alert Triggers and Thresholds)
t3 = doc.tables[3]
alert_data = [
    ("Latency (p99)", "p99 > 800ms for 3 consecutive mins", "API Gateway p99 latency breaches 800ms sustained", "P2 - Major", "PagerDuty to On-call SRE, Slack #alerts-core-banking"),
    ("Availability", "< 99.90% over 5-minute rolling window", "Failed health checks or success ratio drops below 99.90%", "P1 - Critical", "PagerDuty voice call to Incident Commander & SRE Lead, SMS"),
    ("Error Rate", "5xx error rate > 1.0% over 2 minutes", "Sustained spike in HTTP 500/502/503 errors", "P1 - Critical", "PagerDuty immediate dispatch, Automated Incident Bridge"),
    ("Fraud Engine Time", "> 200ms per transaction", "Fraud evaluation duration exceeds real-time processing limit", "P2 - Major", "Slack alert to Fraud Engineering, Jira auto-ticket"),
    ("Database Replication Lag", "Lag > 1,000ms (1 second)", "Secondary DB replica lag exceeds acceptable sync threshold", "P3 - Moderate", "Email to Database Admin (DBA), Slack #db-monitoring")
]

# Table 3 has 4 rows originally (1 header + 3 data). Let's populate and add rows as needed
for idx, data in enumerate(alert_data):
    if idx + 1 < len(t3.rows):
        row = t3.rows[idx + 1]
    else:
        row = t3.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 3: Table 4 (Step 3: Escalation Path)
t4 = doc.tables[4]
escalation_data = [
    ("Level 1 (L1)", "Primary On-Call SRE / DevOps Engineer", "5 minutes"),
    ("Level 2 (L2)", "Lead Backend Architect & Domain Tech Lead", "15 minutes"),
    ("Level 3 (L3)", "Incident Commander, VP of Engineering, Chief Risk Officer", "30 minutes")
]

for idx, data in enumerate(escalation_data):
    row = t4.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 3: Table 5 (Step 4: Post-Mortem Workflow)
t5 = doc.tables[5]
post_mortem_text = """Incident Post-Mortem Workflow (Blameless RCA):
1. Incident Summary: Executive summary covering incident timestamp, severity (P1/P2), duration, impacted banking services, and customer/financial impact.
2. Timeline Reconstruction: Chronological, minute-by-minute sequence of events from commit/deployment, alert trigger, triage, rollback, to full service recovery.
3. Root Cause Analysis (RCA): Structured '5 Whys' investigation identifying the underlying systemic, architectural, or procedural defect rather than surface symptoms.
4. Fix Validation & Remediation: Documentation of immediate mitigation (e.g., Canary rollback) and permanent code/infrastructure fixes verified via regression tests.
5. Corrective and Preventive Actions (CAPA): Actionable, prioritized Jira tickets assigned to engineering teams to eliminate recurrence and enhance test coverage.
6. Regulatory & Compliance Reporting: Preparation and filing of mandatory incident reports for financial regulatory compliance (FFIEC, Central Bank, PCI-DSS) within mandated timeframes."""
t5.rows[0].cells[0].text = post_mortem_text

# Task 4: Table 6 (Checklist)
t6 = doc.tables[6]
checklist_answers = ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
for idx, ans in enumerate(checklist_answers):
    t6.rows[idx + 1].cells[1].text = ans

doc.save(out_path)
print("Successfully generated completed docx for CI/CD & Monitoring Lab!")
