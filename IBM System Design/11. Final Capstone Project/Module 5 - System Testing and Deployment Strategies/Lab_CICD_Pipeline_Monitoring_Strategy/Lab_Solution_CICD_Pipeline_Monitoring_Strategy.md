# Lab: Create a CI/CD Pipeline and Monitoring Strategy - Solution

**Course:** IBM System Design - Capstone Project  
**Module:** Module 5 - System Testing and Deployment Strategies  
**Target System:** Retail Bank Digital Core Platform (Onboarding, Loan Engine, Fraud Detection, Transaction Core)  
**Author:** Parikshit Jain  

---

## Task 1: Create the CI/CD Pipeline

### 1. Enterprise CI/CD Pipeline Diagram

```
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                  RETAIL BANK DIGITAL CORE - REGULATED CI/CD PIPELINE                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                     |
|  [STAGE 1: Code Commit]                     [STAGE 2: Build & Unit Test]                 [STAGE 3: DevSecOps Gate]                                  |
|  +-----------------------+                  +-----------------------+                    +-----------------------+                                  |
|  | - Feature branch push |                  | - Multi-stage compile |                    | - SAST (SonarQube)    |                                  |
|  | - Git secret scanning |  ------------->  | - TDD Unit Tests      |  ----------------> | - SCA & Dependency    |                                  |
|  |   (Gitleaks/TruffleHog|                  | - Packaging (JAR/OCI) |                    |   Check (Snyk/Trivy)  |                                  |
|  +-----------------------+                  +-----------------------+                    | - Container scan      |                                  |
|     Role: Developer                            Role: Developer / DevOps                  +-----------------------+                                  |
|                                                                                             Role: DevSecOps Engineer                                |
|                                                                                                                                                     |
|                                                                                                    |                                                |
|                                                                                                    v                                                |
|                                                                                                                                                     |
|  [STAGE 6: Change Approval Gate]            [STAGE 5: Staging Deployment]                [STAGE 4: Automated Testing]                               |
|  +-----------------------------+            +---------------------------+                +--------------------------+                               |
|  | - Architecture Review       |            | - Deploy to Staging K8s   |                | - Microservice API Tests |                               |
|  | - QA Sign-off validation    | <--------- | - Synthetic Smoke Tests   | <------------- | - Integration (Kafka/DB) |                               |
|  | - Change Advisory Board CAB |            | - Security DAST scanning  |                | - Contract Tests (Pact)  |                               |
|  +-----------------------------+            +---------------------------+                +--------------------------+                               |
|     Role: Architect & Release Mgr              Role: DevOps Engineer                        Role: QA Engineer                                       |
|                                                                                                                                                     |
|        |                                                                                                                                            |
|        v                                                                                                                                            |
|                                                                                                                                                     |
|  [STAGE 7: Production Deployment]           [STAGE 8: Automated Rollback Strategy]       [STAGE 9: Audit & Compliance]                              |
|  +-------------------------------+          +------------------------------------+       +---------------------------+                              |
|  | - Canary (10% -> 50% -> 100%) |          | - Triggers: Error rate > 1%,       |       | - Tamper-proof logging    |                              |
|  |   or Blue-Green Traffic Swap  | -------> |   Latency spike, Health check fail | ----> | - FFIEC, PCI-DSS, SOC2    |                              |
|  | - KMS Secrets runtime inject  |          | - Auto revert traffic to Blue/Old  |       |   audit trail persistence |                              |
|  +-------------------------------+          +------------------------------------+       +---------------------------+                              |
|     Role: DevOps & Release Mgr                 Role: SRE / Automated Pipeline               Role: Compliance & SecOps                               |
|                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
```

### 2. CI/CD Stage Role Assignment Matrix

| CI/CD Stage | Responsible Role | Key Responsibilities & Controls |
| :--- | :--- | :--- |
| **Code Commit** | **Developer** | Pushes modular code, ensures no plain-text credentials via local pre-commit hooks (Gitleaks). |
| **Build & Unit Test** | **Developer / DevOps** | Compiles binaries, executes isolated TDD unit tests, packages OCI-compliant container images. |
| **DevSecOps Gate** | **DevSecOps Engineer** | Enforces static application security testing (SAST), Software Bill of Materials (SBOM), open-source license & container vulnerability scans. Blocks pipeline on Critical/High CVEs. |
| **Automated Testing** | **QA Engineer** | Executes end-to-end integration tests, REST API schema tests, Kafka event contract tests, and non-regression suites. |
| **Staging Deployment** | **DevOps** | Deploys release candidates to ephemeral Kubernetes staging clusters; runs synthetic smoke tests. |
| **Architecture & Approval Gate** | **Architect & Release Manager** | Reviews architectural compliance, confirms zero-defect QA sign-off, verifies change window, and signs off in ITSM (ServiceNow). |
| **Production Deployment** | **DevOps & Release Manager** | Executes automated Canary or Blue-Green release, binds secrets via HashiCorp Vault / Cloud KMS. |
| **Rollback & Health Verification** | **SRE / DevOps** | Monitors real-time Golden Signals during traffic ramp-up; triggers instant traffic re-route upon breach. |
| **Audit & Compliance Logging** | **Compliance Officer / SecOps** | Archives immutable deployment metadata, commit SHAs, scan approvals, and pipeline execution logs for regulatory compliance (PCI-DSS, FFIEC). |

---

## Task 2: Define Deployment Risk Strategy

Summary table of deployment risks, triggers, mitigation strategies, and automated rollback plans for high-availability banking services:

| Risk | Trigger | Mitigation Strategy | Rollback Plan |
| :--- | :--- | :--- | :--- |
| **Service Crash / Deployment Failure** | Container restart loops (`CrashLoopBackOff`), failed Kubernetes liveness/readiness probes within 60s of release. | Implement Canary release strategy (10% traffic canary pod slice); automated container health check gates before scaling. | Automated rollback via ArgoCD/Kubernetes: instantly re-route 100% ingress traffic back to previous stable ReplicaSet. |
| **API Contract Incompatibility / Breaking Changes** | Spike in `HTTP 400 Bad Request` or `HTTP 404 Not Found` (>2% of total traffic) between frontend and downstream core banking microservices. | Enforce consumer-driven contract testing (Pact) during CI; implement backward-compatible API versioning (e.g., `/v1` and `/v2` coexistence). | Instant Blue-Green router switch at API Gateway/Ingress level to the dormant Blue (previous version) target group within 5 seconds. |
| **Configuration or Secret Injection Error** | High rate of `HTTP 500 Internal Server Error`, authentication failures to PostgreSQL / Kafka, or missing DB credentials. | Strict separation of config and code (12-Factor App); dynamic runtime secrets injection using HashiCorp Vault with pre-deployment dry-run validation. | Redeploy previous known-good config map revision from GitOps repository; trigger immediate rolling pod restart. |
| **Database Migration Lock / Schema Incompatibility** | Database migration lock timeout, connection pool exhaustion, or DB query latency > 2,000ms. | Follow Expand-Contract (parallel-run) migration pattern: never drop or rename active columns in the same release; run non-blocking DDL. | Execute automated Flyway/Liquibase rollback script; re-point microservice database connection pool to the previous schema version. |

---

## Task 3: Create a System Monitoring Plan

### Step 1: Definition of Core Banking KPIs

1. **Latency (API Response Time):** Measures p95 and p99 response duration across critical banking APIs (e.g., balance check, fund transfers).
2. **Availability (%):** Percentage of total uptime and successful requests across all core digital banking endpoints (target: 99.99%).
3. **Transaction Throughput (TPS):** Volume of financial transactions processed successfully per second through the core ledger.
4. **Error Rate (%):** Percentage of failed transactions (HTTP 5xx server errors, unhandled exceptions, failed DB commits) relative to total volume.
5. **Fraud Rule Engine Execution Time:** Latency incurred by the real-time anti-fraud and risk assessment engine per transaction.
6. **Database Replication Lag:** Time delay in milliseconds between primary transactional PostgreSQL/Spanner node and read-replicas.

---

### Step 2: Alert Triggers and Thresholds

| KPI | Threshold | Alert Trigger | Severity | Notification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Latency (p99)** | p99 > 800ms for 3 consecutive minutes | API Gateway / Service Mesh p99 latency breaches 800ms sustained | **P2 - Major** | PagerDuty to On-call Backend SRE, Slack `#alerts-core-banking` |
| **Availability** | Availability < 99.90% over a 5-minute rolling window | Failed health checks or successful request ratio drops below 99.90% | **P1 - Critical** | PagerDuty voice call to Incident Commander & SRE Lead, SMS |
| **Error Rate** | 5xx error rate > 1.0% of total traffic over 2 minutes | Sustained spike in `HTTP 500/502/503` or unhandled transaction errors | **P1 - Critical** | PagerDuty immediate dispatch, Automated Incident Bridge opened |
| **Fraud Engine Time** | Execution time > 200ms per transaction | Fraud risk evaluation duration exceeds real-time checkout limit | **P2 - Major** | Slack alert to Fraud & Risk Engineering team, Jira auto-ticket |
| **Database Replication Lag**| Lag > 1,000ms (1 second) | Secondary replica lag exceeds acceptable sync threshold | **P3 - Moderate** | Email to Database Administrator (DBA), Slack `#db-monitoring` |

---

### Step 3: Hierarchical Escalation Path

| Level | Escalated To | Time to Respond | Operational Role & Actions |
| :--- | :--- | :---: | :--- |
| **Level 1 (L1)** | **Primary On-Call SRE / DevOps Engineer** | **5 minutes** | Acknowledges alert, reviews Grafana dashboards/logs, executes initial triage, performs canary rollback if post-deployment. |
| **Level 2 (L2)** | **Lead Backend Architect & Domain Service Tech Lead** | **15 minutes** | Deep-dive root-cause debugging, isolates failing microservice/database dependency, pushes hotfix or initiates Blue-Green traffic drain. |
| **Level 3 (L3)** | **Incident Commander, VP of Engineering, Chief Risk/Compliance Officer** | **30 minutes** | Coordinates multi-team response, manages regulatory disclosure if customer data/funds impacted, initiates formal business continuity plan (BCP). |

---

### Step 4: Post-Mortem Workflow

A structured 6-step incident analysis and resolution workflow:

1. **Incident Summary:** High-level executive overview stating date, severity (P1/P2), duration of downtime/degradation, business impact (affected customers, blocked transactions, estimated financial impact).
2. **Timeline Reconstruction:** Chronological, minute-by-minute breakdown from code deployment, alert trigger time, triage initiation, mitigation, to full service restoration.
3. **Root Cause Analysis (RCA):** Applying the "5 Whys" methodology to identify the fundamental systemic, architectural, or procedural failure rather than superficial symptoms.
4. **Fix Validation & Remediation:** Documenting the immediate hotfix and long-term fix implemented, including automated regression and load test verification.
5. **Prevention Action Items (CAPA):** Creating prioritized, assignable Jira tickets covering architectural hardening, pipeline security gate enhancement, and monitoring threshold adjustments.
6. **Regulatory & Compliance Reporting:** Preparing formal incident summaries required for regulatory compliance audits (FFIEC, Central Bank, PCI-DSS) within mandated reporting windows (e.g., 24-72 hours).

---

## Task 4: Validate the Checklist

| Validation Item | Yes/No | Verification Evidence |
| :--- | :---: | :--- |
| **Pipeline includes all CI/CD stages** | **Yes** | Covers Source, Build, DevSecOps, Automated Test, Staging, Approval Gate, Prod Deploy, Rollback, and Audit logging. |
| **Security gates included (SAST, container scan)** | **Yes** | DevSecOps gate features SAST (SonarQube), SCA dependency analysis, secret leak scans, and container image vulnerability scans (Trivy). |
| **Roles assigned for each stage** | **Yes** | Specific enterprise roles assigned: Developer, DevSecOps Engineer, QA, Architect, DevOps, Release Manager, and Compliance Officer. |
| **Rollback strategy documented** | **Yes** | Multi-faceted strategy with explicit triggers, Canary/Blue-Green traffic re-routing, and automated database schema rollback. |
| **KPIs have thresholds and alerts** | **Yes** | All 6 required banking KPIs (Latency, Availability, TPS, Error Rate, Fraud Engine Time, DB Lag) have quantifiable thresholds and severities. |
| **Escalation path defined** | **Yes** | Hierarchical 3-tier escalation (L1 SRE 5m -> L2 Tech Lead 15m -> L3 Incident Commander/Leadership 30m) documented. |
| **Monitoring covers compliance and uptime** | **Yes** | Adheres to 99.99% uptime SLA, FFIEC/PCI-DSS audit trail archiving, and mandatory regulatory incident reporting. |
