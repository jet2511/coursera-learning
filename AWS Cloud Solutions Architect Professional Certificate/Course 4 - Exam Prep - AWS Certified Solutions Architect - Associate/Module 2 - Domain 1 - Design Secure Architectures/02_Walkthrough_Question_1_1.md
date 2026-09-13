# Walkthrough Question 1.1: Securing Root User Logins

## 1. Phương pháp làm bài thi Multiple-Choice (Exam Strategy)
1. **Phân tích Question Stem:** Đọc kỹ đề bài, xác định số lượng đáp án cần chọn (ví dụ: *Select TWO* - không có điểm thành phần).
2. **Xác định Keywords:** Tìm các từ khóa trọng tâm để khoanh vùng kiến thức.
3. **Phân tích Distractors (Đáp án gây nhiễu):** Loại trừ các đáp án vi phạm Best Practices hoặc sai nguyên lý cơ bản của AWS.
4. **Chọn Best Answers:** Đánh giá các đáp án còn lại dựa trên tính khả thi và chuẩn khuyến nghị của AWS.

---

## 2. Chi tiết Câu hỏi & Phân tích (Walkthrough Question 1.1)

### Đề bài (Stem)
> **The CIO of a company is concerned about the security of the root user of their AWS account. How can the CIO ensure that the root account follows the best practices for securely logging in? (Select TWO.)**
> 
> *(Giám đốc CNTT lo ngại về tính bảo mật của tài khoản Root User. Làm thế nào để đảm bảo tài khoản root tuân thủ các Best Practices khi đăng nhập an toàn? Chọn 2 đáp án).*

### Phân tích Từ khóa (Keywords)
- Root user: Tài khoản quản trị cấp cao nhất của AWS Account.
- Best practices: Các khuyến nghị bảo mật chuẩn từ AWS.
- Secure login: Bảo mật quá trình xác thực và đăng nhập.

---

### Các lựa chọn (Options)

- **A.** *Enforce the use of an Access Key ID and Secret Access Key for the root user logins.*
- **B.** **[CORRECT]** *Enforce the use of MFA for the root user logins.*
- **C.** *Enforce the root user to assume a role to access the root user's own resources.*
- **D.** **[CORRECT]** *Enforce the use of complex passwords for member account root user logins.*
- **E.** *Enforce the deletion of the root account so that it cannot be used.*

---

## 3. Giải thích Đáp án & Phân tích Nhiễu (Explanation & Distractor Analysis)

### Đáp án Đúng
- **B (Enforce MFA):** Bật xác thực đa yếu tố (Multi-Factor Authentication - MFA) là lớp phòng thủ quan trọng nhất để bảo vệ Root User trước các cuộc tấn công đánh cắp mật khẩu.
- **D (Complex Passwords):** Bắt buộc đặt mật khẩu phức tạp (chiều dài tối thiểu, kết hợp chữ hoa/thường/số/ký tự đặc biệt) cho các tài khoản thành viên (member accounts) giúp giảm thiểu rủi ro bị tấn công vét cạn (brute-force).

### Phân tích Đáp án Gây nhiễu (Distractors)
- **A SAI:** Không bao giờ tạo/sử dụng Access Key cho Root User. Access Key có quyền lực tuyệt đối, không thể thu hẹp quyền và cực kỳ nguy hiểm nếu bị rò rỉ. Best practice là khóa hoặc xóa hoàn toàn Root Access Keys.
- **C SAI:** Root user không cần và không thể assume role vào chính account của nó để truy cập tài nguyên sở hữu. Roles dùng cho services, cross-account hoặc identity federation.
- **E SAI:** Không thể xóa Root Account độc lập với tài nguyên. Xóa Root Account đồng nghĩa với việc đóng (close/terminate) toàn bộ tài khoản AWS và hủy toàn bộ tài nguyên bên trong.

---

## 4. Key Takeaways cho kỳ thi SAA-C03
- **Root User Checklist:**
  - Luôn kích hoạt **MFA** (Hardware/Virtual).
  - Sử dụng **Strong/Complex Password**.
  - **Xóa Root Access Keys** (không sử dụng API/CLI bằng root credentials).
  - Khóa tài khoản root và chỉ dùng IAM User/Role cho công việc hàng ngày theo **Least Privilege**.
