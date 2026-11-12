# Task 1: Process Map - Defective Part Replacement Workflow

> **Deliverable:** Task 1 (4 Points)  
> **Course:** IBM System Design - Process Modeling and Requirements Gathering  
> **Scenario:** Request Defective Auto Part Replacement  

---

## 1. Swimlane Actors & Responsibilities

| Swimlane / Actor | Primary Responsibilities |
| :--- | :--- |
| **Customer** | Initiates defective part claim; presents proof of purchase; hands over defective part; selects alternative resolution if out of stock; receives replacement part and receipt. |
| **Store Clerk** | Receives request; conducts physical/digital defect inspection; executes replacement handover or manages alternative resolutions (refund/credit/back-order); enforces warranty policies. |
| **Store & Inventory System** | Validates sales receipt/order against database; verifies return window eligibility; checks real-time inventory; generates POS replacement record; issues confirmation receipt/email. |

---

## 2. Process Flow Architecture

- **Start Event:** Customer identifies defective part purchased within warranty policy.
- **Basic Steps (Happy Path):**
  1. `S01`: Customer contacts store & requests replacement.
  2. `S02`: Customer provides receipt or order number.
  3. `S03`: Store system validates proof of purchase & warranty window.
  4. `S04`: Store clerk inspects part for manufacturing defect.
  5. `S05`: Inventory system queries stock for identical/equivalent part.
  6. `S06`: Clerk executes replacement transaction & hands over new part.
  7. `S07`: System issues replacement receipt & confirmation.
- **Decision Gateways & Alternative Flows:**
  - **Decision 1 [D1]: Purchase Validated?**
    - `Yes` $\rightarrow$ Proceed to Defect Verification (`S04`).
    - `No` $\rightarrow$ **Alternative Flow A2:** Request denied; customer informed of valid documentation requirements $\rightarrow$ **End [Unverified]**.
  - **Decision 2 [D2]: Manufacturing Defect Confirmed?**
    - `Yes` $\rightarrow$ Proceed to Inventory Check (`S05`).
    - `No (Misuse)` $\rightarrow$ **Alternative Flow A3:** Request rejected; customer reminded of policy limits regarding misuse/improper installation $\rightarrow$ **End [Misuse Rejected]**.
  - **Decision 3 [D3]: Replacement Part In Stock?**
    - `Yes` $\rightarrow$ Proceed to Replacement Issuance (`S06`).
    - `No` $\rightarrow$ **Alternative Flow A1:** System offers alternatives (Refund, Store Credit, Back-Order); clerk executes customer selection $\rightarrow$ **End [Alternative Resolution]**.
- **End Event:** Process completes with customer receiving either a replacement, refund/credit/back-order, or formal denial notice.

---

## 3. Visual Flowchart (BPMN / Swimlane Diagram)

```mermaid
flowchart TD
    subgraph Customer_Lane ["Actor: Customer"]
        C_Start([Start: Identifies Defective Part])
        C_Req[S01: Contact Store & Submit Replacement Request]
        C_Doc[S02: Provide Order Number / Receipt]
        C_A2[Receive Denial & Documentation Requirements]
        C_A3[Receive Rejection Notice & Policy Clarification]
        C_A1_Choice[A1.2: Select Option: Refund / Credit / Back-Order]
        C_ReceivePart[S06.2: Receive New Replacement Part]
        C_ReceiveConf[S07.2: Receive Confirmation & Receipt]
        C_End1([End: Denial Recorded])
        C_End2([End: Rejection Recorded])
        C_End3([End: Alternative Completed])
        C_End4([End: Replacement Completed])
    end

    subgraph Clerk_Lane ["Actor: Store Clerk"]
        K_Inspect[S04: Inspect Physical Part / Review Evidence]
        K_A2[A2.1: Deny Request: Proof of Purchase Missing]
        K_A3[A3.1: Reject Request: Signs of Misuse Detected]
        K_A1_Exec[A1.3: Process Selected Alternative Transaction]
        K_Issue[S06.1: Initiate POS Exchange & Hand Over Part]
    end

    subgraph System_Lane ["Actor: Store & Inventory System"]
        S_Val{D1: Purchase Valid & Eligible?}
        S_Eval{D2: Genuine Defect?}
        S_Inv[S05: Query Real-Time Inventory Database]
        S_Stock{D3: Part In Stock?}
        S_A1_Options[A1.1: Present Options: Refund / Store Credit / Back-Order]
        S_Receipt[S07.1: Update Stock & Generate Confirmation Receipt]
    end

    %% Wiring Flows
    C_Start --> C_Req
    C_Req --> C_Doc
    C_Doc --> S_Val

    %% D1 Decisions
    S_Val -- No --> K_A2
    K_A2 --> C_A2
    C_A2 --> C_End1

    S_Val -- Yes --> K_Inspect
    K_Inspect --> S_Eval

    %% D2 Decisions
    S_Eval -- No (Misuse) --> K_A3
    K_A3 --> C_A3
    C_A3 --> C_End2

    S_Eval -- Yes (Defect) --> S_Inv
    S_Inv --> S_Stock

    %% D3 Decisions
    S_Stock -- No (Stockout) --> S_A1_Options
    S_A1_Options --> C_A1_Choice
    C_A1_Choice --> K_A1_Exec
    K_A1_Exec --> C_End3

    S_Stock -- Yes (In Stock) --> K_Issue
    K_Issue --> C_ReceivePart
    C_ReceivePart --> S_Receipt
    S_Receipt --> C_ReceiveConf
    C_ReceiveConf --> C_End4

    %% Styling
    style C_Start fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    style C_End1 fill:#ffebee,stroke:#c62828,stroke-width:2px;
    style C_End2 fill:#ffebee,stroke:#c62828,stroke-width:2px;
    style C_End3 fill:#fff8e1,stroke:#f57f17,stroke-width:2px;
    style C_End4 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    style S_Val fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    style S_Eval fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    style S_Stock fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
```
