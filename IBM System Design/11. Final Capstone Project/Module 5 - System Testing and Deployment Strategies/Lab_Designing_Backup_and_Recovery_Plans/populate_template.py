import docx
from docx.shared import Inches
import os

src_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Designing_Backup_and_Recovery_Plans\Template.docx"
out_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Designing_Backup_and_Recovery_Plans\Completed_Template_Designing_Backup_and_Recovery_Plans.docx"
img_path = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Designing_Backup_and_Recovery_Plans\Retail bank_recovery workflow.png"

doc = docx.Document(src_path)

# Task 1: Table 0 (Inventory of Critical Systems)
t0 = doc.tables[0]
task1_data = [
    ("Core Banking System (Ledger & Accounts)", "Transaction ledger, balances, deposits, ACID journal logs", "High", "System of record; data loss causes financial discrepancies and halts operations.", "PCI-DSS, FFIEC, Central Bank (Zero data loss)"),
    ("Customer Onboarding Service", "Customer PII, identity records, KYC docs (IDs, Passports)", "High", "Essential for customer identification, compliance verification, and lifecycle management.", "GDPR, FFIEC, KYC / AML Regulations"),
    ("Loan Servicing Database", "Loan applications, credit risk scoring, payment schedules, collateral", "High", "Required for interest accounting, loan recovery, and regulatory capital calculation.", "Consumer Credit Regulations, IFRS 9 / BASEL III"),
    ("Fraud Detection & AML Engine", "Suspicious transaction logs, blacklist feeds, ML model states, AML alerts", "High", "Legal mandate to detect financial crime; lost logs invalidate AML regulatory audits.", "Bank Secrecy Act (BSA), FinCEN AML Mandate"),
    ("Configuration Repository (Git)", "Kubernetes manifests, Terraform IaC, Helm charts, CI/CD pipelines", "Medium", "Needed to deterministically rebuild the banking infrastructure in a secondary region.", "FFIEC, ISO 27001 (Change Management)"),
    ("API Gateway & IAM Policies", "Routing tables, OAuth2/OIDC clients, RBAC roles, rate limiting rules", "Medium", "Controls system perimeter security and inter-service authentication routing.", "PCI-DSS Section 7/8, SOC 2 Type II"),
    ("Application & Access Logs", "Nginx ingress logs, microservice JSON logs, security access trails", "Medium", "Critical for security anomaly detection, forensic audits, and debugging.", "FFIEC Audit Requirements, PCI-DSS Log Retention")
]

for idx, data in enumerate(task1_data):
    row = t0.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 2: Table 1 (Backup Frequency and Retention Policies)
t1 = doc.tables[1]
task2_data = [
    ("Transaction DB (Core Ledger)", "Restricted / Confidential", "Continuous WAL streaming + Hourly snapshots + Daily full", "7 Years (Immutable WORM)", "< 15 Mins", "< 1 Min"),
    ("Customer PII & KYC Records", "Confidential / Sensitive PII", "Daily incremental + Weekly full", "5 Years post account closure", "< 30 Mins", "< 1 Hour"),
    ("Loan Records & Credit Files", "Confidential", "Daily differential + Weekly full", "7 Years post loan payoff", "< 1 Hour", "< 1 Hour"),
    ("Audit Logs & AML Alerts", "Restricted / Compliance", "Real-time log streaming (Kafka) + Hourly batch archive", "5 to 7 Years (Tamper-proof)", "< 2 Hours", "< 5 Mins"),
    ("Configuration Files & Git", "Internal / Proprietary", "On every commit (Git) + Daily bundle snapshot", "3 Years (All release tags)", "< 15 Mins", "0 (Git history)"),
    ("Application Container Images", "Internal", "On each CI/CD release + Mirror to secondary registry", "Last 10 production versions", "< 15 Mins", "N/A (Stateless)")
]

for idx, data in enumerate(task2_data):
    row = t1.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 3: Table 2 (Backup Strategies)
t2 = doc.tables[2]
task3_data = [
    ("Core Banking Transaction Database (PostgreSQL / Spanner)", "Continuous Point-in-Time Recovery (PITR) + Daily Full Backup", "Transaction processing requires near-zero RPO. Continuous WAL archiving to S3 enables restoring to any exact millisecond, while daily full backups establish a solid baseline."),
    ("Application & Compliance Audit Logs (Kafka / Elastic)", "Incremental Continuous Streaming + Daily Encrypted Tarball Archive", "Logs are append-only. Streaming to immutable cloud object storage ensures real-time capture without impacting application throughput, with daily archives compressed for cost efficiency."),
    ("Configuration Repository & Infrastructure as Code (GitOps)", "Differential Snapshot + Automated Multi-Region Mirroring", "Configuration data is compact and tracked via Git. Mirroring the repository to an offsite secondary cloud provider on each release provides immediate infrastructure rebuilding capability with negligible storage overhead.")
]

for idx, data in enumerate(task3_data):
    row = t2.rows[idx + 1]
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 4: Paragraphs filling
# Update paragraphs under Task 4
for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith("RTO:"):
        p.text = "RTO: <= 15 Minutes for Core Banking / Payments; <= 1 Hour for non-critical servicing."
    elif text.startswith("RPO:"):
        p.text = "RPO: <= 1 Minute for financial transactions; <= 15 Minutes for customer profile data."
    elif "Active-passive/Active-active/Warm-standby/Pilot-light" in text or text.startswith("Justification:"):
        p.text = "Failover strategy: Warm Standby (Multi-Region Active-Passive with Hot Data Replica)\nJustification: A Warm Standby strategy provides an optimal balance between low recovery time (< 15 mins RTO) and cost-efficiency. Active-active introduces extreme multi-region distributed transaction latency and complex consensus locks on ledger databases. Warm standby maintains an active, synchronously/asynchronously replicated database in Region B with auto-scaling compute capacity ready to handle full load."
    elif text.startswith("Systems covered"):
        # We can fill the next paragraph or this one
        pass

# Let's inspect exact paragraphs around Task 4 to set text cleanly
for i, p in enumerate(doc.paragraphs):
    if p.text.startswith("Systems covered"):
        doc.paragraphs[i+1].text = "Core Banking Ledger & Accounts Service, Customer Onboarding & KYC API, Loan Engine, Anti-Fraud & AML Processor, API Gateway, and Cloud Identity/IAM."
    elif p.text.startswith("DR environment"):
        doc.paragraphs[i+1].text = "Primary Region: us-east-1 (Primary Cloud Datacenter); Secondary DR Region: us-west-2 (Geographically isolated >500km). Mirrored VPC, Transit Gateway, automated Route 53 DNS failover with latency/health routing, and pre-warmed Kubernetes worker node pools."
    elif p.text.startswith("DR execution steps"):
        steps = [
            "1. Disaster Declaration: Monitoring systems fire critical P1 alert; Incident Commander confirms primary region outage (>5 mins unrecoverable) and formally declares DR.",
            "2. Database Promotion: Promote secondary read-replica database in Region B to primary read-write master; apply latest WAL logs for point-in-time consistency.",
            "3. Compute Scale-Up: Trigger Kubernetes cluster autoscaler in Region B to scale stateless microservice deployments from warm standby capacity (20%) to 100% production capacity.",
            "4. DNS & Traffic Re-routing: Update Global Anycast DNS / CloudFront / Route 53 health-check records to redirect all incoming customer and payment traffic to Region B API Gateway.",
            "5. Data & Service Integrity Verification: Run automated synthetic financial smoke tests (probe balance query, initiate test transaction, verify ledger checksums).",
            "6. Operational Sign-Off & Notification: Notify executive leadership, regulatory bodies, and operations teams of successful failover."
        ]
        for step_idx, step_text in enumerate(steps):
            doc.paragraphs[i+1+step_idx].text = step_text
    elif p.text.startswith("Compliance and audit requirements"):
        doc.paragraphs[i+1].text = "Bi-annual mandatory unannounced DR failover drills in accordance with FFIEC Appendices A & J and PCI-DSS Requirement 12.10. Full cryptographic audit logs verifying zero loss or corruption of financial transactions."

# Task 5: Table 3 (Backup Storage Architecture)
t3 = doc.tables[3]
task5_data = [
    ("Object Storage (Hot / S3 / GCS)", "Hourly database WAL logs, daily database snapshots, container images", "AES-256 server-side encryption (KMS managed keys), TLS 1.3 in-transit, S3 Object Lock (Compliance Mode WORM), Bucket Versioning enabled", "30 to 90 Days", "Fast retrieval for rapid point-in-time restoration."),
    ("Block Storage Snapshots (EBS / Persistent Disks)", "Immediate state recovery of persistent application volumes and caching nodes", "KMS volume encryption with customer-managed keys (CMK), automated snapshot lifecycle policies, Cross-Region snapshot replication", "7 to 14 Days", "Instant volume attachment for immediate recovery without network transfer overhead."),
    ("Archival / Cold Storage (Glacier / Cloud Storage Archive)", "Historical transaction archives, 7-year audit logs, tax and compliance records", "Immutable WORM storage, Multi-Factor Authentication (MFA) Delete enforced, strict IAM role-based access control (RBAC), KMS envelope encryption", "7 to 10 Years", "Cost-effective, tamper-proof long-term regulatory compliance storage.")
]

# Table 3 has 3 rows (1 header + 2 data). Let's expand if needed
for idx, data in enumerate(task5_data):
    if idx + 1 < len(t3.rows):
        row = t3.rows[idx + 1]
    else:
        row = t3.add_row()
    for c_idx, val in enumerate(data):
        row.cells[c_idx].text = val

# Task 6: Table 4 (Insert diagram image)
t4 = doc.tables[4]
cell = t4.rows[0].cells[0]
cell.text = "" # clear placeholder
p_img = cell.paragraphs[0]
p_img.text = "Retail Bank - Disaster Recovery & Restoration Workflow:\n"
run = p_img.add_run()
run.add_picture(img_path, width=Inches(6.0))

# Task 7: Table 5 (Validation Checklist)
t5 = doc.tables[5]
for row in t5.rows[1:]:
    row.cells[1].text = "Yes"

doc.save(out_path)
print("Successfully generated completed docx for Backup & Recovery Plans!")
