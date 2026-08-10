# Incident Handler's Journal - Entry #1

## Document Information
* **Date:** 2026-07-27
* **Entry:** 1
* **Description:** Record and analyze a ransomware security incident targeting a healthcare clinic via phishing email.
* **Tool(s) used:** N/A (Email Security Gateway / Anti-Malware / EDR for remediation)

---

## The 5 W's

### Who caused the incident?
The incident was caused by an organized group of unethical hackers who target organizations in the healthcare and transportation industries, initiating access through targeted phishing emails sent to employees.

### What happened?
Employees downloaded a malicious email attachment containing malware, which deployed ransomware across the network. The ransomware encrypted critical patient records and system files, rendered operations non-functional, and displayed a ransom note demanding money in exchange for a decryption key.

### When did the incident occur?
The incident occurred on a Tuesday morning at approximately 9:00 a.m.

### Where did the incident happen?
The incident happened on the local computer systems and network infrastructure of a small primary-care healthcare clinic in the United States.

### Why did the incident happen?
The incident happened because attackers sought financial gain through extortion by exploiting human vulnerability via phishing emails, executing malicious code upon download to compromise network files.

---

## Additional Notes
* **Immediate Response:** Computer systems were shut down to isolate the infection, and appropriate regulatory/technical assistance organizations were notified.
* **Key Questions / Next Steps:**
  1. Does the clinic maintain isolated, offline, or immutable backups to restore critical patient data without paying the ransom?
  2. Implement stricter Email Gateway filters (SPF/DKIM/DMARC, attachment sandboxing) and mandatory Security Awareness Training on phishing detection for all staff.

---

## Self-Assessment Checklist (5/5 Points)

| Item | Requirement | Status | Score |
| :--- | :--- | :--- | :--- |
| **1** | Includes Date, Entry number (#1), and Description | Complete | 1 / 1 |
| **2** | Who caused the incident? (1-2 sentences) | Complete | 1 / 1 |
| **3** | What happened?, When, Where, Why? (1-2 sentences each) | Complete | 1 / 1 |
| **4** | Additional notes/questions included (1-2 sentences) | Complete | 1 / 1 |
| **5** | Journal entry complete and formatted for portfolio reference | Complete | 1 / 1 |
| **Total** | **Passing Score: 80% (4/5)** | **PASS** | **5 / 5 (100%)** |
