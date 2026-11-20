# LAB DELIVERABLES: Creating an Infrastructure Inventory
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Core Digital Transformation for Retail Banking  
**Vai trò:** Systems and Solutions Architect  
**Mục tiêu:** Xây dựng tài liệu kiểm kê hạ tầng CNTT toàn diện (Hardware, Software, Network) phân loại theo môi trường (Dev, Staging, Production), xác định quyền sở hữu (Ownership), tình trạng giấy phép (Licensing), chu kỳ cập nhật bản vá (Patching) và ma trận phụ thuộc (Dependencies) phục vụ quản trị và kiểm toán ngân hàng.  

---

# TASK 1: HARDWARE INVENTORY (BẢNG KIỂM KÊ PHẦN CỨNG)

Bảng thống kê các tài sản phần cứng (máy chủ vật lý, thiết bị cân bằng tải, tủ lưu trữ SAN) phục vụ các hệ thống lõi:

| Asset Name | Type | Environment | Manufacturer | Model | Purpose | Shared (Yes/No) | Owner | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **Prod-App-Server-1** | Server | Production | Dell | PowerEdge R750 | Application hosting (Core Microservices Node 1) | No | Infra Team | Cụm máy chủ chạy K8s Worker Nodes |
| **Prod-App-Server-2** | Server | Production | Dell | PowerEdge R750 | Application hosting (Core Microservices Node 2) | No | Infra Team | Dự phòng nóng N+1 cho Prod-App-Server-1 |
| **Prod-DB-Server-1** | Server | Production | HPE | ProLiant DL380 Gen10 | Primary Database Cluster | No | Database Team | Chạy MySQL Cluster (Master) với ổ cứng NVMe |
| **Prod-DB-Server-2** | Server | Production | HPE | ProLiant DL380 Gen10 | Standby Database Cluster | No | Database Team | Replication đồng bộ (Slave/Read-replica) |
| **LB-01** | Load Balancer | Production | F5 Networks | BIG-IP i5800 | Traffic routing & SSL Termination | Yes | Network Team | Hoạt động theo cặp High-Availability (Active-Standby) |
| **SAN-Storage-01** | Storage (SAN) | Production | NetApp | AFF A400 | Enterprise Data Persistence & Backups | Yes | Storage Team | Cung cấp block storage tốc độ cao cho Database |
| **Stg-K8s-Node-01** | Server (VM) | Staging | VMware ESXi | ProLiant DL360 | Staging Integration Testing | No | QA/DevOps | Giả lập môi trường Production cho kiểm thử tải |
| **Dev-Server-Pool** | Server (Blade) | Development | Cisco | UCS B200 M5 | Development Sandbox & CI/CD Builds | Yes | DevOps Team | Phân vùng tài nguyên qua OpenShift Dev Cluster |

---

# TASK 2: SOFTWARE INVENTORY (BẢNG KIỂM KÊ PHẦN MỀM)

Bảng thống kê hệ điều hành, hệ quản trị CSDL, phần mềm trung gian và công cụ DevOps:

| Software Name | Type | Version | Environment | License | Owner | Installed on | Shared (Yes/No) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **Red Hat Enterprise Linux (RHEL)** | Operating System | 9.2 | Production | Commercial Subscription | Infra Team | Prod-App-Server-1, 2 | Yes | Đạt chuẩn an ninh CIS Benchmark Level 2 |
| **Ubuntu Server** | Operating System | 22.04 LTS | Dev / Staging | Open Source | DevOps Team | Dev-Server-Pool, Stg-K8s | Yes | Cập nhật bản vá bảo mật hàng tuần |
| **MySQL Enterprise Edition** | DBMS (Relational) | 8.0.35 | Production | Commercial (Oracle) | DB Team | Prod-DB-Server-1, 2 | Yes | Hỗ trợ mã hóa TDE (Transparent Data Encryption) |
| **PostgreSQL** | DBMS | 15.4 | Staging / Dev | Open Source (PostgreSQL) | DB Team | Stg-K8s-Node-01 | Yes | Phục vụ lưu trữ dịch vụ phụ trợ và PoC |
| **Apache Kafka** | Middleware / Event Broker | 3.5.1 | All (Dev, Stg, Prod) | Open Source (Apache 2.0) | Architecture Team | Dedicated Cluster | Yes | Xương sống cho kiến trúc hướng sự kiện (EDA) |
| **Docker Engine** | Container Runtime | 24.0.7 | All | Open Source (Community) | DevOps Team | All Worker Nodes | Yes | Đóng gói và chạy các microservices ngân hàng |
| **Kubernetes (OpenShift)** | Container Orchestration | 4.14 | Production | Commercial (Red Hat) | DevOps Team | Prod App Cluster | Yes | Tự động co giãn (HPA) và tự phục hồi (Self-healing) |
| **Jenkins** | CI/CD Automation | 2.426 LTS | Dev / Staging | Open Source (MIT) | DevOps Team | Dev-Server-Pool | Yes | Điều phối pipeline build, test, scan CVE và deploy |
| **HashiCorp Vault** | Secret Management | 1.15 | Production | Commercial Enterprise | SecOps Team | Security Cluster | Yes | Quản lý khóa mã hóa và token tập trung |

---

# TASK 3: NETWORK COMPONENTS (BẢNG KIỂM KÊ THIẾT BỊ MẠNG)

Bảng ghi nhận cấu hình tường lửa, VPN, định tuyến và phân đoạn mạng ảo:

| Component Name | Type | IP Range | Role | Vendor | Version / Model | Environment | Owner | Shared (Yes/No) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **FW-GW-01** | Perimeter Firewall / WAF | 10.0.0.0/24 | Perimeter Defense | Palo Alto | PA-5220 (PAN-OS 10.2) | Production | SecOps | No | Chặn tấn công DDoS, lọc Geo-blocking, WAF cho API |
| **Internal-FW-02** | Internal Core Firewall | 10.10.0.0/16 | Network Segmentation | Fortinet | FortiGate 600E | All | NetOps | Yes | Phân tách ranh giới DMZ, Private App và Secure DB |
| **VPN-Gateway** | VPN Server | 172.16.0.0/16 | Remote Secure Access | Cisco | ASA 5545-X (v8.4) | All | NetOps | Yes | Xác thực 2FA/MFA cho kỹ sư vận hành và quản trị |
| **Core-Switch-01** | Core Switch | 10.10.1.0/24 | High-Speed Backbone | Cisco | Catalyst 9500 | Production | NetOps | Yes | Cặp đôi dự phòng công nghệ VSS (Virtual Switching System) |
| **Cloud-Direct-Link** | Dedicated Network Link | 192.168.100.0/29 | Hybrid Cloud Interconnect | IBM Cloud / AWS | Direct Connect 10Gbps | Production | NetOps | Yes | Kết nối mạng riêng tốc độ cao giữa Data Center & Cloud VPC |
| **Enterprise-DNS** | DNS Resolver | 10.10.0.10, .11 | Internal Name Resolution | Infoblox | NIOS 8.6 | All | NetOps | Yes | Định giải tên miền nội bộ và dịch vụ vi mô nội bộ |

---

# TASK 4: CATEGORIZE BY ENVIRONMENT (PHÂN LOẠI THEO MÔI TRƯỜNG)

Bảng phân vùng tài nguyên rạch ròi giữa 3 môi trường phát triển và chỉ rõ các dịch vụ dùng chung (Shared Services):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          SHARED ENTERPRISE SERVICES (DÙNG CHUNG)                       │
│  • Enterprise-DNS (Infoblox)       • VPN-Gateway (Cisco ASA - Remote Access MFA)       │
│  • Jenkins CI/CD Controller        • HashiCorp Vault (Centralized Secrets)             │
│  • Nexus Artifact Registry         • NTP Servers (Đồng bộ thời gian chuẩn xác thực)   │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌─────────────────────────┐       ┌─────────────────────────┐       ┌─────────────────────────┐
│       DEVELOPMENT       │       │         STAGING         │       │       PRODUCTION        │
├─────────────────────────┤       ├─────────────────────────┤       ├─────────────────────────┤
│ • Dev-Server-Pool       │       │ • Stg-K8s-Node-01       │       │ • Prod-App-Server-1, 2  │
│ • Ubuntu 22.04 LTS      │       │ • PostgreSQL 15.4       │       │ • Prod-DB-Server-1, 2   │
│ • Docker Community      │       │ • Pre-prod Kafka Topic  │       │ • F5 LB-01 (HA Pair)    │
│ • Sandbox Databases     │       │ • Palo Alto Stg Policy  │       │ • NetApp SAN-Storage-01 │
│ • Cập nhật hàng ngày    │       │ • Môi trường UAT & Tải  │       │ • RHEL 9.2 & OpenShift  │
│                         │       │ • Cập nhật theo Sprint  │       │ • MySQL Enterprise 8.0  │
│                         │       │                         │       │ • Palo Alto FW-GW-01    │
│                         │       │                         │       │ • Cloud-Direct-Link     │
│                         │       │                         │       │ • Khóa thay đổi chặt chẽ│
└─────────────────────────┘       └─────────────────────────┘       └─────────────────────────┘
```

---

# TASK 5: DOCUMENT OWNERSHIP AND COMPLIANCE (QUẢN TRỊ & TUÂN THỦ)

Bảng theo dõi quyền sở hữu, tình trạng bản quyền, lịch cập nhật bản vá bảo mật và ma trận phụ thuộc:

| Asset / Component Name | Responsible Owner (Đội ngũ sở hữu) | License Status | Last Patch Date | Dependencies (Các hệ thống phụ thuộc) | Audit & Compliance Notes |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Prod-App-Server-1 & 2** | Infrastructure Team (Lead: David Tran) | Active Commercial (Dell ProSupport) | 01/11/2026 | Hạ tầng nền tảng cho 82 Pods microservices ngân hàng | Đạt chứng nhận chuẩn bảo mật trung tâm dữ liệu ISO 27001 |
| **MySQL Enterprise 8.0** | Database Operations Team (Lead: Lan Nguyen) | Commercial Subscription (Oracle SLA 24/7) | 15/10/2026 | Dùng chung cho: `auth-service`, `loan-service`, `onboarding-service` | Kích hoạt mã hóa trong suốt TDE, đáp ứng chuẩn PCI-DSS Mục 3.4 |
| **Apache Kafka Cluster** | Architecture & Integration Team (Arjun Desai) | Open Source (Apache 2.0 Compliance) | 20/10/2026 | Phụ thuộc bởi: Transaction Engine, Fraud AI Engine, Push Notification Service | Nhật ký thông điệp mã hóa TLS 1.3, đạt chuẩn RBI Real-time Tracking |
| **FW-GW-01 (Palo Alto)** | Cyber Security Operations (CISO Team) | Commercial License & Threat Prevention Sub | 05/11/2026 | Bảo vệ cổng vào toàn bộ hệ thống Web/Mobile Banking | Kiểm toán chính sách tường lửa 3 tháng/lần, 0 lỗ hổng Critical |
| **HashiCorp Vault** | Security & Compliance Team | Commercial Enterprise | 12/10/2026 | Toàn bộ microservices và database pool kết nối lấy secrets | Cơ chế tự động xoay vòng khóa (Key Rotation) định kỳ 90 ngày |
| **SAN-Storage-01** | Storage & Backup Operations Team | Commercial (NetApp Support) | 28/09/2026 | Nơi lưu trữ vật lý của MySQL Datafiles và Backup Dumps | Áp dụng chính sách lưu trữ bất biến (WORM) lưu dữ liệu kiểm toán 7 năm |
