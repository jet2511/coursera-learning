from PIL import Image, ImageDraw, ImageFont
import os

width = 1200
height = 800
bg_color = (248, 250, 252) # light slate
image = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(image)

# Colors
primary = (30, 58, 138) # navy blue
card_bg = (255, 255, 255)
border_color = (148, 163, 184)
text_dark = (15, 23, 42)
text_muted = (71, 85, 105)
arrow_color = (37, 99, 235)
accent_green = (16, 185, 129)
accent_red = (239, 68, 68)

# Title
draw.rectangle([(0, 0), (width, 80)], fill=primary)
draw.text((40, 25), "RETAIL BANK DIGITAL CORE - DISASTER RECOVERY & RESTORATION WORKFLOW", fill=(255, 255, 255))

# Flowchart steps: 8 steps in 2 rows of 4
steps = [
    ("Step 1: Failure Detected", "Health checks fail or primary\ndatabase unreachability alert", accent_red),
    ("Step 2: Alert Triggered", "PagerDuty fires P1 alert to\nIncident Commander & SRE", primary),
    ("Step 3: Assess Impact", "Triage blast radius, verify\nreplication lag & failover criteria", primary),
    ("Step 4: Start DR Process", "Declare DR emergency;\nActivate secondary standby region", primary),
    ("Step 5: Retrieve Backups", "Point-in-Time Recovery (PITR)\nRestore WAL & S3 snapshots", primary),
    ("Step 6: Restore Systems", "Promote DB replica; Re-route\nRoute53 DNS / Ingress traffic", primary),
    ("Step 7: Validate & Test", "Run synthetic smoke tests &\nverify ledger balance integrity", accent_green),
    ("Step 8: Resume & Review", "Resume normal operations;\nConduct blameless post-mortem", accent_green),
]

# Grid coordinates
cols = 4
rows = 2
box_w = 230
box_h = 130
start_x = 50
gap_x = 70
start_y = 150
gap_y = 220

boxes = []
for i, (title, desc, color) in enumerate(steps):
    r = i // cols
    c = i % cols
    if r == 1:
        # reverse direction for snake flow
        c = (cols - 1) - c
    x1 = start_x + c * (box_w + gap_x)
    y1 = start_y + r * gap_y
    x2 = x1 + box_w
    y2 = y1 + box_h
    boxes.append((x1, y1, x2, y2, title, desc, color))

    # Draw Card
    draw.rectangle([(x1, y1), (x2, y2)], fill=card_bg, outline=color, width=3)
    # Header box inside card
    draw.rectangle([(x1, y1), (x2, y1 + 35)], fill=color)
    draw.text((x1 + 10, y1 + 10), title, fill=(255, 255, 255))
    draw.text((x1 + 12, y1 + 45), desc, fill=text_dark)

# Draw arrows between boxes
# Row 0: 0 -> 1 -> 2 -> 3
for i in range(3):
    x1, y1, x2, y2, _, _, _ = boxes[i]
    nx1, ny1, nx2, ny2, _, _, _ = boxes[i+1]
    mid_y = (y1 + y2) // 2
    draw.line([(x2, mid_y), (nx1, mid_y)], fill=arrow_color, width=4)
    draw.polygon([(nx1, mid_y), (nx1 - 10, mid_y - 6), (nx1 - 10, mid_y + 6)], fill=arrow_color)

# Turn down: 3 -> 4
_, _, bx2, by2, _, _, _ = boxes[3]
nx1, ny1, _, _, _, _, _ = boxes[4]
draw.line([(bx2 - 30, by2), (bx2 - 30, ny1)], fill=arrow_color, width=4)
draw.polygon([(bx2 - 30, ny1), (bx2 - 36, ny1 - 10), (bx2 - 24, ny1 - 10)], fill=arrow_color)

# Row 1 (backwards): 4 -> 5 -> 6 -> 7
for i in range(4, 7):
    x1, y1, x2, y2, _, _, _ = boxes[i]
    nx1, ny1, nx2, ny2, _, _, _ = boxes[i+1]
    mid_y = (y1 + y2) // 2
    draw.line([(x1, mid_y), (nx2, mid_y)], fill=arrow_color, width=4)
    draw.polygon([(nx2, mid_y), (nx2 + 10, mid_y - 6), (nx2 + 10, mid_y + 6)], fill=arrow_color)

# Legend / Footer
footer_y = 660
draw.rectangle([(50, footer_y), (1150, 750)], fill=(241, 245, 249), outline=border_color, width=1)
draw.text((70, footer_y + 15), "DISASTER RECOVERY KEY CONTROLS & COMPLIANCE:", fill=primary)
draw.text((70, footer_y + 40), "* RTO Target: < 15 Minutes | RPO Target: < 1 Minute (Zero data loss for core banking ledger)", fill=text_muted)
draw.text((70, footer_y + 60), "* Multi-Region Hot-Standby: Synchronous PostgreSQL streaming replication + Global DNS Traffic Failover", fill=text_muted)

out_dir = r"d:\Ent\Learning\Cousera\IBM System Design\11. Final Capstone Project\Module 5 - System Testing and Deployment Strategies\Lab_Designing_Backup_and_Recovery_Plans"
img_path = os.path.join(out_dir, "Retail bank_recovery workflow.png")
image.save(img_path)
print(f"Workflow image generated successfully at: {img_path}")
