# Walkthrough Question 4.1: Shared File Storage for Windows & On-Premises Active Directory

## 1. Nội dung câu hỏi (Question Stem)
Một cơ sở xử lý dữ liệu muốn chuyển một nhóm **Microsoft Windows servers** lên AWS Cloud. 
Các server này cần truy cập vào một **shared file system** có khả năng tích hợp với hạ tầng **Active Directory** sẵn có tại cơ sở để phân quyền file và folder. 
Giải pháp cần hỗ trợ chia sẻ file liền mạch giữa **AWS và on-premises servers**, có tính sẵn sàng cao (**Highly Available**), đồng thời đảm bảo bảo mật bằng cách hỗ trợ **mã hóa khi lưu trữ (at rest) và khi truyền tải (in transit)**.

**Giải pháp lưu trữ nào đáp ứng các yêu cầu trên?**

---

## 2. Phân tích từ khóa (Keywords & Clues)
- **Microsoft Windows servers:** Loại hệ điều hành $\to$ Hướng tới dịch vụ tương thích chuẩn Windows (SMB protocol).
- **Shared file system:** Hệ thống file dùng chung cho nhiều server.
- **Tích hợp Active Directory & phân quyền file/folder:** Yêu cầu hỗ trợ ACLs (Access Control Lists) và Kerberos authentication chuẩn Microsoft AD.
- **Chia sẻ liền mạch AWS & On-premises:** Hỗ trợ hybrid access.
- **High Availability (HA):** Triển khai Multi-AZ.
- **Mã hóa (At rest & In transit):** Tính năng bảo mật tích hợp.

---

## 3. Lựa chọn đáp án & Phân tích chi tiết

### Các lựa chọn:
- **A.** AWS S3 File Gateway được join vào domain Active Directory hiện tại.
- **B. (Đúng) Amazon FSx for Windows File Server file system được join vào domain Active Directory hiện tại.**
- **C.** Amazon Elastic File System (EFS) file system được join vào AWS Managed Active Directory domain.
- **D.** Amazon S3 bucket được mount lên các EC2 instance Windows servers chạy trên nhiều Availability Zones.

---

### Giải thích chi tiết:

| Lựa chọn | Đánh giá | Lý do |
| :--- | :---: | :--- |
| **B. Amazon FSx for Windows File Server** | **ĐÚNG** | - Được xây dựng native trên nền Windows Server, hỗ trợ đầy đủ giao thức **SMB**, tích hợp **Active Directory** (bao gồm On-premises AD và AWS Managed AD).<br>- Hỗ trợ phân quyền thư mục chi tiết (NTFS ACLs), tính năng Multi-AZ cho HA.<br>- Hỗ trợ mã hóa dữ liệu at rest (AWS KMS) và in transit (SMB encryption).<br>- Cho phép truy cập liền mạch từ cả AWS EC2 và On-premises qua VPN / Direct Connect. |
| **A. AWS S3 File Gateway** | **SAI** | S3 File Gateway có thể xác thực với AD ở phía On-premises, nhưng bản chất dữ liệu lưu trữ trên S3 là Object Storage, không giữ được đầy đủ phân quyền bảo mật file/folder (NTFS ACLs) native khi lưu trên S3. |
| **C. Amazon EFS** | **SAI** | Amazon EFS là giải pháp file system quản lý dựa trên giao thức NFS dành riêng cho **Linux-based workloads**, không hỗ trợ native cho Windows servers. |
| **D. Mount Amazon S3 lên EC2** | **SAI** | S3 là Object Storage, không phải là Network File System được thiết kế để mount trực tiếp làm shared file system cho Windows servers. |

---

## 4. Key Exam Takeaways
1. **Windows + Shared File Storage + Active Directory / SMB $\to$ Amazon FSx for Windows File Server.**
2. **Linux + Shared File Storage + NFS $\to$ Amazon EFS.**
3. **S3 File Gateway vs FSx:** Khi đề bài nhấn mạnh đến việc giữ nguyên cơ chế phân quyền bảo mật thư mục chuẩn Windows (*file and folder permissions / NTFS permissions*) với Active Directory $\to$ Luôn chọn **FSx for Windows File Server**.
