# Final Project Implementation Plan: Defective Part Replacement Workflow

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create production-ready submission deliverables for Coursera Final Project (Task 1: Process Map, Task 2: Process Narrative, Task 3: Reflection) for the auto part replacement use case, including visual assets and complete documentation.

**Architecture:** Decompose the assignment into 3 isolated deliverable tasks matching the grading rubric (4 pts, 4 pts, 2 pts). Output clean Markdown, SVG/Mermaid diagrams, and CSV/table data ready for direct export into PDF/DOCX templates.

**Tech Stack:** Markdown, Mermaid.js / SVG, CSV, PowerShell.

---

## Deliverables & File Structure

Target Directory: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\`

- **Task 1 Artifacts:**
  - `result/Task1_ProcessMap.md` (Detailed swimlane architecture, Mermaid diagrams, layout specifications)
  - `result/Task1_ProcessMap.svg` (Standalone high-res SVG process map for direct inclusion in submission PDF/Docx)
- **Task 2 Artifacts:**
  - `result/Task2_ProcessNarrative.md` (Formal 7-column tabular narrative)
  - `result/Task2_ProcessNarrative.csv` (Spreadsheet-importable data for Excel/Google Sheets)
- **Task 3 Artifacts:**
  - `result/Task3_Reflection.md` (Comprehensive 3-prompt academic reflection with concrete enterprise examples)
- **Master Summary Artifact:**
  - `result/Final_Project_Complete_Submission.md` (Consolidated submission bundle ready to print to PDF)

---

### Task 1: Generate Visual Process Map (Task 1 - 4 Points)

**Files:**
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Task1_ProcessMap.md`
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Task1_ProcessMap.svg`

- [ ] **Step 1: Write Task 1 Process Map markdown file**
  - Define 3 clear swimlanes: `Customer`, `Store Clerk`, `Store & Inventory System`.
  - Model Start event, 6 basic flow steps, and 3 explicit Decision Gateways:
    1. Decision: Proof of Purchase Valid? (No -> A2 Deny).
    2. Decision: Defect Manufacturing Related? (No -> A3 Reject).
    3. Decision: Part In Stock? (No -> A1 Refund/Store Credit/Back-order).
  - Include end states for all branches.

- [ ] **Step 2: Generate standalone SVG vector graphic**
  - Render or generate clean SVG diagram with distinct swimlane colors, decision diamonds, process rectangles, and terminal rounded capsules.

- [ ] **Step 3: Verification of Task 1**
  - Verify all 3 alternative flows (A1, A2, A3) and basic flow steps exist and are correctly labeled.

---

### Task 2: Generate Process Narrative Table & CSV (Task 2 - 4 Points)

**Files:**
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Task2_ProcessNarrative.md`
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Task2_ProcessNarrative.csv`

- [ ] **Step 1: Construct complete 7-column Narrative table**
  - Columns: `Step ID`, `Description`, `Actor`, `Trigger`, `Inputs`, `Outputs`, `Notes / Alternative Paths`.
  - Include S01 through S07 covering Happy Path + explicit sub-steps for A1, A2, A3 handling.
  - Ensure zero placeholder text; provide complete production descriptions.

- [ ] **Step 2: Export CSV version for spreadsheet template import**
  - Format as standard UTF-8 CSV with quoted strings for easy import into Microsoft Excel / Google Sheets template.

- [ ] **Step 3: Verification of Task 2**
  - Check 1-to-1 alignment between Task 1 Step IDs and Task 2 rows.

---

### Task 3: Author Critical Reflection (Task 3 - 2 Points)

**Files:**
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Task3_Reflection.md`

- [ ] **Step 1: Write structured response for Prompt 1 (Key Learnings)**
  - Value of swimlanes, distinction between happy path and exception boundaries, importance of mapping inputs/outputs.

- [ ] **Step 2: Write structured response for Prompt 2 (Challenges Encountered)**
  - Delineating human vs system responsibilities, managing visual complexity of 3 alternative paths.

- [ ] **Step 3: Write structured response for Prompt 3 (Validation & Improvement in Practice)**
  - Operational Gemba walks/walkthroughs, process mining logs, continuous feedback loops (Kaizen/PDCA).

- [ ] **Step 4: Verification of Task 3**
  - Ensure academic depth, professional tone, and alignment with course rubric.

---

### Task 4: Compile Consolidated Master Submission Package

**Files:**
- Create: `d:\Ent\Learning\Cousera\IBM System Design\04. Process Modeling and Requirements Gathering\Module 5 - Final Project, Final Quiz, and Course Wrap-Up\result\Final_Project_Complete_Submission.md`

- [ ] **Step 1: Merge Task 1, 2, and 3 into single cohesive submission document**
- [ ] **Step 2: Add submission checklist and instructions for converting to PDF**
- [ ] **Step 3: Final file integrity check across the `result/` folder**
