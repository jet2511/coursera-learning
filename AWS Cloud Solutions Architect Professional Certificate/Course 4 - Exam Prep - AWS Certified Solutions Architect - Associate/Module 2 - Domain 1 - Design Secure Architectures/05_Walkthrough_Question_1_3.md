# Walkthrough Question 1.3: Secure Cryptographic Key Management

## 1. Đề bài & Phân tích Yêu cầu (Stem & Requirements)

### Đề bài (Stem)
> **A company needs to implement a secure data encryption solution to meet regulatory requirements. The solution must provide security and durability in generating, storing, and controlling cryptographic data keys. Which action should be taken to provide the MOST secure solution?**
>
> *(Một công ty cần triển khai giải pháp mã hóa dữ liệu an toàn để đáp ứng các yêu cầu tuân thủ pháp lý. Giải pháp phải đảm bảo tính bảo mật và độ bền vững (durability) trong việc tạo, lưu trữ và kiểm soát các khóa mã hóa dữ liệu (cryptographic data keys). Hành động nào sau đây mang lại giải pháp an toàn nhất?)*

### Phân tích Từ khóa (Keywords)
- `Regulatory requirements`: Yêu cầu tuân thủ quy chuẩn bảo mật (FIPS compliant HSMs).
- `Security and durability`: Đảm bảo an toàn cao, không bị mất mát dữ liệu khóa.
- `Generating, storing, and controlling data keys`: Vòng đời hoàn chỉnh của khóa (tạo, lưu trữ, phân quyền).
- `MOST secure solution`: Giải pháp bảo mật tối ưu và chuẩn best practice của AWS.

---

## 2. Các Lựa chọn (Options)

- **A.** **[CORRECT]** *Use AWS KMS to generate AWS KMS keys and data keys. Use KMS key policies to control access to the AWS KMS keys.*
- **B.** *Use AWS KMS to generate cryptographic keys and import the keys to AWS Certificate Manager. Use IAM policies to control access to the keys.*
- **C.** *Use a third-party solution from AWS Marketplace to generate the cryptographic keys and store them on an encrypted instance store volume. Use IAM policies to control access to the encryption key APIs.*
- **D.** *Use OpenSSL to generate the cryptographic keys and upload the keys to an Amazon S3 bucket with encryption activated. Apply AWS Key Management Service key policies to control access to the keys.*

---

## 3. Giải thích Đáp án & Phân tích Nhiễu (Explanation & Distractor Analysis)

### Đáp án Đúng
- **A (AWS KMS + Key Policies):**
  - AWS Key Management Service (KMS) sử dụng Hardware Security Modules (HSMs) đạt chuẩn **FIPS 140-2 Level 2/3** để tạo và bảo vệ khóa an toàn.
  - Hỗ trợ cơ chế **Envelope Encryption** (tạo Root KMS Keys và Data Encryption Keys).
  - Tích hợp kiểm soát quyền truy cập chi tiết cấp cao nhất thông qua **KMS Key Policies** và ghi vết đầy đủ vào **AWS CloudTrail**.
  - Dữ liệu khóa được nhân bản trên nhiều Availability Zones đảm bảo tính **durability** tối đa.

### Phân tích Đáp án Gây nhiễu (Distractors)
- **B SAI:** **AWS Certificate Manager (ACM)** chuyên dùng để cấp phát, quản lý và lưu trữ **chứng chỉ SSL/TLS X.509**, không phải là dịch vụ lưu trữ Data Encryption Keys cho mã hóa dữ liệu chung.
- **C SAI:** **Instance Store Volume** có tính chất **Ephemeral (tạm thời)**; dữ liệu sẽ bị mất hoàn toàn khi EC2 instance bị Stop, Terminate hoặc gặp sự cố phần cứng $\rightarrow$ Vi phạm nghiêm trọng yêu cầu về **durability**.
- **D SAI:** S3 không phải là hệ thống quản trị vòng đời khóa chuyên dụng. Hơn nữa, **KMS Key Policies** chỉ có thể áp dụng cho các khóa được quản trị trực tiếp bên trong AWS KMS, không thể áp dụng cho file khóa tải lên S3.

---

## 4. Bảng So sánh & Điểm thi Cần nhớ (Exam Takeaways)

| Thành phần | AWS KMS | AWS CloudHSM | Instance Store | ACM |
| :--- | :--- | :--- | :--- | :--- |
| **Mục đích chính** | Quản lý Root Keys & Data Keys tập trung cho toàn bộ dịch vụ AWS | Quản lý Dedicated HSM riêng biệt trong VPC | Ổ đĩa gắn trực tiếp tốc độ cao, tạm thời (Ephemeral) | Quản lý và gia hạn SSL/TLS Certificate |
| **Cơ chế Phân quyền** | **KMS Key Policy** (Bắt buộc) + IAM Policy | HSM Users / Crypto Officers | IAM Policy / OS Permissions | IAM Policy |
| **Độ bền (Durability)** | **High (99.999999999%)** | Khách hàng tự cấu hình Cluster | **Không đảm bảo (Mất khi stop)** | High |

