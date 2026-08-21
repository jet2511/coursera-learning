# Tài liệu đọc: Các Dịch vụ AWS cho Triển khai Hybrid (AWS Services for Hybrid Deployments)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Chi tiết kỹ thuật về Amazon ECS Anywhere, Luồng xử lý tác vụ của AWS Systems Manager và Cơ chế bảo vệ dữ liệu tập trung với AWS Backup  
**Vị trí:** Module 3 - Designing a hybrid solution for container based workloads on AWS

---

## 1. Tổng quan Bộ Giải pháp Quản trị Hybrid cho Khách hàng

Để đáp ứng trọn vẹn yêu cầu **dùng chung một bộ công cụ quản lý và vận hành** trên cả Data Center On-Premises và AWS Cloud, giải pháp kiến trúc của AnyCompany Insurance tích hợp 3 dịch vụ trọng tâm:

```mermaid
flowchart TD
    HybridTooling["<b>Bộ Công Cụ Quản Trị & Vận Hành Hybrid Đồng Nhất</b>"]

    HybridTooling --> ECS_A["<b>1. Amazon ECS Anywhere</b><br/>Điều phối và quản lý vòng đời container on-premises"]
    HybridTooling --> SSM["<b>2. AWS Systems Manager</b><br/>Tự động hóa tác vụ vận hành, cấu hình và vá lỗi hạ tầng"]
    HybridTooling --> Backup["<b>3. AWS Backup</b><br/>Quản trị và thực thi chính sách sao lưu dữ liệu tập trung"]

    style HybridTooling fill:#1e293b,stroke:#f59e0b,stroke-width:2.5px,color:#f8fafc;
    style ECS_A fill:#1e293b,stroke:#4ade80,stroke-width:2px,color:#f8fafc;
    style SSM fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    style Backup fill:#1e293b,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
```

---

## 2. Amazon ECS Anywhere (Điều phối Container Hybrid)

### A. Nguyên lý & Lợi ích
* **Khái niệm:** Là tính năng mở rộng của Amazon ECS cho phép chạy và điều phối các tác vụ container trên chính hạ tầng phần cứng/máy ảo do khách hàng tự quản trị (*customer-managed infrastructure*).
* **Trải nghiệm đồng nhất:** Sử dụng chung API, cú pháp Task Definition, cluster management và monitoring tương tự như khi vận hành trên AWS Cloud.
* **Tối ưu chi phí & Tận dụng hạ tầng cũ:** Cho phép khách hàng khai thác tối đa phần cứng máy chủ On-Premises sẵn có trong thời gian chờ hết hạn hợp đồng data center, đồng thời đáp ứng các tiêu chuẩn tuân thủ pháp lý về lưu trữ dữ liệu tại chỗ.

```mermaid
flowchart LR
    subgraph ControlPlane["<b>AWS Cloud (Control Plane)</b>"]
        ECS_CP["<b>Amazon ECS Console / APIs</b><br/>(Lập lịch & Theo dõi Task)"]
    end

    subgraph OnPremNode["<b>On-Premises Infrastructure (Data Plane)</b>"]
        Agent_SSM["<b>1. SSM Agent</b><br/>(Xác thực & Kết nối an toàn)"]
        Agent_ECS["<b>2. ECS Container Agent</b><br/>(Giao tiếp với Docker Engine)"]
        Containers["<b>Application Containers</b><br/>(Chạy trên CPU/RAM On-Prem)"]
    end

    ECS_CP <===>|"Quản lý qua kết nối an toàn"| Agent_SSM
    ECS_CP ===|"Triển khai & Giám sát Task"| Agent_ECS
    Agent_ECS --> Containers

    style ControlPlane fill:#0f172a,stroke:#22c55e,stroke-width:1px,color:#f8fafc;
    style OnPremNode fill:#0f172a,stroke:#64748b,stroke-width:1px,color:#f8fafc;
    style ECS_CP fill:#1e293b,stroke:#4ade80,stroke-width:2px,color:#f8fafc;
    style Agent_SSM fill:#1e293b,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc;
    style Agent_ECS fill:#1e293b,stroke:#fbbf24,stroke-width:1.5px,color:#f8fafc;
    style Containers fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;
```

---

## 3. AWS Systems Manager - Quy trình 5 Bước Thực thi Tác vụ

AWS Systems Manager cung cấp giao diện thống nhất để xem dữ liệu vận hành và tự động hóa các tác vụ trên toàn bộ tài nguyên AWS và On-Premises.

```mermaid
flowchart TD
    S1["<b>1. Truy cập Systems Manager</b><br/>(AWS Console, AWS CLI, SDKs)"] --> S2["<b>2. Chọn Tính năng (Capability)</b><br/>(Run Command, Patch Manager, State Manager...)"]
    S2 --> S3["<b>3. Xác thực & Xử lý (Verification & Processing)</b><br/>Kiểm tra quyền IAM -> SSM Agent trên Node thực thi"]
    S3 --> S4["<b>4. Báo cáo Trạng thái (Reporting)</b><br/>Gửi trạng thái thành công/thất bại về SSM và EventBridge"]
    S4 --> S5["<b>5. Quản trị Vận hành (Operations Management)</b><br/>Tổng hợp OpsData, tạo OpsItems và kích hoạt tự động xử lý"]

    style S1 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    style S2 fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;
    style S3 fill:#1e293b,stroke:#fbbf24,stroke-width:2px,color:#f8fafc;
    style S4 fill:#1e293b,stroke:#4ade80,stroke-width:1.5px,color:#f8fafc;
    style S5 fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
```

### Chi tiết từng bước:
1. **Access Systems Manager:** Quản trị viên khởi tạo tác vụ qua Console hoặc câu lệnh CLI/SDK.
2. **Choose a Capability:** Lựa chọn công cụ phù hợp với mục đích (ví dụ: *Run Command* để chạy script, *Patch Manager* để vá lỗi, *Maintenance Windows* để lên lịch).
3. **Verification & Processing:** 
   * SSM tự động kiểm tra chính sách quyền IAM của người dùng/role.
   * Nếu đích là **Managed Node** (EC2 hoặc On-Premises VM), **SSM Agent** cài trên máy sẽ trực tiếp thực thi tác vụ.
   * Nếu là tài nguyên khác (S3, RDS), Systems Manager sẽ trực tiếp gọi API của dịch vụ đó.
4. **Reporting:** SSM Agent và các dịch vụ liên quan báo cáo chi tiết kết quả thực thi về Systems Manager dashboard.
5. **Operations Management:** Các công cụ *Explorer, OpsCenter, Incident Manager* tổng hợp dữ liệu, tự động tạo sự cố (**OpsItems**) và kích hoạt quy trình khắc phục tự động (*Automated Remediation*).

---

## 4. AWS Backup - Bảo vệ Dữ liệu Tập trung theo Chính sách

AWS Backup là dịch vụ quản lý toàn phần (*fully managed*), tự động hóa và tập trung hóa việc sao lưu dữ liệu trên quy mô lớn (*policy-based data protection*).

```mermaid
flowchart LR
    subgraph Org["<b>Quản Trị Tập Trung (AWS Organizations)</b>"]
        Policy["<b>Chính Sách Sao Lưu (Backup Policies)</b><br/>- Tần suất: Hàng ngày 01:00 AM<br/>- Thời gian lưu trữ: 90 ngày<br/>- Mã hóa: AWS KMS"]
    end

    subgraph Targets["<b>Phạm Vi Tài Nguyên Hỗ Trợ (Hybrid & Cloud)</b>"]
        direction TB
        HybridWorkloads["<b>1. Hybrid Workloads</b><br/>VMware ESXi on-prem, AWS Outposts, Storage Gateway"]
        ComputeStorage["<b>2. Compute & Storage</b><br/>Amazon EC2 (VSS Windows), EBS, S3, EFS, FSx"]
        Databases["<b>3. Managed Databases</b><br/>Amazon RDS (PostgreSQL/Aurora), DynamoDB, DocumentDB"]
    end

    Policy ===|"Tự động áp dụng & Thực thi"| Targets

    style Org fill:#0f172a,stroke:#f59e0b,stroke-width:1px,color:#f8fafc;
    style Targets fill:#0f172a,stroke:#22c55e,stroke-width:1px,color:#f8fafc;
    style Policy fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#f8fafc;
    style HybridWorkloads fill:#1e293b,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc;
    style ComputeStorage fill:#1e293b,stroke:#4ade80,stroke-width:1.5px,color:#f8fafc;
    style Databases fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;
```

### Danh mục các tài nguyên được AWS Backup hỗ trợ:

| Nhóm tài nguyên | Danh sách dịch vụ hỗ trợ |
| :--- | :--- |
| **Môi trường Hybrid** | Máy ảo **VMware** (On-Premises, Amazon Outposts, VMware Cloud on AWS), **AWS Storage Gateway volumes**. |
| **Tính toán & Máy chủ** | **Amazon EC2 instances**, các ứng dụng hỗ trợ Windows VSS (*Windows Server, Microsoft SQL Server, Exchange Server*). |
| **Lưu trữ Tệp & Khối** | **Amazon EBS**, **Amazon S3**, **Amazon EFS**, **Amazon FSx** (*ONTAP, Lustre, Windows File Server, OpenZFS*). |
| **Cơ sở Dữ liệu Quản lý** | **Amazon RDS** (bao gồm cụm Aurora), **Amazon DynamoDB**, **Amazon Neptune**, **Amazon DocumentDB**. |

---

## 5. Tổng kết Lựa chọn Kiến trúc cho AnyCompany Insurance

| Nhu cầu của Khách hàng | Giải pháp Kiến trúc AWS | Giá trị Đem lại |
| :--- | :--- | :--- |
| **Quản trị Container Hybrid** | **Amazon ECS Anywhere** | Dùng chung 1 giao diện điều phối container trên cả AWS và on-premise, không cần học công cụ mới. |
| **Tự động hóa Vận hành** | **AWS Systems Manager** | Quản trị tập trung, chạy lệnh Run Command không cần SSH, lên lịch vá lỗi OS qua Maintenance Windows. |
| **Bảo vệ Dữ liệu Doanh nghiệp** | **AWS Backup** | Áp dụng chính sách sao lưu tự động cho VMware on-premise, Storage Gateway và RDS PostgreSQL. |
