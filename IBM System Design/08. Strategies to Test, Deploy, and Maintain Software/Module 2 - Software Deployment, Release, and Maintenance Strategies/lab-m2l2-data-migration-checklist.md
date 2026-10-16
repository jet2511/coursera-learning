# Data Migration Readiness Checklist

**Document Name:** `lab-m2l2-data-migration-checklist.md`  
**Role:** Systems Professional / Lead Systems Analyst  
**Project:** Legacy On-Premises CRM to Modern Cloud CRM Migration  
**Target Audience / Executors:** Systems Professionals, Data Analysts, Developers, DevOps, QA, and Business Stakeholders  

---

## 📌 Document Introduction
This Data Migration Readiness Checklist serves as a governance framework and operational gate to guide the safe transition of customer contact records, communication history, and subscription data from our legacy on-premises CRM to the new cloud-based CRM. The checklist ensures all prerequisites—including data cleansing, field mapping, environment preparation, dry-run testing, and rollback readiness—are rigorously verified and approved by accountable owners before executing the production migration.

---

## 📋 Data Migration Readiness Checklist Table

| Item # | Section | Description | Owner | Complete (Y/N) |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **Planning** | Conduct legacy data audit & inventory; identify active vs. obsolete/archived records to avoid migrating stale data. | Systems Analyst | [ ] |
| **2** | **Planning** | Define migration scope, business objectives, and measurable success criteria (e.g., 100% active customer balance match). | Business Lead | [ ] |
| **3** | **Planning** | Establish and document a comprehensive Rollback Strategy & Data Recovery Procedure in case of critical cutover failure. | Systems Architect | [ ] |
| **4** | **Planning** | Provision and configure dedicated Staging/Dry-run environment mirroring production schemas and access controls. | DevOps Engineer | [ ] |
| **5** | **Mapping** | Create and document the comprehensive Field Mapping Sheet (source fields, target fields, and data types). | Systems Analyst | [ ] |
| **6** | **Mapping** | Define transformation rules for complex fields (e.g., currency cent conversion, name concatenations, date format standardization `YYYY-MM-DD`). | Developer | [ ] |
| **7** | **Mapping** | Map lookup codes and categorical status flags (e.g., `Y/N` to `ACTIVE/INACTIVE`, legacy subscription tier mapping). | Systems Analyst | [ ] |
| **8** | **Validation** | Execute end-to-end Migration Dry Run on staging replica using real sanitized production data copy. | DevOps / Developer | [ ] |
| **9** | **Validation** | Perform Record Count Comparison between legacy CRM and new Cloud CRM to detect missing or duplicate entries. | QA Engineer | [ ] |
| **10** | **Validation** | Conduct Sample Record Spot-Checks on representative profiles (random & high-value VIP accounts) across all critical fields. | QA / Business Analyst | [ ] |
| **11** | **Validation** | Verify business rule compliance & strict field validations (e.g., mandatory email formats, non-negative subscription balances). | QA Engineer | [ ] |
| **12** | **Validation** | Complete post-migration verification report (Validation Summary) and compile audit artifacts. | Systems Professional | [ ] |

---

## ✍️ Stakeholder Sign-Off & Approval

By signing below, each stakeholder confirms that all readiness criteria within their domain have been satisfied and that the system and data are verified ready for live production migration cutover:

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Lead Systems Analyst** | John Doe | _________________________ | ___/___/2026 |
| **Systems Architect** | Sarah Jenkins | _________________________ | ___/___/2026 |
| **Lead Developer** | Alex Chen | _________________________ | ___/___/2026 |
| **DevOps / Infrastructure Lead** | David Kumar | _________________________ | ___/___/2026 |
| **QA Lead** | Riya Singh | _________________________ | ___/___/2026 |
| **Business Stakeholder / CRM Owner** | Emily Watson | _________________________ | ___/___/2026 |
