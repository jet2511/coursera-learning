"""
generate_capstone_visuals.py
Tạo toàn bộ các hình ảnh sơ đồ kiến trúc chuẩn cao cấp phục vụ chèn vào slide Capstone Presentation.
"""

from PIL import Image, ImageDraw, ImageFont
import os

out_dir = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 6 - Final Submission and Evaluation\Final_Submission_Result"
os.makedirs(out_dir, exist_ok=True)

# Colors
NAVY = (15, 32, 67)
SLATE = (40, 60, 95)
LIGHT_BG = (245, 247, 250)
WHITE = (255, 255, 255)
BORDER_BLUE = (30, 115, 190)
ACCENT_BLUE = (0, 102, 204)
CARD_BG = (255, 255, 255)
TEXT_DARK = (20, 30, 45)
TEXT_MUTED = (80, 90, 105)
SUCCESS_GREEN = (34, 139, 34)
WARN_ORANGE = (220, 120, 20)
PURPLE = (110, 60, 160)

def draw_card(draw, x, y, w, h, title, subtitle="", bg=CARD_BG, border=BORDER_BLUE, title_col=NAVY):
    draw.rectangle([(x, y), (x + w, y + h)], fill=bg, outline=border, width=2)
    draw.text((x + 12, y + 10), title, fill=title_col)
    if subtitle:
        draw.text((x + 12, y + 30), subtitle, fill=TEXT_MUTED)

def draw_arrow_h(draw, x1, y, x2, label=""):
    draw.line([(x1, y), (x2, y)], fill=BORDER_BLUE, width=2)
    draw.polygon([(x2, y), (x2 - 8, y - 5), (x2 - 8, y + 5)], fill=BORDER_BLUE)
    if label:
        draw.text(((x1 + x2)//2 - len(label)*3, y - 16), label, fill=ACCENT_BLUE)

def draw_arrow_v(draw, x, y1, y2, label=""):
    draw.line([(x, y1), (x, y2)], fill=BORDER_BLUE, width=2)
    draw.polygon([(x, y2), (x - 5, y2 - 8), (x + 5, y2 - 8)], fill=BORDER_BLUE)
    if label:
        draw.text((x + 8, (y1 + y2)//2 - 8), label, fill=ACCENT_BLUE)

# 1. Use Case Diagram
def create_use_case_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "RETAIL BANK DIGITAL CORE - USE CASE ARCHITECTURE DIAGRAM", fill=NAVY)
    d.text((30, 48), "Actors & Core System Interaction Boundaries (UML Specification)", fill=TEXT_MUTED)

    # System boundary
    d.rectangle([(280, 80), (920, 560)], fill=(238, 243, 250), outline=ACCENT_BLUE, width=2)
    d.text((300, 95), "SYSTEM BOUNDARY: Retail Bank Digital Core Platform", fill=NAVY)

    # Left Actors
    draw_card(d, 40, 140, 180, 70, "Retail Customer", "Web / Mobile Banking", bg=(230, 240, 255))
    draw_card(d, 40, 320, 180, 70, "Branch Teller", "Staff Internal Portal", bg=(230, 240, 255))
    draw_card(d, 40, 440, 180, 70, "Loan Officer", "Credit Origination UI", bg=(230, 240, 255))

    # Right External Services
    draw_card(d, 960, 150, 190, 70, "National eKYC Registry", "Gov Identity Validation", bg=(255, 245, 230))
    draw_card(d, 960, 280, 190, 70, "Credit Bureau API", "FICO / Credit Score", bg=(255, 245, 230))
    draw_card(d, 960, 410, 190, 70, "Payment Switch / Fed", "External Clearing Switch", bg=(255, 245, 230))

    # Use cases inside boundary
    cases = [
        (320, 140, "UC-01: Digital Onboarding & eKYC", "Self-service identity & account opening"),
        (320, 220, "UC-02: Real-Time Funds Transfer", "Internal ledger debit/credit + external switch"),
        (320, 300, "UC-03: Loan Application & Underwriting", "Credit score check & rule-based approval"),
        (320, 380, "UC-04: Real-Time Fraud & AML Scoring", "Event-driven fraud detection on transactions"),
        (320, 460, "UC-05: Account Servicing & Statement", "Ledger balance, transaction history, audit"),
    ]
    for x, y, title, sub in cases:
        draw_card(d, x, y, 560, 60, title, sub, bg=WHITE, border=BORDER_BLUE)
        draw_arrow_h(d, 220, y + 30, x, "")

    draw_arrow_h(d, 880, 170, 960, "eKYC Check")
    draw_arrow_h(d, 880, 330, 960, "Credit Query")
    draw_arrow_h(d, 880, 250, 960, "Clearing")

    d.text((30, 568), "Caption: Use Case Diagram mapping 3 primary actors and 3 external systems into Core Banking microservices.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "01_use_case_diagram.png"))

# 2. WBS Visual Tree
def create_wbs_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "WORK BREAKDOWN STRUCTURE (WBS) - RETAIL BANK MODERNIZATION", fill=NAVY)
    d.text((30, 48), "Hierarchical Task Decomposition across 5 Engineering Phases", fill=TEXT_MUTED)

    # Root Level
    draw_card(d, 350, 80, 500, 55, "1.0 Retail Bank Digital Core Modernization", "Target Duration: 9.5 Months | Budget: Regulated CapEx", bg=(220, 235, 252))

    # Phase 1 to 5
    phases = [
        (40, 180, 210, "1.1 Planning & Charter", "1.1.1 Stakeholders\n1.1.2 BRD & RTM\n1.1.3 Cloud Architecture"),
        (275, 180, 210, "1.2 Process & Models", "1.2.1 Onboarding Flow\n1.2.2 Sequence Models\n1.2.3 Data Flowcharts"),
        (510, 180, 210, "1.3 Enterprise Design", "1.3.1 Relational Schema\n1.3.2 EDA Event Broker\n1.3.3 Security In-Depth"),
        (745, 180, 210, "1.4 PoC & Validation", "1.4.1 Kafka Prototype\n1.4.2 TDD & BDD Suites\n1.4.3 Migration Testing"),
        (980, 180, 210, "1.5 CI/CD & Operations", "1.5.1 GitOps Pipeline\n1.5.2 Prometheus/Grafana\n1.5.3 Disaster Recovery")
    ]
    for x, y, w, title, tasks in phases:
        draw_arrow_v(d, 600, 135, 160)
        draw_card(d, x, y, w, 65, title, "", bg=(235, 245, 255), border=BORDER_BLUE)
        # Tasks box
        draw_card(d, x, y + 80, w, 280, "Key Work Packages:", tasks, bg=WHITE, border=SLATE)

    d.line([(145, 160), (1085, 160)], fill=BORDER_BLUE, width=2)
    for x, _, w, _, _ in phases:
        draw_arrow_v(d, x + w//2, 160, 180)

    d.text((30, 568), "Caption: WBS hierarchy detailing all core phases, deliverables, and engineering work packages.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "02_wbs_diagram.png"))

# 3. Network Diagram & Critical Path
def create_network_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "PROJECT NETWORK DIAGRAM & CRITICAL PATH ANALYSIS", fill=NAVY)
    d.text((30, 48), "Precedence Relationship, Activity Durations & Critical Path (Red Highlight)", fill=TEXT_MUTED)

    # Nodes
    nodes = [
        (40, 250, "Start", "Project Kickoff", False),
        (160, 250, "1.1.1 Stakeholders\n(0.5w)", "ID Stakeholders", True),
        (320, 250, "1.1.2 Gather Req\n(1.5w)", "BRD & RTM", True),
        (480, 140, "1.2.1 Process Models\n(2.0w)", "BPMN & Flows", False),
        (480, 360, "1.3.1 Cloud Setup\n(2.5w)", "Docker/K8s/VPC", True),
        (660, 140, "1.3.2 Data Architect\n(3.0w)", "3NF Schema & Migr", False),
        (660, 360, "1.4.1 PoC Prototype\n(4.0w)", "Kafka Fraud PoC", True),
        (840, 250, "1.5.1 CI/CD & QA\n(3.0w)", "TDD/BDD & ArgoCD", True),
        (1010, 250, "1.5.2 Deploy & BDR\n(2.0w)", "Go-Live & BDR Drill", True),
    ]

    for x, y, name, sub, crit in nodes:
        bg = (255, 230, 230) if crit else WHITE
        border = (200, 30, 30) if crit else BORDER_BLUE
        draw_card(d, x, y, 130, 75, name, sub, bg=bg, border=border, title_col=(180, 20, 20) if crit else NAVY)

    # Connectors
    draw_arrow_h(d, 100, 285, 160)
    draw_arrow_h(d, 290, 285, 320)
    # Split
    draw_line_diag = lambda x1, y1, x2, y2, col: d.line([(x1, y1), (x2, y2)], fill=col, width=3 if col==(200,30,30) else 2)
    draw_line_diag(450, 270, 480, 175, BORDER_BLUE)
    draw_line_diag(450, 300, 480, 395, (200, 30, 30))
    # Paths
    draw_arrow_h(d, 610, 175, 660)
    draw_arrow_h(d, 610, 395, 660)
    # Merge
    draw_line_diag(790, 175, 840, 270, BORDER_BLUE)
    draw_line_diag(790, 395, 840, 300, (200, 30, 30))
    draw_arrow_h(d, 970, 285, 1010)

    # Legend
    d.rectangle([(840, 480), (1160, 560)], fill=WHITE, outline=SLATE, width=2)
    d.rectangle([(855, 495), (895, 515)], fill=(255, 230, 230), outline=(200, 30, 30), width=2)
    d.text((910, 498), "Critical Path (Total = 13.5 Weeks)", fill=(180, 20, 20))
    d.rectangle([(855, 530), (895, 545)], fill=WHITE, outline=BORDER_BLUE, width=2)
    d.text((910, 530), "Non-Critical Activity (With Float)", fill=NAVY)

    d.text((30, 568), "Caption: Activity network diagram indicating critical path driving overall project launch schedule.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "03_network_diagram.png"))

# 4. Risk Matrix Visualization
def create_risk_matrix():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "ENTERPRISE RISK MATRIX - LIKELIHOOD VS. IMPACT (5x5 GRID)", fill=NAVY)
    d.text((30, 48), "Prioritized Threat and Opportunity Positioning with Risk Threshold Zones", fill=TEXT_MUTED)

    # 5x5 grid
    ox, oy = 240, 100
    cw, ch = 140, 80

    # Colors for zones
    # y=0 is Likelihood 5, y=4 is Likelihood 1
    zone_colors = [
        [(255, 200, 100), (255, 140, 100), (255, 140, 100), (255, 80, 80), (255, 50, 50)], # L5
        [(255, 240, 120), (255, 200, 100), (255, 140, 100), (255, 80, 80), (255, 80, 80)], # L4
        [(200, 240, 140), (255, 240, 120), (255, 200, 100), (255, 140, 100), (255, 80, 80)], # L3
        [(160, 230, 160), (200, 240, 140), (255, 240, 120), (255, 200, 100), (255, 140, 100)], # L2
        [(160, 230, 160), (160, 230, 160), (200, 240, 140), (255, 240, 120), (255, 200, 100)], # L1
    ]

    for r in range(5):
        for c in range(5):
            x1, y1 = ox + c * cw, oy + r * ch
            x2, y2 = x1 + cw, y1 + ch
            d.rectangle([(x1, y1), (x2, y2)], fill=zone_colors[r][c], outline=(200, 210, 220), width=1)

    # Axis labels
    impact_labels = ["1 (Insignificant)", "2 (Minor)", "3 (Moderate)", "4 (Major)", "5 (Catastrophic)"]
    for c, lab in enumerate(impact_labels):
        d.text((ox + c * cw + 15, oy + 5 * ch + 10), lab, fill=NAVY)
    d.text((ox + 250, oy + 5 * ch + 35), "IMPACT (SEVERITY) --->", fill=NAVY)

    lh_labels = ["5 (Almost Certain)", "4 (Likely)", "3 (Possible)", "2 (Unlikely)", "1 (Rare)"]
    for r, lab in enumerate(lh_labels):
        d.text((40, oy + r * ch + 30), lab, fill=NAVY)
    d.text((80, oy - 25), "LIKELIHOOD ^", fill=NAVY)

    # Plot Risks
    # R1: L4, I5 -> r=1, c=4
    d.rectangle([(ox + 4*cw + 20, oy + 1*ch + 20), (ox + 4*cw + 120, oy + 1*ch + 60)], fill=(180, 20, 20), outline=WHITE, width=2)
    d.text((ox + 4*cw + 25, oy + 1*ch + 25), "R1: KYC API Viol\nScore=20 (Extreme)", fill=WHITE)

    # R2: L4, I4 -> r=1, c=3
    d.rectangle([(ox + 3*cw + 20, oy + 1*ch + 20), (ox + 3*cw + 120, oy + 1*ch + 60)], fill=(180, 20, 20), outline=WHITE, width=2)
    d.text((ox + 3*cw + 25, oy + 1*ch + 25), "R2: Legacy Integr\nScore=16 (Extreme)", fill=WHITE)

    # R3: L3, I5 -> r=2, c=4
    d.rectangle([(ox + 4*cw + 20, oy + 2*ch + 20), (ox + 4*cw + 120, oy + 2*ch + 60)], fill=(220, 100, 20), outline=WHITE, width=2)
    d.text((ox + 4*cw + 25, oy + 2*ch + 25), "R3: CI/CD Crash\nScore=15 (High)", fill=WHITE)

    # R4: L3, I3 -> r=2, c=2
    d.rectangle([(ox + 2*cw + 20, oy + 2*ch + 20), (ox + 2*cw + 120, oy + 2*ch + 60)], fill=(200, 160, 20), outline=WHITE, width=2)
    d.text((ox + 2*cw + 25, oy + 2*ch + 25), "R4: Scope Creep\nScore=9 (Medium)", fill=NAVY)

    # Legend box
    d.rectangle([(980, 100), (1170, 250)], fill=WHITE, outline=SLATE, width=2)
    d.text((995, 110), "RISK ACTION ZONES", fill=NAVY)
    d.rectangle([(995, 135), (1025, 155)], fill=(255, 50, 50))
    d.text((1035, 138), "Extreme (Immediate)", fill=NAVY)
    d.rectangle([(995, 165), (1025, 185)], fill=(255, 140, 100))
    d.text((1035, 168), "High (Mitigate ASAP)", fill=NAVY)
    d.rectangle([(995, 195), (1025, 215)], fill=(255, 240, 120))
    d.text((1035, 198), "Medium (Monitor)", fill=NAVY)
    d.rectangle([(995, 225), (1025, 245)], fill=(160, 230, 160))
    d.text((1035, 228), "Low (Accept)", fill=NAVY)

    d.text((30, 568), "Caption: Risk Matrix positioning top technical, compliance, and integration risks on a standardized 5x5 grid.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "04_risk_matrix.png"))

# 5. Core Banking Flowchart
def create_process_flowchart():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "CORE BANKING PROCESS FLOWCHART - ONBOARDING & LOAN ORIGINATION", fill=NAVY)
    d.text((30, 48), "End-to-End Decision & Approval Workflow with Exception Branching", fill=TEXT_MUTED)

    # Start
    draw_card(d, 40, 250, 110, 60, "START", "Customer Request", bg=(200, 230, 255), border=BORDER_BLUE)
    draw_arrow_h(d, 150, 280, 200)

    # Step 1: Submit data
    draw_card(d, 200, 250, 150, 60, "1. Submit PII & Docs", "Mobile / Web Form", bg=WHITE)
    draw_arrow_h(d, 350, 280, 400)

    # Decision: eKYC Pass?
    d.polygon([(460, 240), (520, 280), (460, 320), (400, 280)], fill=(255, 250, 210), outline=WARN_ORANGE, width=2)
    d.text((435, 272), "eKYC Pass?", fill=NAVY)

    # eKYC No -> Branch Appt
    draw_arrow_v(d, 460, 320, 420, "Fail")
    draw_card(d, 390, 420, 150, 60, "Schedule Branch Appt", "Manual Verification", bg=(255, 235, 220), border=WARN_ORANGE)
    draw_arrow_h(d, 540, 450, 620)

    # eKYC Yes -> Credit & Fraud Engine
    draw_arrow_h(d, 520, 280, 600, "Pass")
    draw_card(d, 600, 250, 160, 60, "2. Fraud & AML Engine", "Kafka Event Stream", bg=WHITE)
    draw_arrow_h(d, 760, 280, 810)

    # Decision 2: AML / Credit Clear?
    d.polygon([(870, 240), (930, 280), (870, 320), (810, 280)], fill=(255, 250, 210), outline=WARN_ORANGE, width=2)
    d.text((840, 272), "AML Clear?", fill=NAVY)

    # AML Clear No -> Reject
    draw_arrow_v(d, 870, 240, 160, "Flagged")
    draw_card(d, 810, 100, 150, 60, "Reject / SAR Report", "Compliance Review", bg=(255, 220, 220), border=(200, 30, 30))

    # AML Clear Yes -> Activate Account
    draw_arrow_h(d, 930, 280, 990, "Approved")
    draw_card(d, 990, 250, 160, 60, "3. Activate Account", "Core Ledger Entry", bg=(220, 255, 220), border=SUCCESS_GREEN)
    draw_arrow_v(d, 1070, 310, 380)

    draw_card(d, 1010, 380, 120, 50, "END: Active", "SMS Notification", bg=(200, 230, 255), border=BORDER_BLUE)

    d.text((30, 568), "Caption: Standardized BPMN flowchart showing digital straight-through processing (STP) and branch exception loops.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "05_process_flowchart.png"))

# 6. System Context & DFD Level 0/1
def create_system_dfd():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "SYSTEM DESIGN: DATA FLOW DIAGRAM (DFD LEVEL 1) & SYSTEM CONTEXT", fill=NAVY)
    d.text((30, 48), "Data Ingestion, Microservice Processing Pipelines & Storage Boundaries", fill=TEXT_MUTED)

    # Core system boundary
    d.rectangle([(260, 90), (940, 550)], fill=(240, 246, 255), outline=ACCENT_BLUE, width=2)
    d.text((280, 105), "CORE BANKING ENGINE BOUNDARY", fill=NAVY)

    # External entities
    draw_card(d, 40, 150, 180, 70, "Customer (Mobile/Web)", "API Requests", bg=WHITE)
    draw_card(d, 40, 350, 180, 70, "Branch Portal", "Internal Staff Requests", bg=WHITE)
    draw_card(d, 980, 150, 180, 70, "Payment Switch", "ACH / Fedwire Clearing", bg=WHITE)
    draw_card(d, 980, 350, 180, 70, "Regulator (FinCEN)", "AML Reports & Audit", bg=WHITE)

    # API Gateway
    draw_card(d, 290, 220, 130, 180, "Kong API\nGateway", "mTLS, Rate Limit,\nJWT Validation", bg=(225, 240, 255), border=BORDER_BLUE)
    draw_arrow_h(d, 220, 260, 290, "REST / JSON")
    draw_arrow_h(d, 220, 370, 290, "Internal API")

    # Microservices
    services = [
        (480, 140, "Onboarding Service", "eKYC verification"),
        (480, 240, "Transaction Service", "ACID Ledger Transfer"),
        (480, 340, "Loan Origination", "Credit Underwriting"),
        (480, 440, "Fraud Detection", "Kafka Real-Time AML"),
    ]
    for x, y, name, sub in services:
        draw_card(d, x, y, 180, 60, name, sub, bg=WHITE, border=SLATE)
        draw_arrow_h(d, 420, y + 30, x)

    # Databases
    draw_card(d, 740, 170, 160, 80, "PostgreSQL\n(Ledger DB)", "Accounts & Balances\nACID Compliant", bg=(230, 255, 230), border=SUCCESS_GREEN)
    draw_card(d, 740, 330, 160, 80, "Apache Kafka\n(Event Stream)", "Immutable Events\nTopic: fraud-events", bg=(255, 245, 230), border=WARN_ORANGE)

    draw_arrow_h(d, 660, 260, 740, "Commit Txn")
    draw_arrow_h(d, 660, 460, 740, "Publish Event")
    draw_arrow_h(d, 900, 210, 980, "Settle Txn")
    draw_arrow_h(d, 900, 370, 980, "SAR Stream")

    d.text((30, 568), "Caption: DFD Level 1 showcasing API Gateway entry, microservice decomposition, and decoupled persistence layers.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "06_system_dfd.png"))

# 7. Sequence Diagram
def create_sequence_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "SEQUENCE DIAGRAM - HIGH-VALUE REAL-TIME FUNDS TRANSFER WITH MFA", fill=NAVY)
    d.text((30, 48), "Synchronous Orchestration & Asynchronous Event Streaming Workflow", fill=TEXT_MUTED)

    # Lifelines
    cols = [
        (100, "Customer"),
        (280, "API Gateway"),
        (460, "Payment Service"),
        (640, "Keycloak MFA"),
        (820, "Ledger DB"),
        (1000, "Kafka (Fraud)")
    ]
    for x, name in cols:
        draw_card(d, x - 60, 90, 120, 40, name, "", bg=(230, 240, 255), border=BORDER_BLUE)
        d.line([(x, 130), (x, 530)], fill=(180, 190, 205), width=2)

    # Messages
    msgs = [
        (150, 100, 280, "1. POST /transfers (Amount=$15,000)", True),
        (190, 280, 460, "2. Forward request with JWT", True),
        (230, 460, 640, "3. Challenge MFA (High-Value Rule)", True),
        (270, 640, 100, "4. Push OTP / Biometric Prompt", False),
        (310, 100, 640, "5. Submit Verified OTP", True),
        (350, 640, 460, "6. MFA Verified Token Granted", False),
        (390, 460, 820, "7. BEGIN TXN: Debit Acc A, Credit Acc B", True),
        (430, 820, 460, "8. TXN COMMITTED (Balance Updated)", False),
        (470, 460, 1000, "9. Asynch Publish Event: 'TransferCompleted'", True),
        (510, 460, 100, "10. HTTP 201 Created (Transaction Receipt)", False),
    ]

    for y, x1, x2, txt, sync in msgs:
        col = ACCENT_BLUE if sync else SUCCESS_GREEN
        d.line([(x1, y), (x2, y)], fill=col, width=2)
        # Arrowhead
        if x2 > x1:
            d.polygon([(x2, y), (x2 - 8, y - 5), (x2 - 8, y + 5)], fill=col)
        else:
            d.polygon([(x2, y), (x2 + 8, y - 5), (x2 + 8, y + 5)], fill=col)
        d.text(((x1 + x2)//2 - len(txt)*3, y - 16), txt, fill=NAVY)

    d.text((30, 568), "Caption: Sequence diagram depicting MFA step-up security, ACID transaction settlement, and decoupled event streaming.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "07_sequence_diagram.png"))

# 8. Conceptual & Logical ERD
def create_erd_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "ENTERPRISE DATABASE DESIGN - CONCEPTUAL & LOGICAL ERD (3NF)", fill=NAVY)
    d.text((30, 48), "Normalized Relational Entity Models, Primary Keys (PK), Foreign Keys (FK) & Constraints", fill=TEXT_MUTED)

    # Entity cards
    entities = [
        (40, 100, "CUSTOMERS (PK: customer_id)", "customer_id [PK, INT]\nbranch_id [FK, INT]\nfirst_name, last_name\nekyc_status [VERIFIED]\nrisk_tier [LOW/MED/HIGH]\ncreated_at [TIMESTAMP]"),
        (340, 100, "BRANCHES (PK: branch_id)", "branch_id [PK, INT]\nbranch_code [VARCHAR, UQ]\nbranch_name [VARCHAR]\nrouting_number [VARCHAR]\nstatus [ACTIVE]"),
        (640, 100, "ACCOUNTS (PK: account_id)", "account_id [PK, INT]\ncustomer_id [FK, INT]\naccount_number [UQ]\naccount_type [CHECKING]\nbalance [DECIMAL(18,2)]\nstatus [ACTIVE]"),
        (940, 100, "LOANS (PK: loan_id)", "loan_id [PK, INT]\ncustomer_id [FK, INT]\nloan_amount [DECIMAL]\ninterest_rate [DECIMAL]\napproval_status\norigination_date"),
        (490, 350, "TRANSACTIONS (PK: txn_id)", "txn_id [PK, INT]\nsource_acc_id [FK, INT]\ndest_acc_id [FK, INT]\namount [DECIMAL(18,2)]\ntxn_type [TRANSFER]\nstatus [SETTLED]\ncreated_at [TIMESTAMP]"),
    ]

    for x, y, title, attrs in entities:
        d.rectangle([(x, y), (x + 230, y + 210 if y==100 else y + 200)], fill=WHITE, outline=BORDER_BLUE, width=2)
        d.rectangle([(x, y), (x + 230, y + 35)], fill=(230, 240, 255), outline=BORDER_BLUE, width=2)
        d.text((x + 8, y + 8), title, fill=NAVY)
        d.text((x + 10, y + 45), attrs, fill=TEXT_DARK)

    # Relationships lines
    # Branch -> Customer (1:N)
    d.line([(340, 140), (270, 140)], fill=ACCENT_BLUE, width=2)
    d.text((290, 120), "1:N", fill=ACCENT_BLUE)

    # Customer -> Account (1:N)
    d.line([(270, 180), (640, 180)], fill=ACCENT_BLUE, width=2)
    d.text((450, 160), "1:N (Owns)", fill=ACCENT_BLUE)

    # Customer -> Loan (1:N)
    d.line([(270, 210), (940, 210)], fill=ACCENT_BLUE, width=2)
    d.text((580, 220), "1:N (Borrows)", fill=ACCENT_BLUE)

    # Account -> Transactions (1:N)
    draw_arrow_v(d, 600, 310, 350, "1:N (Debit/Credit)")

    d.text((30, 568), "Caption: Fully normalized 3NF relational data model guaranteeing ACID transaction integrity and zero redundancy.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "08_erd_diagram.png"))

# 9. Security Architecture Diagram
def create_security_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "SECURITY ARCHITECTURE: DEFENSE-IN-DEPTH & ZERO-TRUST FRAMEWORK", fill=NAVY)
    d.text((30, 48), "Multi-Layered Protection, Cryptographic Controls & Regulatory Compliance Boundaries", fill=TEXT_MUTED)

    # Zones
    zones = [
        (40, 100, 200, "Edge / Perimeter", "Cloudflare WAF / Anti-DDoS\nTLS 1.3 Termination\nStrict CORS & Geo-IP", (255, 235, 235), (200, 60, 60)),
        (270, 100, 200, "DMZ / Ingress", "Kong API Gateway\nOAuth2 / OpenID Connect\nMutual TLS (mTLS)\nRate Limiting (Token Bucket)", (255, 245, 230), WARN_ORANGE),
        (500, 100, 240, "Private App Zone", "Kubernetes Microservices\nIstio Service Mesh\nRBAC / NetworkPolicies\nHashiCorp Vault Secrets", (240, 245, 255), ACCENT_BLUE),
        (770, 100, 200, "Data Tier (Encrypted)", "PostgreSQL (TDE at rest)\nKafka (SCRAM-SHA-512)\nAWS KMS CMK Keys\nWORM Compliance Storage", (235, 255, 235), SUCCESS_GREEN),
        (1000, 100, 160, "Governance / SIEM", "Splunk Audit Logs\nFalco Runtime Sec\nSonarQube CI Gate\nPCI-DSS / FFIEC", (245, 235, 255), PURPLE)
    ]

    for x, y, w, title, desc, bg, border in zones:
        d.rectangle([(x, y), (x + w, y + 430)], fill=bg, outline=border, width=2)
        d.rectangle([(x, y), (x + w, y + 40)], fill=WHITE, outline=border, width=2)
        d.text((x + 10, y + 10), title, fill=NAVY)
        d.text((x + 10, y + 60), desc, fill=TEXT_DARK)

    # Flow arrows
    draw_arrow_h(d, 240, 250, 270)
    draw_arrow_h(d, 470, 250, 500)
    draw_arrow_h(d, 740, 250, 770)
    draw_arrow_h(d, 970, 250, 1000)

    d.text((30, 568), "Caption: Comprehensive Defense-in-Depth security model satisfying FFIEC, PCI-DSS, and ISO 27001 mandates.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "09_security_architecture.png"))

# 10. CI/CD & Disaster Recovery Workflow
def create_cicd_bdr_diagram():
    img = Image.new("RGB", (1200, 600), color=LIGHT_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(10, 10), (1190, 590)], outline=SLATE, width=3)
    d.text((30, 25), "ENTERPRISE CI/CD PIPELINE & DISASTER RECOVERY RESTORATION WORKFLOW", fill=NAVY)
    d.text((30, 48), "Automated GitOps Progression with Canary Deployments & High-Availability BDR Architecture", fill=TEXT_MUTED)

    # Top: CI/CD Pipeline
    d.rectangle([(30, 85), (1170, 305)], fill=WHITE, outline=BORDER_BLUE, width=2)
    d.text((45, 95), "CI/CD REGULATED DEPLOYMENT WORKFLOW (GitOps + ArgoCD)", fill=NAVY)

    stages = [
        (50, 135, "1. Git Push", "Developer commit\nGitleaks pre-commit"),
        (230, 135, "2. Build & Test", "Maven compile\nTDD Unit Tests"),
        (420, 135, "3. Security Gate", "SonarQube SAST\nTrivy Container Scan"),
        (610, 135, "4. Staging Deploy", "Automated DAST\nSynthetic Smoke Test"),
        (800, 135, "5. Canary Prod", "10% -> 50% -> 100%\nPrometheus Monitor"),
        (990, 135, "6. Auto Rollback", "Triggers if error > 1%\nInstant revert (<30s)"),
    ]
    for x, y, name, sub in stages:
        draw_card(d, x, y, 160, 135, name, sub, bg=(245, 250, 255), border=BORDER_BLUE)
        if x < 990:
            draw_arrow_h(d, x + 160, y + 65, x + 180)

    # Bottom: BDR Strategy
    d.rectangle([(30, 330), (1170, 550)], fill=WHITE, outline=SUCCESS_GREEN, width=2)
    d.text((45, 340), "DISASTER RECOVERY ARCHITECTURE & PITR (RTO < 15 Mins | RPO < 1 Min)", fill=NAVY)

    bdr_boxes = [
        (50, 380, 250, "Primary Region (Region A)", "Active Kubernetes Cluster\nPostgreSQL Master (Read/Write)\nContinuous WAL Archiving"),
        (370, 380, 220, "Replication Layer", "Cross-Region S3 Sync (WAL)\nAsync DB Streaming\nKafka MirrorMaker 2"),
        (660, 380, 250, "Disaster Region (Region B)", "Standby Kubernetes Cluster\nRead Replicas Hot Standby\nAutomated Route53 Failover"),
        (980, 380, 170, "Restoration Targets", "RPO: < 1 Minute\nRTO: < 15 Minutes\nAutomated Health Check"),
    ]
    for x, y, w, name, sub in bdr_boxes:
        draw_card(d, x, y, w, 140, name, sub, bg=(245, 255, 245), border=SUCCESS_GREEN)
        if x < 980:
            draw_arrow_h(d, x + w, y + 70, x + w + 20)

    d.text((30, 568), "Caption: End-to-end GitOps CI/CD delivery pipeline coupled with automated cross-region Disaster Recovery failover.", fill=TEXT_MUTED)
    img.save(os.path.join(out_dir, "10_cicd_bdr_diagram.png"))

if __name__ == "__main__":
    create_use_case_diagram()
    create_wbs_diagram()
    create_network_diagram()
    create_risk_matrix()
    create_process_flowchart()
    create_system_dfd()
    create_sequence_diagram()
    create_erd_diagram()
    create_security_diagram()
    create_cicd_bdr_diagram()
    print("Successfully generated all 10 high-resolution architectural diagrams!")
