# Task 2: Multi-Layered Security Architecture Diagram

Sơ đồ kiến trúc an ninh bảo mật đa tầng trực quan mô phỏng mô hình **Defense-in-Depth** và **Zero-Trust** bảo vệ toàn diện hệ thống Retail Bank.

---

## 1. Biểu đồ Kiến trúc An ninh Đa tầng (Mermaid Security Architecture Diagram)

```mermaid
graph TB
    %% Users / Actors
    User(["👤 External Customers<br/>(Web / Mobile)"]):::actorNode
    Staff(["👤 Internal Bank Staff<br/>(Workstations)"]):::actorNode

    %% ------------------------------------------------------------------------
    %% LAYER 1: NETWORK SECURITY LAYER (PERIMETER & SEGMENTATION)
    %% ------------------------------------------------------------------------
    subgraph L1 ["<b>TẦNG 1: NETWORK SECURITY LAYER (Perimeter Defense & Segmentation)</b>"]
        direction TB
        ExtFW["🛡️ Perimeter Firewall (Packet Filtering & Anti-DDoS)"]:::netNode
        WAF["🛡️ Web Application Firewall (WAF)"]:::netNode
        SASE["☁️ SASE Cloud Edge / VPN Gateway"]:::netNode
        DMZ["🌐 Demilitarized Zone (DMZ - Reverse Proxy / Ingress)"]:::dmzNode
        IntFW["🛡️ Internal Stateful Inspection Firewall"]:::netNode
        
        ExtFW --> WAF
        SASE --> IntFW
        WAF --> DMZ
        DMZ --> IntFW
    end

    %% ------------------------------------------------------------------------
    %% LAYER 2: APPLICATION SECURITY LAYER (DEVSECOPS & RUNTIME)
    %% ------------------------------------------------------------------------
    subgraph L2 ["<b>TẦNG 2: APPLICATION SECURITY LAYER (DevSecOps & Runtime Protection)</b>"]
        direction TB
        DevSecOps["⚙️ DevSecOps Pipeline<br/>(SAST SonarQube | DAST ZAP | Secret Scan Trivy)"]:::appSecNode
        APIGW["🚪 Secure API Gateway (OAuth2/OIDC | Rate Limiting | TLS Term)"]:::appCoreNode
        Microservices["🧩 Microservices Internal Zone<br/>(Onboarding | Loans | Core Transfers | RASP Protected)"]:::appCoreNode
        
        DevSecOps -.->|"Scanned & Verified Deploy"| Microservices
        APIGW -->|"mTLS / Zero-Trust East-West"| Microservices
    end

    %% ------------------------------------------------------------------------
    %% LAYER 3: DATA SECURITY LAYER (ENCRYPTION & GOVERNANCE)
    %% ------------------------------------------------------------------------
    subgraph L3 ["<b>TẦNG 3: DATA SECURITY LAYER (Encryption & Governance)</b>"]
        direction TB
        DataGov["📜 Data Discovery, Classification & Governance Engine"]:::dataGovNode
        KMS["🔑 Hardware Security Module (AWS KMS / CloudHSM - AES-256)"]:::dataSecNode
        DataStores["🗄️ Protected Databases & Sensitive Data Zones<br/>- Core Ledger (TDE Encrypted)<br/>- PCI-DSS Card Vault (Tokenized)<br/>- KYC & AML Audit Logs"]:::dataSecNode
        
        DataGov -.->|"Policy Enforcement"| DataStores
        KMS <-->|"Key Management & Envelope Encryption"| DataStores
    end

    %% ------------------------------------------------------------------------
    %% LAYER 4: MONITORING & INCIDENT RESPONSE LAYER (SIEM & SOC)
    %% ------------------------------------------------------------------------
    subgraph L4 ["<b>TẦNG 4: MONITORING & RESPONSE LAYER (SIEM, DLP & SOC Operations)</b>"]
        direction LR
        SIEM["📊 Central SIEM & Audit Aggregator<br/>(Splunk / QRadar)"]:::monNode
        DLP["🔍 Data Loss Prevention (DLP Engine)"]:::monNode
        SOC["🚨 SOC 24/7 Incident Response Workflow<br/>(Alerts ➔ Analyst Triage ➔ Auto Containment)"]:::monNode

        SIEM --> SOC
        DLP --> SOC
    end

    %% Central IAM Cross-cutting Layer
    IAM["🔐 Central IAM & Identity Provider (Azure AD / MFA / RBAC / PAM)"]:::iamNode

    %% Inter-layer Traffic Connections (North-South Flow)
    User -->|"North-South Traffic (HTTPS / TLS 1.3)"| ExtFW
    Staff -->|"Zero-Trust Secure Access"| SASE
    IntFW -->|"Sanitized Traffic"| APIGW
    Microservices -->|"Encrypted Queries & Tokenized Calls"| DataStores
    
    %% IAM Cross-layer Authorization
    IAM -.->|"Verify Token & Claims"| APIGW
    IAM -.->|"Access Control & RBAC"| DataStores
    IAM -.->|"Privileged Access PAM"| Staff

    %% Telemetry & Log Shipping to Monitoring (All Layers -> SIEM)
    L1 -.->|"Network NetFlow / Firewall Logs"| SIEM
    L2 -.->|"API & App Access Audit Logs"| SIEM
    L3 -.->|"DB Query & Decryption Audit Trails"| SIEM
    L3 -.->|"Egress Content Inspection"| DLP

    %% Style Classes
    classDef actorNode fill:#fff8e1,stroke:#f57f17,stroke-width:2px,color:#212121;
    classDef netNode fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#263238;
    classDef dmzNode fill:#cfd8dc,stroke:#37474f,stroke-width:2px,stroke-dasharray: 4 4,color:#212121;
    classDef appCoreNode fill:#0d47a1,stroke:#082a63,stroke-width:2px,color:#ffffff;
    classDef appSecNode fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e;
    classDef dataSecNode fill:#ede7f6,stroke:#512da8,stroke-width:2px,color:#311b92;
    classDef dataGovNode fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1.5px,stroke-dasharray: 4 4,color:#4a148c;
    classDef monNode fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#b71c1c;
    classDef iamNode fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c;
```

---

## 2. Hướng dẫn xuất tệp bàn giao (Deliverable)
- **Tên tệp yêu cầu:** `security_architecture_diagram.pdf` (hoặc `.png`).
- Khi vẽ trên Lucidchart / Draw.io / PowerPoint:
  1. Vẽ 4 khối hộp hình chữ nhật nằm ngang (Horizontal Swimlanes) theo thứ tự từ trên xuống dưới:
     - Tầng 1: `Network Security Layer` (trên cùng tiếp nhận traffic bên ngoài).
     - Tầng 2: `Application Security Layer` (ở giữa xử lý nghiệp vụ).
     - Tầng 3: `Data Security Layer` (tầng lõi bảo vệ dữ liệu).
     - Tầng 4: `Monitoring & Response Layer` (chân đế tiếp nhận log từ 3 tầng trên).
  2. Bố trí khối `Identity & Access Management (IAM)` ở cột bên cạnh thể hiện tính chất cắt ngang (cross-cutting) kiểm soát tất cả các tầng.
  3. Sử dụng các đường mũi tên liền cho luồng nghiệp vụ (North-South Traffic) và đường mũi tên nét đứt cho luồng đẩy Log về SIEM/DLP.
