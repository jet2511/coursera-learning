# -*- coding: utf-8 -*-
import docx
import os
import copy

dir_path = r'd:\Ent\Learning\Cousera\IBM System Design\08. Strategies to Test, Deploy, and Maintain Software\Module 4 - Final Project, Final Exam, and Course Wrap-Up'
src1 = os.path.join(dir_path, 'NexaCare-Testing-Release-Planning-Template.docx')
out1 = os.path.join(dir_path, 'NexaCare-Testing-Release-Planning-Completed-v2.docx')

doc = docx.Document(src1)

# 1. Update metadata
for p in doc.paragraphs:
    if '[Insert your full name]' in p.text:
        p.text = p.text.replace('[Insert your full name]', 'Systems Professional (NexaCare Solutions)')
    if '[Insert date]' in p.text:
        p.text = p.text.replace('[Insert date]', 'October 19, 2026')
    if '[Describe your general approach to testing.]' in p.text:
        p.text = (
            "Our test strategy adopts a comprehensive, risk-based, and compliance-first methodology tailored specifically to NexaCare v3.0. "
            "Following a past data loss incident in another product line, leadership mandates zero-data-loss and rigorous regression protection. "
            "Testing is structured across 4 distinct operational tiers:\n"
            "1. Component & Unit Testing: Input normalization, slot state machines, deterministic phone number parsing (E.164).\n"
            "2. Multi-System Integration Testing: External contracts with the newly integrated third-party SMS gateway, bi-directional Google/Outlook Calendar OAuth webhooks, and legacy clinic PMS REST APIs.\n"
            "3. Concurrency & Performance Testing: Simulating 500 baseline up to 2,500 concurrent virtual users during peak Monday morning surges (3-5x normal traffic) to prevent deadlocks and race conditions.\n"
            "4. User Acceptance Testing (UAT) & Pilot Validation: Staged rollout starting with 20 pre-selected pilot clinics of diverse technical maturity (basic standalone web portal vs. deep EHR/PMS API integrations) to validate real operational workflows before full cutover to 300+ clinics."
        )
    if '[List key features and components that require high-priority testing.]' in p.text:
        p.text = (
            "- P0 (Critical/Blocker): Data migration schema validation (1.2M records), ACID booking transactions, real-time doctor availability concurrency locks (double-booking prevention), HIPAA PHI encryption at rest/in transit, and clinic PMS API backward compatibility.\n"
            "- P1 (High): Automated SMS reminder engine (T-24h/T-1h dispatch via new third-party gateway), bi-directional Google/Outlook Calendar synchronization, rate limiting & retry queues.\n"
            "- P2 (Medium): Redesigned responsive UI across mobile/desktop, WCAG 2.1 AA screen reader & color contrast compliance, pilot clinic telemetry tracking.\n"
            "- P3 (Low): Micro-animations and minor static text updates."
        )
    if '[Summarize your testing goals: e.g., system stability, user experience, compliance.]' in p.text:
        p.text = (
            "1. Data Integrity & HIPAA Compliance: Ensure zero data corruption across 1.2M+ patient records with AES-256 rest encryption and TLS 1.3 transit encryption.\n"
            "2. High Concurrency & Scalability: Guarantee sub-3-second booking completion under 2,500 concurrent sessions during peak Monday 8-10 AM windows.\n"
            "3. Interoperability & Reliability: Validate error-free integration with external SMS gateway, OAuth calendar providers, and PMS APIs with automated circuit breakers.\n"
            "4. Usability & Accessibility: Meet WCAG 2.1 AA standards for seamless clinic staff and patient booking workflows across desktop, tablet, and mobile browsers."
        )
    if '[List any tools, automation frameworks, or environments used.]' in p.text:
        p.text = (
            "- Functional & Regression Automation: Cypress, Playwright, Jest, JUnit 5, Mockito.\n"
            "- API & Integration Testing: Postman, Newman, REST-assured, WireMock (for SMS & Calendar OAuth mocking).\n"
            "- Performance & Load Testing: Apache JMeter, k6 (simulating 500 to 2,500 concurrent virtual users).\n"
            "- Security & Static Analysis: OWASP ZAP, SonarQube, Snyk (HIPAA & SAST/DAST scanning).\n"
            "- Test Environments: Staging / Pre-Production mirror environment populated with anonymized, HIPAA-compliant dataset."
        )

# Populate Table 0: Types of Testing
t0 = doc.tables[0]
test_types_data = [
    ("Unit & Component Testing", "Validates isolated business logic, input sanitization, phone number formatting (E.164), and appointment slot state machines before integration."),
    ("Integration Testing", "Verifies contracts with external third-party SMS provider, Google/Outlook Calendar OAuth 2.0 endpoints, and clinic PMS REST APIs."),
    ("System & Regression Testing", "Ensures end-to-end booking flows operate flawlessly and verifies that legacy functionality across 300 clinics remains intact."),
    ("Security & Compliance Testing", "Audits HIPAA PHI handling, TLS 1.3 transit encryption, AES-256 rest encryption, and role-based access control (RBAC)."),
    ("Performance & Stress Testing", "Simulates Monday morning surge (1,500-2,500 concurrent users) to prove sub-3s response time and zero deadlocks."),
    ("User Acceptance Testing (UAT)", "Conducted with 20 pre-selected pilot clinics with varying technical maturity to validate operational clinic workflows.")
]
while len(t0.rows) > 1:
    t0._tbl.remove(t0.rows[-1]._tr)
for row in test_types_data:
    r = t0.add_row()
    r.cells[0].text = row[0]
    r.cells[1].text = row[1]

# Populate Table 1: Traceability Matrix (Expanded with Pilot Clinic & Edge Condition Coverage)
t1 = doc.tables[1]
matrix_data = [
    ("REQ-01", "Automated SMS reminders dispatched 24h & 1h prior to appointment via 3rd party", "TC-SMS-01, TC-SMS-02", "Covered (Standard & Edge)", "P1 - High"),
    ("REQ-01-A", "SMS opt-out (STOP) compliance handling under TCPA/HIPAA regulations", "TC-SMS-03", "Covered (Compliance)", "P0 - Critical"),
    ("REQ-01-B", "SMS delivery retry on carrier throttling or rate-limiting (429 Too Many Requests)", "TC-SMS-04 (Edge)", "Covered (Edge)", "P1 - High"),
    ("REQ-02", "Real-time doctor availability broadcast across active clinic browser sessions", "TC-AVAIL-01", "Covered (Standard)", "P0 - Critical"),
    ("REQ-02-A", "Concurrent appointment booking race condition & double-booking prevention", "TC-AVAIL-02 (Edge)", "Covered (Edge)", "P0 - Critical"),
    ("REQ-02-B", "Doctor availability update under spotty clinic Wi-Fi & WebSocket disconnect", "TC-AVAIL-03 (Edge)", "Covered (Pilot Clinic & Edge)", "P1 - High"),
    ("REQ-03", "Bi-directional Google Calendar and Microsoft Outlook event synchronization", "TC-CAL-01, TC-CAL-02", "Covered (Standard)", "P1 - High"),
    ("REQ-03-A", "Calendar sync handling when patient revokes OAuth permission or token expires", "TC-CAL-03 (Edge)", "Covered (Edge)", "P1 - High"),
    ("REQ-03-B", "Calendar event synchronization across mismatched clinic and patient timezones", "TC-CAL-04 (Edge)", "Covered (Edge)", "P1 - High"),
    ("REQ-04", "Redesigned UI responsiveness across Mobile (375px), Tablet, and Desktop (1440px)", "TC-UI-01, TC-UI-02", "Covered (Mobile/Desktop)", "P2 - Medium"),
    ("REQ-04-A", "Redesigned UI WCAG 2.1 AA accessibility (screen reader & keyboard tab navigation)", "TC-UI-03", "Covered (Accessibility)", "P2 - Medium"),
    ("REQ-05", "Backward compatibility for third-party clinic PMS REST API integrations", "TC-API-01, TC-API-02", "Covered (API/UI & Pilot)", "P0 - Critical"),
    ("REQ-05-A", "Pilot clinic validation: Hybrid workflow (Clinic PMS API write + Web Portal view)", "TC-PILOT-01", "Covered (Pilot Clinic)", "P0 - Critical"),
    ("REQ-06", "Data migration schema transformation & record reconciliation (1.2M records)", "TC-MIG-01, TC-MIG-02", "Covered (Data Integrity)", "P0 - Critical"),
    ("REQ-07", "Monday morning peak load concurrency handling (2,500 concurrent users, 3-5x normal)", "TC-PERF-01", "Covered (Performance)", "P0 - Critical")
]
while len(t1.rows) > 1:
    t1._tbl.remove(t1.rows[-1]._tr)
for row in matrix_data:
    r = t1.add_row()
    for i in range(5):
        r.cells[i].text = row[i]

# Modify Annotated Test Plans Section to include comprehensive test cases for ALL 4 features
# Locate paragraphs in Annotated test plans
p_feature = None
p_obj = None
p_pre = None
p_repeat = None

for p in doc.paragraphs:
    if 'Feature: ' in p.text or 'Feature: [' in p.text:
        p_feature = p
    if 'Test objective:' in p.text or 'Test Objective:' in p.text:
        p_obj = p
    if 'Preconditions:' in p.text:
        p_pre = p
    if '(Repeat this section' in p.text:
        p_repeat = p

# Set Feature 1 details
p_feature.text = "Feature 1: Automated SMS Reminder Engine (Third-Party Gateway Integration)"
p_obj.text = (
    "Test Objective: Validate timely, compliant, and reliable dispatch of automated SMS reminders at T-24h "
    "and T-1h intervals via the newly integrated third-party SMS provider, with resilient error, throttling, and opt-out handling."
)
p_pre.text = (
    "Preconditions: Patient account configured with valid mobile phone number; appointment scheduled >24 hours ahead; "
    "Third-party SMS sandbox and webhook endpoints active; HIPAA consent flag set to OPTED_IN."
)

# Table 2: Steps for Feature 1 (SMS)
t2 = doc.tables[2]
test_steps_sms = [
    ("TC-SMS-01.1", "Trigger automated cron scheduler to query appointments due for T-24h and T-1h reminder notifications.", 
     "Query retrieves eligible appointments without database table locks; dispatches queue message.", 
     "Edge Case: Timezone calculation discrepancies between clinic local time (e.g. EST) and UTC database timestamps."),
    ("TC-SMS-01.2", "Generate SMS message payload without diagnostic or physician specialty PHI (HIPAA Minimum Necessary Rule).", 
     "Payload contains only clinic name, appointment date/time, and opt-out instruction (e.g. 'Reply STOP to cancel').", 
     "Risk: Regulatory HIPAA violation and legal penalty if medical specialty or diagnosis is transmitted in plain text SMS."),
    ("TC-SMS-01.3", "Dispatch payload via REST API to third-party SMS gateway with mock carrier network.", 
     "HTTP 200 OK received; message ID stored; status updated to SENT within <= 2 minutes of scheduled dispatch.", 
     "Risk: Third-party API rate limiting (429 Too Many Requests). Must implement token-bucket throttling and exponential backoff."),
    ("TC-SMS-01.4", "Simulate incoming SMS webhook with 'STOP' response from patient (TCPA Opt-Out).", 
     "Database immediately updates patient preference to OPTED_OUT; audit log recorded; zero future SMS sent.", 
     "Compliance: Mandatory TCPA mandate. Immediate suppression of all automated messaging across the platform.")
]
while len(t2.rows) > 1:
    t2._tbl.remove(t2.rows[-1]._tr)
for row in test_steps_sms:
    r = t2.add_row()
    for i in range(4):
        r.cells[i].text = row[i]

# In place of p_repeat, let's insert Feature 2, Feature 3, Feature 4, and Feature 5!
p_repeat.text = "" # Clear placeholder

def add_feature_test_plan(feature_title, objective, preconditions, steps_data):
    doc.add_paragraph().text = ""
    h = doc.add_heading(feature_title, level=2)
    p1 = doc.add_paragraph()
    p1.add_run("Test Objective: ").bold = True
    p1.add_run(objective)
    p2 = doc.add_paragraph()
    p2.add_run("Preconditions: ").bold = True
    p2.add_run(preconditions)
    
    t = doc.add_table(rows=1, cols=4)
    t.style = doc.tables[2].style
    hdr_cells = t.rows[0].cells
    hdr_cells[0].text = "Step / TC ID"
    hdr_cells[1].text = "Test Action"
    hdr_cells[2].text = "Expected Result"
    hdr_cells[3].text = "Risks / Edge Cases / Notes"
    
    for row in steps_data:
        r = t.add_row()
        for i in range(4):
            r.cells[i].text = row[i]

# Feature 2: Real-Time Doctor Availability & Concurrency Control
f2_steps = [
    ("TC-AVAIL-01.1", "Doctor alters schedule slot (opens/blocks slot S1) in Clinic Web Portal.", 
     "WebSocket server broadcasts availability delta payload to all connected clients; slot color changes within <= 5s.", 
     "Risk: High broadcast fanout overhead if hundreds of patients are connected simultaneously."),
    ("TC-AVAIL-02.1", "Simulate 2 patients (User A and User B) simultaneously clicking 'Confirm Booking' on identical slot S1 at t=0ms (Race Condition).", 
     "Database transactional lock (pessimistic lock) grants commit to User A; User B receives HTTP 409 Conflict with clear modal notice. Zero double-booking.", 
     "Risk: Ghost bookings or double allocations under high Monday morning concurrency. Requires strict row-level isolation."),
    ("TC-AVAIL-03.1", "Patient browser experiences spotty clinic Wi-Fi (WebSocket drops); patient attempts to book an expired slot.", 
     "Client automatically detects socket disconnect, fails pre-booking validation, and forces background availability refresh.", 
     "Edge Case: Pilot clinics with poor network infrastructure seeing stale availability data on desktop screens.")
]
add_feature_test_plan(
    "Feature 2: Real-Time Doctor Availability & Concurrency Control",
    "Verify instant multi-session availability updates, accurate slot locking, and zero double-bookings under high concurrency and network drops.",
    "Doctor D schedule active in Clinic Portal; 2 authenticated patient accounts active on web portal; WebSocket gateway online.",
    f2_steps
)

# Feature 3: Bi-Directional Calendar Integration (Google Calendar & Outlook)
f3_steps = [
    ("TC-CAL-01.1", "Patient authenticates Google/Outlook account via OAuth 2.0 and books an appointment in NexaCare.", 
     "Appointment event created in external calendar within <= 15s with clinic address, date, time, and clinic name.", 
     "Risk: OAuth token scope leakage or excessive permissions. Must strictly request calendar.events scope."),
    ("TC-CAL-02.1", "Patient reschedules or cancels appointment inside NexaCare web platform.", 
     "Webhook triggers external calendar update; existing calendar entry is modified or deleted cleanly without orphan events.", 
     "Risk: Desynchronization if external API is temporarily down; requires persistent retry queue with exponential backoff."),
    ("TC-CAL-03.1", "Patient revokes NexaCare access token from Google Account security settings prior to sync update.", 
     "NexaCare receives HTTP 401/403, updates sync_status to 'ACTION_REQUIRED', and alerts user via UI banner without failing booking.", 
     "Edge Case: Expired/revoked OAuth refresh tokens causing silent booking errors in clinic schedules."),
    ("TC-CAL-04.1", "Clinic in EST (UTC-5) schedules appointment for patient traveling in PST (UTC-8).", 
     "Event stored internally in UTC ISO-8601; external invitation renders at exact matching local time for both parties.", 
     "Edge Case: Daylight saving transitions or cross-timezone appointment misalignments leading to missed doctor visits.")
]
add_feature_test_plan(
    "Feature 3: Bi-Directional Calendar Integration (Google Calendar & Microsoft Outlook)",
    "Validate seamless event creation, updates, and cancellations across Google Calendar and Microsoft Outlook, including OAuth lifecycle and timezone parity.",
    "User linked active Google/Outlook account; OAuth refresh token encrypted in database; mock external calendar endpoints ready.",
    f3_steps
)

# Feature 4: Redesigned Accessible & Responsive User Interface
f4_steps = [
    ("TC-UI-01.1", "Execute full booking journey on viewport width 375px (iPhone/Android mobile screen).", 
     "Responsive layout renders without horizontal scroll; touch targets >= 48x48px; booking completed in <= 3 steps.", 
     "Risk: Overflow of schedule slot tables on smaller smartphone displays causing booking drop-offs."),
    ("TC-UI-02.1", "Execute booking journey on viewport width 1440px (Desktop clinic reception workstation).", 
     "Full calendar grid renders clearly; multi-provider view displays without layout overlap or rendering artifacts.", 
     "Risk: Desktop performance stuttering when rendering dozens of provider schedules simultaneously."),
    ("TC-UI-03.1", "Navigate entire booking workflow using keyboard-only navigation (Tab, Enter, Space, Arrow keys).", 
     "Visible focus indicators present on 100% interactive elements; modal trap focus works correctly; zero keyboard traps.", 
     "Compliance: WCAG 2.1 AA requirement. Failure excludes users with motor impairments."),
    ("TC-UI-04.1", "Audit interface with NVDA and JAWS screen readers across appointment selection and confirmation dialogs.", 
     "All interactive controls have descriptive aria-labels; dynamic availability updates announced via aria-live regions.", 
     "Compliance: Accessibility compliance mandatory for healthcare platforms serving diverse demographics.")
]
add_feature_test_plan(
    "Feature 4: Redesigned User Interface (Responsive Design & WCAG 2.1 AA Accessibility)",
    "Ensure complete responsive usability across mobile, tablet, and desktop devices, alongside strict WCAG 2.1 AA accessibility compliance.",
    "Staging frontend deployed with redesigned CSS/JS design system; screen reader tools (NVDA/JAWS) and mobile emulators configured.",
    f4_steps
)

# Feature 5: Clinic PMS/API Integration & Pilot Clinic Hybrid Workflows
f5_steps = [
    ("TC-API-01.1", "Clinic PMS sends REST API request to POST /api/v2/appointments using legacy payload format.", 
     "API Gateway accepts request; backward-compatibility adapter maps legacy fields to v3.0 schema; returns HTTP 201 Created.", 
     "Risk: Breaking external clinic EHR/PMS integrations that rely on v2 JSON schema contracts."),
    ("TC-API-02.1", "Clinic PMS queries GET /api/v2/doctors/{id}/availability for real-time schedule.", 
     "API responds within <= 250ms with standardized ISO-8601 availability payload matching exact legacy format.", 
     "Risk: API latency causing timeouts in third-party clinic electronic health record software."),
    ("TC-PILOT-01.1", "Pilot Clinic #4 creates appointment via EHR API integration; receptionist verifies live update on NexaCare Web Portal.", 
     "Appointment immediately reflects on Web UI in real-time (< 3s); SMS reminder scheduled; calendar invite dispatched.", 
     "Pilot Focus: Validates hybrid clinic environment where staff use both local PMS software and web platform simultaneously.")
]
add_feature_test_plan(
    "Feature 5: Clinic PMS/API Integration & Pilot Clinic Hybrid Workflows",
    "Verify backward compatibility for external clinic patient management systems (PMS) and validate hybrid API/UI workflows across the 20 pilot clinics.",
    "API Gateway running with v2 backward-compatibility middleware; test clinic registered in Pilot program with active API keys.",
    f5_steps
)

# Move Deployment Checklist, Rollback Strategy, Migration Plan, Post-deployment monitoring into correct order
# Let's verify Table 3-9 are untouched and clean
# Table 3: Pre-deployment tasks
t3 = doc.tables[3]
pre_deploy_data = [
    ("Final code freeze across all v3.0 release branches & artifact tagging", "DevOps Lead", "T-48h", "Signed Docker images published to secure registry"),
    ("Broadcast deployment advisory to all 300+ clinics detailing 6h window", "Support Lead", "T-24h", "Email and in-app banner notifications sent"),
    ("Execute Staging environment migration rehearsal dry run (1.2M records)", "DBA / QA Lead", "T-12h", "100% row count and checksum match achieved"),
    ("Verify production backup storage capacity and failover availability", "DevOps / SRE", "T-2h", "Secondary S3 replication and snapshot scripts verified")
]
while len(t3.rows) > 1:
    t3._tbl.remove(t3.rows[-1]._tr)
for row in pre_deploy_data:
    r = t3.add_row()
    for i in range(4):
        r.cells[i].text = row[i]

# Table 4: Deployment window tasks (Saturday 12:00 AM - 6:00 AM EST)
t4 = doc.tables[4]
window_deploy_data = [
    ("Enable global maintenance mode and sever incoming web traffic", "DevOps Lead", "12:00 AM - 12:15 AM", "Load balancer routing updated to static maintenance splash"),
    ("Execute cold full snapshot of 1.2M patient production database", "Lead DBA", "12:15 AM - 01:00 AM", "Gate 1: Verified snapshot taken and cryptographically hashed"),
    ("Execute DDL schema transformations & batch data migration", "Lead DBA", "01:00 AM - 02:30 AM", "Batch chunks of 10,000 rows; zero unhandled exceptions"),
    ("Run post-migration reconciliation script (100% row match)", "Lead DBA / QA", "02:30 AM - 03:00 AM", "Gate 2: Target row count = 1,200,000; checksum verified"),
    ("Deploy v3.0 backend services & frontend static assets", "DevOps Lead", "03:00 AM - 03:30 AM", "Kubernetes pods reach READY status; secrets mounted"),
    ("Execute production smoke test suite & live SMS/Calendar verification", "QA Lead", "03:30 AM - 04:30 AM", "100% core test cases pass; sub-3s booking confirmed"),
    ("Formal Go/No-Go Decision Meeting with all Leads", "Release Manager", "04:30 AM - 04:45 AM", "Gate 3: Hard deadline. Decision to cutover or rollback"),
    ("Cutover access for 20 Pilot Clinics; monitor initial telemetry", "DevOps / Support", "04:45 AM - 05:30 AM", "Pilot clinics operational; zero P0/P1 tickets logged"),
    ("Full public cutover for remaining 280+ clinics; lift maintenance", "Release Manager", "05:30 AM - 06:00 AM", "Platform fully operational across North America")
]
while len(t4.rows) > 1:
    t4._tbl.remove(t4.rows[-1]._tr)
for row in window_deploy_data:
    r = t4.add_row()
    for i in range(4):
        r.cells[i].text = row[i]

# Table 5: Post-deployment tasks
t5 = doc.tables[5]
post_deploy_data = [
    ("Establish 48-Hour Virtual War Room for Hypercare monitoring", "SRE / DevOps", "06:00 AM onwards", "Cross-functional team on active bridge"),
    ("Monitor real-time Golden Signals (Latency, Traffic, Errors, Saturation)", "DevOps / SRE", "Continuous", "Datadog / Prometheus dashboards streaming live metrics"),
    ("Triage pilot clinic feedback and direct support escalation queue", "Support Lead", "Hourly checks", "Priority SLA < 15 minutes for 20 pilot clinics"),
    ("Deliver daily executive operational health summaries to leadership", "Systems Lead", "Daily 05:00 PM", "Comprehensive telemetry, error counts, and ticket analysis")
]
while len(t5.rows) > 1:
    t5._tbl.remove(t5.rows[-1]._tr)
for row in post_deploy_data:
    r = t5.add_row()
    for i in range(4):
        r.cells[i].text = row[i]

for p in doc.paragraphs:
    if '[Define technical, operational, and business conditions that' in p.text:
        p.text = (
            "1. Technical Go Conditions: 100% schema migration match (1.2M records); zero P0/P1 defects in smoke tests; "
            "API P95 latency < 500ms; external SMS/Calendar webhooks returning HTTP 200.\n"
            "2. Operational Go Conditions: DevOps, DBA, and QA leads provide unanimous written sign-off by 04:30 AM EST.\n"
            "3. Hard No-Go Triggers: Any data loss/corruption; smoke test failure rate > 5%; unresolvable DB deadlocks; "
            "or clock reaching 04:30 AM EST without QA sign-off (mandating immediate rollback to preserve 6:00 AM opening)."
        )
    if '[State clear conditions such as performance failure, critica' in p.text:
        p.text = (
            "1. Data corruption, truncation, or reconciliation mismatch > 0.01% of patient records.\n"
            "2. Migration or critical smoke test incomplete by 04:30 AM EST hard deadline.\n"
            "3. Core appointment booking engine failure, persistent double-booking, or security vulnerability.\n"
            "4. Database connection pool exhaustion (>95%) or sustained 5xx error rate > 2%."
        )
    if '[Define internal and external communication steps and respon' in p.text:
        p.text = (
            "- Internal Escalation: Release Manager notifies Executive Team and incident response bridge via Slack/Paging within 5 minutes.\n"
            "- External Communication: Support Lead updates status.nexacare.com and dispatches priority advisory to all 300+ clinics: "
            "'The scheduled platform update has been postponed for further optimization. Stable platform v2.x remains fully available.'"
        )
    if '[Give a range or best-case / worst-case timing.]' in p.text:
        p.text = (
            "Total Rollback Duration: 60 - 90 minutes maximum. Executing by 04:30 AM guarantees full v2.x system restoration "
            "and verification before the 06:00 AM EST clinic opening deadline."
        )

# Table 6: Rollback Procedures Table
t6 = doc.tables[6]
rollback_steps_data = [
    ("Step 1", "Enforce global maintenance mode and isolate database connections", "DevOps Lead"),
    ("Step 2", "Scale down all v3.0 application containers and background workers to 0", "DevOps Lead"),
    ("Step 3", "Drop working database and restore from 12:15 AM verified pre-deployment snapshot", "Lead DBA"),
    ("Step 4", "Execute verification script confirming 1,200,000 legacy records intact", "Lead DBA / QA"),
    ("Step 5", "Redeploy stable v2.x container images and revert DNS/ingress routing rules", "DevOps Lead"),
    ("Step 6", "Execute v2.x sanity smoke test suite and reopen platform to all clinics", "QA Lead / Release Manager")
]
while len(t6.rows) > 1:
    t6._tbl.remove(t6.rows[-1]._tr)
for row in rollback_steps_data:
    r = t6.add_row()
    for i in range(3):
        r.cells[i].text = row[i]

# Data Migration Details
for p in doc.paragraphs:
    if 'Source system: ' in p.text:
        p.text = "Source system: NexaCare Legacy Production Database (PostgreSQL 12 - Monolithic v2 Schema)"
    if 'Destination system: ' in p.text:
        p.text = "Destination system: NexaCare v3.0 Partitioned Database (PostgreSQL 15 - Normalized Microservice Schema)"
    if '[Indicate the number of records, file sizes, batch structure' in p.text:
        p.text = (
            "Total Record Volume: 1,200,000 Patient Records, 8,540,000 Historical Appointments, 312 Clinic Profiles.\n"
            "Batch Strategy: Script executes in controlled transactional chunks of 10,000 records with progress tracking, "
            "automated commit checkpoints, and dedicated exception routing to avoid database table locking."
        )

# Table 7: Data Field Mapping
t7 = doc.tables[7]
field_mapping_data = [
    ("patient_id (INT)", "patient_uuid (UUID)", "Deterministic UUIDv5 generation based on legacy ID namespace."),
    ("phone_home, phone_mobile", "mobile_number_e164 (VARCHAR)", "Normalize and convert phone numbers to ITU E.164 standard (+1XXXXXXXXXX)."),
    ("sms_consent (0/1/NULL)", "sms_opt_in_status (ENUM)", "Map 1 -> OPTED_IN, 0 -> OPTED_OUT, NULL -> PENDING_CONFIRMATION."),
    ("first_name, last_name", "legal_name_encrypted (BYTEA)", "Sanitize and encrypt using AES-256-GCM envelope encryption (HIPAA PHI)."),
    ("N/A (New Feature)", "calendar_sync_provider", "Initialize as 'NONE'; updated dynamically upon Google/Outlook OAuth link."),
    ("N/A (New Feature)", "availability_version (INT)", "Initialize default to 1 for optimistic concurrency locking control.")
]
while len(t7.rows) > 1:
    t7._tbl.remove(t7.rows[-1]._tr)
for row in field_mapping_data:
    r = t7.add_row()
    for i in range(3):
        r.cells[i].text = row[i]

# Table 8: Post-deployment Monitoring Metrics
t8 = doc.tables[8]
metrics_data = [
    ("Platform Uptime / Availability", ">= 99.9% uptime (<= 43.8 min/month)", "Synthetic Probes (Pingdom / Better Uptime)"),
    ("HTTP 5xx Server Error Rate", "< 0.1% of total requests (Alert if > 0.5%)", "Datadog APM / Application Load Balancer"),
    ("Booking Transaction Latency (P95)", "< 500 ms (Alert if > 1,500 ms)", "Datadog APM Distributed Tracing"),
    ("SMS Reminder Delivery Latency", "< 2 minutes from schedule (Alert if > 5 min)", "Third-Party Webhook Delivery Logs"),
    ("SMS Delivery Failure Rate", "< 1.0% failure (Alert if > 3.0%)", "Logstash / Elasticsearch Aggregation"),
    ("Doctor Availability Update Sync", "< 5.0 seconds cross-session propagation", "WebSocket Gateway Telemetry / Prometheus"),
    ("Calendar Sync Authorization Errors", "< 0.5% failure rate (Alert if > 2.0%)", "Application Exception Logs (Sentry / ELK)")
]
while len(t8.rows) > 1:
    t8._tbl.remove(t8.rows[-1]._tr)
for row in metrics_data:
    r = t8.add_row()
    for i in range(3):
        r.cells[i].text = row[i]

# Table 9: Monitoring Roles
t9 = doc.tables[9]
roles_data = [
    ("DevOps / SRE Team", "Infrastructure health, container autoscaling, CPU/RAM, DB connection pool", "Continuous 24/7 (Hypercare War Room)"),
    ("Database Administrator (DBA)", "Database lock contention, slow query logs, read replica replication lag", "Every 30 minutes in peak hours"),
    ("QA & Automation Lead", "Synthetic user transaction testing, smoke test validation", "Hourly automated test execution"),
    ("Customer Support Lead", "Pilot clinic tickets, feedback triage, incident escalation to engineering", "Continuous shift monitoring"),
    ("Systems Analyst / Architect", "Overall health KPIs, executive status reports, capacity alignment", "Daily 08:00 AM & 05:00 PM reviews")
]
while len(t9.rows) > 1:
    t9._tbl.remove(t9.rows[-1]._tr)
for row in roles_data:
    r = t9.add_row()
    for i in range(3):
        r.cells[i].text = row[i]

for p in doc.paragraphs:
    if '[Describe what happens when an alert is triggered, including' in p.text:
        p.text = (
            "- Severity 1 (Critical - P0): Automated PagerDuty escalation calls SRE, DevOps, and Lead Architect immediately. "
            "War Room convenes within 10 minutes. If core booking is impaired, circuit breaking activates.\n"
            "- Severity 2 (Major - P1): Slack alert to #eng-triage; assigned engineer investigates within 30 minutes.\n"
            "- Severity 3 (Minor - P2): Ticket logged automatically in Jira backlog for scheduled sprint remediation."
        )

doc.save(out1)
print(f"Successfully generated comprehensive update: {out1} ({os.path.getsize(out1)} bytes)")
