from PIL import Image, ImageDraw
import os

width = 1200
height = 800
bg_color = (248, 250, 252) # slate-50
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Palette
primary = (30, 58, 138)    # Blue 900
secondary = (14, 165, 233) # Sky 500
card_bg = (255, 255, 255)
border = (148, 163, 184)
text_dark = (15, 23, 42)
text_muted = (71, 85, 105)
arrow_color = (37, 99, 235)
accent_green = (16, 185, 129)
accent_purple = (147, 51, 234)

# Header
draw.rectangle([(0, 0), (width, 80)], fill=primary)
draw.text((40, 25), "RETAIL BANK DIGITAL CORE - END-TO-END API & DATA FLOW ARCHITECTURE", fill=(255, 255, 255))

# Boxes definition: 6 vertical / staged columns
stages = [
    ("1. Client Apps", "Mobile & Web Banking\n- Initiates Transfer\n- Sends OAuth2 Bearer\n- Receives Real-time Status", 50, 160, 210, 360, primary),
    ("2. API Gateway", "Kong / Edge Gateway\n- Terminates TLS 1.3\n- Validates JWT & Scopes\n- Enforces Rate Limits\n- Injects Trace ID", 240, 160, 400, 360, secondary),
    ("3. Transaction Core", "Payment Microservice\n- Idempotency Check\n- Coordinates SAGA\n- Publishes Txn Event\n- Dispatches Fraud Check", 430, 160, 590, 360, primary),
    ("4. Fraud & Risk Engine", "AI Fraud & AML\n- Real-time ML Scoring\n- Blacklist Validation\n- Approves / Rejects\n- Latency < 150ms", 620, 160, 780, 360, accent_purple),
    ("5. Core Ledger", "PostgreSQL / Spanner\n- ACID Double-Entry\n- Account Debit / Credit\n- Generates Ledger Hash\n- Commits Transaction", 810, 160, 970, 360, primary),
    ("6. Notification / Ext", "Notifications & External\n- Kafka Consumer\n- SMS / Push Dispatch\n- Ext Clearing / SWIFT\n- Audits to WORM S3", 1000, 160, 1160, 360, accent_green),
]

for title, desc, x1, y1, x2, y2, color in stages:
    draw.rectangle([(x1, y1), (x2, y2)], fill=card_bg, outline=color, width=3)
    draw.rectangle([(x1, y1), (x2, y1 + 35)], fill=color)
    draw.text((x1 + 10, y1 + 10), title, fill=(255, 255, 255))
    draw.text((x1 + 10, y1 + 50), desc, fill=text_dark)

# Draw forward arrows across 1 -> 2 -> 3 -> 4 -> 5 -> 6
arrow_y = 260
for i in range(5):
    _, _, x2, _, _, _, _ = stages[i]
    _, _, _, _, _, _, _ = stages[i+1]
    nx1 = stages[i+1][2]
    draw.line([(x2, arrow_y), (nx1, arrow_y)], fill=arrow_color, width=4)
    draw.polygon([(nx1, arrow_y), (nx1 - 8, arrow_y - 6), (nx1 - 8, arrow_y + 6)], fill=arrow_color)

# Draw backward feedback line (Ledger/Txn -> Client)
ret_y = 320
draw.line([(970, ret_y), (970, 420), (130, 420), (130, 360)], fill=accent_green, width=3)
draw.polygon([(130, 360), (124, 370), (136, 370)], fill=accent_green)
draw.text((350, 430), "<-- HTTP 201 Created / Approved (Balance Updated, Txn Reference ID) <--", fill=accent_green)

# Bottom Details Box (Security & Integration Contracts)
bot_y = 500
draw.rectangle([(50, bot_y), (1160, 750)], fill=(241, 245, 249), outline=border, width=2)
draw.text((70, bot_y + 15), "END-TO-END DATA FLOW & SECURITY PROTOCOLS SPECIFICATION:", fill=primary)
spec_lines = [
    "1. Client to Gateway: HTTPS / TLS 1.3, OAuth 2.0 Authorization Code + PKCE, Bearer JWT in Authorization header.",
    "2. Gateway to Microservices: Mutual TLS (mTLS), Internal Service Mesh (Envoy), propagation of X-Correlation-ID and X-Consumer-Username.",
    "3. Transaction to Fraud & Core Ledger: Synchronous gRPC / REST with strict 200ms timeout; async Kafka event streaming for audit logs.",
    "4. Third-Party Integrations: Credit Bureau API (REST / JSON with API Key & IP Whitelist), Clearing Houses / Fedwire via ISO 20022.",
    "5. Compliance & Audit Trail: Tamper-evident immutable transaction records emitted to Kafka 'banking-audit-events' and stored in S3 WORM."
]
for idx, line in enumerate(spec_lines):
    draw.text((70, bot_y + 45 + idx * 35), line, fill=text_dark)

out_dir = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Documenting_APIs_and_Data_Flows"
img_path = os.path.join(out_dir, "API_dataflow for retail bank.png")
pdf_path = os.path.join(out_dir, "API_dataflow for retail bank.pdf")
img.save(img_path)
img.save(pdf_path, "PDF", resolution=100.0)
print(f"Generated flow image and PDF at: {img_path} and {pdf_path}")
