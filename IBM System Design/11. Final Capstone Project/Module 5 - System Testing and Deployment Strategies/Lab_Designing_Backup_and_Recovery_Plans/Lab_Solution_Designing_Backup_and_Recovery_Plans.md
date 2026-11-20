# Lab: Designing Backup and Recovery Plans - Solution

**Course:** IBM System Design - Capstone Project  
**Module:** Module 5 - System Testing and Deployment Strategies  
**Target System:** Retail Bank Digital Core Platform (Core Banking, Onboarding, Loans, Transactions, Fraud/AML)  
**Author:** Parikshit Jain  

---

## Task 1: Identify Critical Systems and Data Assets

Comprehensive inventory of essential banking systems, classified by business function, criticality tier, backup rationale, and regulatory impact:

| System / Component | Data Assets | Criticality (High/Medium/Low) | Reason for Backup | Regulatory Impact |
| :--- | :--- | :---: | :--- | :--- |
| **Core Banking System (Ledger & Accounts)** | Transaction ledger, account balances, deposits, ACID journal logs | **High** | Core system of record; data loss causes financial discrepancies, balance corruption, and immediate halt of operations. | **PCI-DSS, FFIEC, Central Bank Regulations** (Zero data loss requirement) |
| **Customer Onboarding Service** | Customer PII, verified identity records, KYC documents (IDs, passports) | **High** | Critical for customer lifecycle management, identity proofing, and legal customer identification. | **GDPR, FFIEC, KYC / AML Regulations** (Heavy penalties for data loss/breach) |
| **Loan Servicing Database** | Loan applications, credit risk scoring, payment schedules, collateral records | **High** | Required for loan disbursement, interest accounting, debt recovery, and regulatory capital reporting. | **Consumer Credit Regulations, IFRS 9 / BASEL III** |
| **Fraud Detection & AML Engine** | Suspicious activity logs, blacklist feeds, ML model states, AML audit alerts | **High** | Legal mandate to detect financial crime; loss of historical logs invalidates AML regulatory audits. | **Bank Secrecy Act (BSA), FinCEN AML Mandate** |
| **Configuration Repository (Git)** | Kubernetes manifests, Terraform IaC, Helm charts, CI/CD pipelines | **Medium** | Needed to rebuild the cloud infrastructure and microservices deterministically in a new region. | **FFIEC, ISO 27001** (Change management & operational resilience) |
| **API Gateway & IAM Policies** | Routing tables, OAuth2/OIDC clients, RBAC roles, rate limiting policies | **Medium** | Controls system access, perimeter security, and inter-service authentication routing. | **PCI-DSS Section 7/8, SOC 2 Type II** |
| **Application & Access Logs** | Nginx ingress logs, microservice JSON logs, security access trails | **Medium** | Critical for forensics, security anomaly detection, and operational debugging. | **FFIEC Audit Requirements, PCI-DSS Log Retention (1 yr)** |

---

## Task 2: Define Backup Frequency and Retention Policies

Backup schedule, retention rules, and Recovery Objectives (RTO/RPO) categorized by data sensitivity and compliance standards:

| Data Type | Classification | Backup Frequency | Retention Period | RTO | RPO |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Transaction DB (Core Ledger)** | Restricted / Confidential | Continuous WAL streaming + Hourly snapshots + Daily Full | **7 Years** (Immutable WORM storage) | **< 15 Mins** | **< 1 Min** (Near-Zero) |
| **Customer PII & KYC Records** | Confidential / Sensitive PII | Daily incremental + Weekly full | **5 Years** post account closure (or per GDPR retention) | **< 30 Mins** | **< 1 Hour** |
| **Loan Records & Credit Files** | Confidential | Daily differential + Weekly full | **7 Years** post loan payoff | **< 1 Hour** | **< 1 Hour** |
| **Audit Logs & AML Alerts** | Restricted / Compliance | Real-time log streaming (Kafka) + Hourly batch archive | **5 to 7 Years** (tamper-proof) | **< 2 Hours** | **< 5 Mins** |
| **Configuration Files & Git** | Internal / Proprietary | On every commit (Git) + Daily Git bundle snapshot | **3 Years** (all release tags retained) | **< 15 Mins** | **0 (Git history)** |
| **Application Container Images** | Internal | On each CI/CD release + Mirror to secondary registry | Retain last **10 production release versions** | **< 15 Mins** | **N/A (Stateless)** |

---

## Task 3: Select Appropriate Backup Strategies

Mapping backup types (Full, Incremental, Differential, PITR) to system workloads:

| Component | Strategy Type | Justification |
| :--- | :--- | :--- |
| **Core Banking Transaction Database (PostgreSQL / Spanner)** | **Continuous Point-in-Time Recovery (PITR) + Daily Full Backup** | Transaction processing requires near-zero RPO. Continuous Write-Ahead Log (WAL) archiving to cloud object storage allows restoring the ledger to any exact millisecond, while daily full backups establish a deterministic recovery baseline. |
| **Application & Compliance Audit Logs (Kafka / Elastic)** | **Incremental Continuous Streaming + Daily Encrypted Tarball Archive** | Logs are append-only. Streaming to immutable cloud object storage (S3/GCS Object Lock) ensures real-time capture without impacting application throughput, with daily archives compressed for cost efficiency. |
| **Configuration Repository & Infrastructure as Code (GitOps)** | **Differential Snapshot + Automated Multi-Region Mirroring** | Configuration data is compact and tracked via Git. Mirroring the repository to an offsite secondary cloud provider on each release provides immediate infrastructure rebuilding capability with negligible storage overhead. |

---

## Task 4: Draft Disaster Recovery (DR) Plan

### 1. Recovery Objectives
- **Recovery Time Objective (RTO):** $\le 15\text{ minutes}$ for Core Banking & Payment APIs; $\le 1\text{ hour}$ for non-critical servicing.
- **Recovery Point Objective (RPO):** $\le 1\text{ minute}$ for financial transactions; $\le 15\text{ minutes}$ for general customer profile updates.

### 2. Failover Strategy & Justification
- **Selected Strategy:** **Warm Standby / Multi-Region Active-Passive with Hot Data Replica**.
- **Justification:** Financial institutions require strict RTO/RPO guarantees that cold backups cannot satisfy. An active-active multi-region setup introduces complex distributed ledger latency and distributed transaction consensus overhead. Warm standby pairs a live, synchronously/asynchronously replicated database in Region B with auto-scaling compute pods, delivering sub-15-minute RTO at an optimal cost/complexity balance.

### 3. Systems Covered
- Core Banking Ledger & Accounts Service, Customer Onboarding & KYC API, Loan Engine, Anti-Fraud & AML Processor, API Gateway, and Cloud Identity/IAM.

### 4. DR Environment
- **Primary Region:** Primary Cloud Region A (e.g., `us-east-1` / Tier-4 Datacenter).
- **Secondary DR Region:** Geographically separated Cloud Region B (e.g., `us-west-2` / >500km distance to mitigate regional natural disasters).
- **Network & Infrastructure:** Mirrored VPC, Transit Gateway, automated Route 53 DNS failover with latency/health routing, and pre-warmed Kubernetes worker node pools.

### 5. DR Execution Steps
1. **Disaster Declaration:** Monitoring systems fire critical P1 alert; Incident Commander confirms primary region outage (>5 mins unrecoverable) and formally declares DR.
2. **Database Promotion:** Promote secondary read-replica database in Region B to primary read-write master; apply latest WAL logs for point-in-time consistency.
3. **Compute Scale-Up:** Trigger Kubernetes cluster autoscaler in Region B to scale stateless microservice deployments from warm standby capacity (20%) to 100% production capacity.
4. **DNS & Traffic Re-routing:** Update Global Anycast DNS / CloudFront / Route 53 health-check records to redirect all incoming customer and payment traffic to Region B API Gateway.
5. **Data & Service Integrity Verification:** Run automated synthetic financial smoke tests (probe balance query, initiate test transaction, verify ledger checksums).
6. **Operational Sign-Off & Notification:** Notify executive leadership, regulatory bodies, and operations teams of successful failover.

### 6. Compliance and Audit Requirements
- Bi-annual mandatory unannounced DR failover drills in accordance with **FFIEC Appendices A & J** and **PCI-DSS Requirement 12.10**.
- Complete cryptographic proof and audit log retention confirming no financial transaction ledger records were corrupted or lost during transition.

---

## Task 5: Define Backup Storage Architecture

Multi-tier, highly secure backup storage architecture:

| Storage Type | Used For | Security Controls | Retention | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Object Storage (Hot / S3 / GCS)** | Hourly database WAL logs, daily database snapshots, container images | AES-256 server-side encryption (KMS managed keys), TLS 1.3 in-transit, S3 Object Lock (Compliance Mode WORM), Bucket Versioning enabled | **30 to 90 Days** | Fast retrieval for rapid point-in-time restoration. |
| **Block Storage Snapshots (EBS / Persistent Disks)** | Immediate state recovery of persistent application volumes and caching nodes | KMS volume encryption with customer-managed keys (CMK), automated snapshot lifecycle policies, Cross-Region snapshot replication | **7 to 14 Days** | Instant volume attachment for immediate recovery without network transfer overhead. |
| **Archival / Cold Storage (Glacier / Cloud Storage Archive)** | Historical transaction archives, 7-year audit logs, tax and compliance records | Immutable WORM storage, Multi-Factor Authentication (MFA) Delete enforced, strict IAM role-based access control (RBAC), KMS envelope encryption | **7 to 10 Years** | Cost-effective, tamper-proof long-term regulatory compliance storage. |

---

## Task 6: Create a Recovery Workflow Diagram

Flowchart sequence of actions executed after severe data loss or system failure:

```
+--------------------------------------------------------------------------------------------------------------------------+
|                                    RETAIL BANK DISASTER RECOVERY & RESTORATION WORKFLOW                                  |
+--------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                          |
|  +--------------------------+          +--------------------------+          +--------------------------+                |
|  | [1] Failure Detected     |          | [2] Alert Triggered      |          | [3] Assess Impact        |                |
|  | - Health checks fail     | -------> | - PagerDuty P1 critical  | -------> | - Triage blast radius    |                |
|  | - Primary DB unreachable |          | - Incident Commander     |          | - Evaluate RTO/RPO       |                |
|  +--------------------------+          |   dispatched             |          |   thresholds             |                |
|                                        +--------------------------+          +--------------------------+                |
|                                                                                             |                            |
|                                                                                             v                            |
|  +--------------------------+          +--------------------------+          +--------------------------+                |
|  | [6] Restore Systems      |          | [5] Retrieve Backups     |          | [4] Start DR Process     |                |
|  | - Promote DB replica     | <------- | - Restore latest WAL logs| <------- | - Formal DR declaration  |                |
|  | - Scale K8s microservices|          | - Fetch S3 snapshots     |          | - Activate Secondary     |                |
|  | - Shift DNS traffic to B |          |   (Point-in-Time PITR)   |          |   Standby Region         |                |
|  +--------------------------+          +--------------------------+          +--------------------------+                |
|               |                                                                                                          |
|               v                                                                                                          |
|  +--------------------------+          +--------------------------+                                                      |
|  | [7] Validate & Smoke Test|          | [8] Resume Operations    |                                                      |
|  | - Verify ledger checksum | -------> | - Open traffic to public |                                                      |
|  | - Run synthetic API tests|          | - Post-mortem RCA        |                                                      |
|  | - Confirm zero data loss |          | - Regulatory reporting   |                                                      |
|  +--------------------------+          +--------------------------+                                                      |
|                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------+
```
*(Sơ đồ đồ họa chất lượng cao đã được xuất ra file: `Retail bank_recovery workflow.png` và nhúng trực tiếp vào tài liệu Word).*

---

## Task 7: Validate Checklist

| Validation Item | Yes/No | Verification Evidence |
| :--- | :---: | :--- |
| **Critical systems identified** | **Yes** | 7 core systems/data assets (Ledger, KYC, Loan DB, AML, Git, IAM, Logs) inventoried in Task 1. |
| **Backup frequency and retention are defined** | **Yes** | Frequency (WAL continuous, hourly, daily) and retention (up to 7 years) defined in Task 2. |
| **RTO and RPO documented** | **Yes** | RTO $\le 15\text{ mins}$ and RPO $\le 1\text{ min}$ established across all critical workloads. |
| **Backup strategy selected correctly** | **Yes** | Continuous PITR, streaming incremental, and differential methods mapped in Task 3. |
| **The DR plan includes failover steps** | **Yes** | 6-step operational failover procedure (Declare $\rightarrow$ Promote DB $\rightarrow$ Scale K8s $\rightarrow$ Switch DNS $\rightarrow$ Validate $\rightarrow$ Sign-off) defined in Task 4. |
| **Storage is encrypted and versioned** | **Yes** | AES-256 KMS encryption, TLS 1.3, S3 Object Lock, and Bucket Versioning detailed in Task 5. |
| **Recovery workflow included** | **Yes** | Visual 8-step workflow diagram created and embedded in Task 6. |
| **Plan supports DR drills** | **Yes** | Bi-annual unannounced failover drill schedule aligned with FFIEC and PCI-DSS requirements. |
