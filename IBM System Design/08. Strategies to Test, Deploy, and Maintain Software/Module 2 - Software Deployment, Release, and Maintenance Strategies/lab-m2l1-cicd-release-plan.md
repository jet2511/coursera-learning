# Lab: Release Plan with CI/CD Workflows

**Document Name:** `lab-m2l1-cicd-release-plan.md`  
**Role:** Systems Professional  
**Project:** Online Course Management System  
**Features in Release:** Course Bookmarking & Weekly Engagement Email Digest  
**CI/CD Stack:** Jenkins + GitHub Actions  

---

## 1. CI/CD Pipeline Stages (Plain Language)

| Pipeline Stage | Description (in plain language) | Who needs to be informed? |
| :--- | :--- | :--- |
| **Code commit** | Developers push new code to GitHub repository for the Bookmarking and Weekly Digest features. | Systems professionals track features and commits; Dev Lead. |
| **Build** | Code is compiled and dependencies are checked; container images/artifacts are packaged automatically. | DevOps and QA teams. |
| **Automated unit test** | Automated tests check if core functions and code logic behave as expected without regressions. | QA, systems professionals for tracking pass/fail rates. |
| **Staging deploy** | Application is automatically deployed to a staging environment mimicking production for preview and integration testing. | QA, Product Owner, systems professional. |
| **UAT review** | Key business workflows (bookmarking flows, email digest triggering) are manually reviewed and verified against user expectations before production push. | **Systems professional coordinates UAT**, Product Owner, QA Lead. |
| **Production deploy** | CI/CD pipeline deploys the validated release package to the live production environment. | All teams alerted via Slack/Email/Teams. |

---

## 2. Systems Professional Checkpoints

As the systems professional, I review staging deploy logs to check for failed API responses and integration issues tied to business workflows (such as bookmark persistence and queue handling for the weekly digest). I also prepare a summary of what's new for the product owner during UAT and coordinate their sign-off. After UAT passes, I confirm that release notes are finalized and shared, alert thresholds are aligned with DevOps, and metrics dashboards are in place for monitoring production success and adoption.

---

## 3. CI/CD Risks and Mitigation Strategies

| Risk | Why it matters | Mitigation (Systems Professional role) |
| :--- | :--- | :--- |
| **Feature deploys before UAT approval** | Users may see unfinished or broken features (e.g., faulty email digest sent to live users). | Configure a **Manual Approval Gate** in the pipeline: block the production deploy step unless the UAT approval task is officially signed off. |
| **Alert fatigue from test pipeline failures** | Teams may ignore critical test failures if bombarded by frequent non-critical or flaky test notifications. | Define clear alert thresholds with DevOps (e.g., fail notification only after 3 retries, separate critical errors from warnings). |
| **Metrics not tracked in production** | No way to assess whether the new features are working properly or driving user engagement. | Include a mandatory systems professional review of KPI dashboards and telemetry tracking before approving release to production. |

---

## 4. Systems Professional-Owned Pre-Release Checklist

Final checklist verification prior to triggering the automated production deployment:

- [ ] **Staging pass:** Staging deployment successful with all automated unit and integration tests passing, plus QA spot checks verified.
- [ ] **Product Owner UAT sign-off:** Formal sign-off and approval obtained from the Product Owner.
- [ ] **Release summary & documentation:** Release summary/notes completed and shared with support, marketing, and cross-functional teams.
- [ ] **Alert thresholds aligned:** Error thresholds and alerting channels verified with DevOps.
- [ ] **Monitoring dashboard updated:** Production monitoring dashboard and business KPI metrics (bookmark counts, email digest open rates) updated and active.
