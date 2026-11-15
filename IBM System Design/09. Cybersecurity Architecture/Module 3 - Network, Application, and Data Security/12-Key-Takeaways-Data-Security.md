# Key Takeaways: Data Security

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Tài liệu**: Reading: Key Takeaways: Data Security (Thời lượng: ~5 phút)  
> **Tác giả**: Dee Dee Collette (IBM)

---

## 📌 Các Điểm Trọng Tâm Cần Ghi Nhớ (Key Highlights)

Hệ sinh thái an ninh dữ liệu (**Data Security Ecosystem**) bao gồm 6 cấu phần và quy trình then chốt:

### 1. Kế hoạch Quản trị (Governance Plan)
- Xác định rõ chiến lược và mục tiêu bảo vệ thông qua **Data Security Policy** nhằm nhận diện các lĩnh vực trọng yếu và nhạy cảm:
  - **Classification Criteria**: Thiết lập tiêu chí phân loại và dán nhãn dữ liệu (Confidential, Unclassified, Secret, Top Secret,...).
  - **Data Catalog**: Bản danh mục định vị chính xác vị trí lưu trữ của dữ liệu, đặc biệt là dữ liệu nhạy cảm.
  - **Resilience Plan**: Kế hoạch phục hồi hoạt động và dữ liệu khi xảy ra sự cố rò rỉ hoặc thảm họa.

### 2. Khám phá Dữ liệu (Discovery)
- Rà quét và phát hiện dữ liệu nhạy cảm trên toàn bộ hệ thống:
  - **Structured Data**: Dữ liệu có cấu trúc lưu trong Cơ sở dữ liệu (Databases).
  - **Unstructured Data**: Dữ liệu phi cấu trúc nằm rải rác trong tệp tin (Files), thư điện tử (Emails) và bảng tính (Spreadsheets).
- **Data Loss Prevention (DLP)**: Công nghệ hỗ trợ phát hiện và ngăn chặn các vấn đề thất thoát dữ liệu đang lưu chuyển qua hạ tầng mạng.

### 3. Bảo vệ Dữ liệu (Protection of Data)
- **Encryption (Mã hóa)**: Xáo trộn dữ liệu (Scrambling) để ngăn chặn truy cập trái phép, áp dụng cho cả dữ liệu lưu trữ trong database (*at rest*) lẫn dữ liệu truyền tải trên mạng (*in transit*).
- **Key Management**: Quản lý khóa an toàn, tạo khóa ngẫu nhiên hoàn toàn.
- **Access Control (Kiểm soát truy cập)**: Tích hợp với hệ thống Identity & Access Management (IAM).
- **Backup (Sao lưu)**: Đảm bảo khả năng ứng phó và khôi phục khi gặp kịch bản thảm họa hoặc mã độc tống tiền (Ransomware).

### 4. Tuân thủ Quy định Ngành (Complying with Industry Regulations)
- Tuân thủ các khung quy định bảo vệ dữ liệu phổ biến: **GDPR** (Châu Âu) và **HIPAA** (Y tế tại Mỹ).
- Xây dựng cơ chế báo cáo khi xảy ra tình trạng không tuân thủ (*Non-compliance*).
- **Data Retention**: Lưu trữ hồ sơ, dữ liệu đúng thời hạn luật pháp quy định, không lưu trữ vô thời hạn.

### 5. Phát hiện Mối đe dọa (Detection)
- Giám sát hệ thống, phân tích luồng di chuyển và cách thức dữ liệu được sử dụng (ai đang dùng, dùng như thế nào).
- **User Behavior Analytics (UBA)**: Phân tích hành vi người dùng để phát hiện sớm các dấu hiệu bất thường so với chuẩn mực.
- **Alerts**: Tự động gửi cảnh báo lên bảng điều khiển (Console) yêu cầu xử lý ngay lập tức.

### 6. Phản ứng Sự cố (Response to Security Breach)
- Điều tra, phân tích các vụ việc vi phạm (*Case Investigation*).
- Sử dụng **Dynamic Playbook** để dẫn dắt các bước ứng phó linh hoạt theo tình huống.
- Kết hợp **Automation** (tự động hóa cho các tác vụ đã biết) và **Orchestration** (điều phối cho các tình huống mới phát sinh).

---

## 🏆 Top 5 Yếu Tố Làm Giảm Thiệt Hại Chi Phí Rò Rỉ Dữ Liệu
1. **Artificial Intelligence (AI)**: Ứng dụng AI trong phát hiện và điều tra.
2. **DevSecOps**: Đưa an ninh vào mọi khâu phát triển phần mềm (Shift-Left).
3. **Incident Response (IR)**: Kế hoạch và quy trình ứng phó sự cố bài bản.
4. **Cryptography**: Mã hóa dữ liệu và quản trị khóa nghiêm ngặt.
5. **Employee Training**: Đào tạo nâng cao nhận thức bảo mật cho nhân viên.
