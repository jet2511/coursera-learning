# Reading: Understanding Multi-Factor Authentication (MFA)

> **Source**: Course *Cybersecurity Architecture* - Reading: *Understanding Multi-Factor Authentication*  
> **Author**: Dee Dee Collette (IBM)

---

## 1. Khái niệm & Mục tiêu của MFA

* **Định nghĩa**: Multi-factor Authentication (MFA) là cơ chế bảo mật yêu cầu người dùng cung cấp **từ hai yếu tố xác minh độc lập trở lên** để có quyền truy cập vào tài nguyên (hệ thống, mạng, cơ sở dữ liệu, ứng dụng).
* **Mục tiêu**: Tạo ra chiến lược phòng thủ nhiều lớp (**Defense-in-Depth**). Nếu kẻ tấn công xâm nhập hoặc bẻ khóa thành công một yếu tố (ví dụ: đánh cắp mật khẩu), họ vẫn vấp phải ít nhất một rào cản bảo mật độc lập khác trước khi có thể xâm nhập hệ thống.

---

## 2. Ba yếu tố xác thực cốt lõi (Three Factors)

MFA dựa trên giả định rằng một kẻ tấn công trái phép rất khó có thể đồng thời sở hữu tất cả các yếu tố xác thực thuộc các danh mục khác nhau:

| Yếu tố (Factor) | Định nghĩa | Ví dụ thực tế |
| :--- | :--- | :--- |
| **1. Something you know** *(Điều bạn biết)* | Thông tin chỉ duy nhất người dùng nắm giữ. | Mật khẩu (Password), mã PIN, câu hỏi bảo mật. |
| **2. Something you have** *(Vật bạn có)* | Thiết bị vật lý nằm trong quyền sở hữu của người dùng. | Điện thoại thông minh (SMS OTP, Push Notification), thẻ thông minh (Smart card), thẻ ngân hàng, phần cứng bảo mật (Hardware token/dongle như YubiKey). |
| **3. Something you are** *(Đặc tính của bạn)* | Dữ liệu sinh trắc học hoặc mẫu hành vi cá nhân gắn liền với người dùng. | Dấu vân tay (Fingerprint), mống mắt/võng mạc (Retinal pattern), nhận dạng khuôn mặt, nhận dạng giọng nói, mẫu hành vi (behavioral patterns). |

---

## 3. So sánh các cấp độ xác thực: SFA vs. 2FA vs. MFA

```
[ SFA: 1 Yếu tố ]  -->  [ 2FA: Đúng 2 Yếu tố khác nhau ]  -->  [ MFA: >= 2 Yếu tố độc lập ]
(Dễ bị tổn thương)      (Phổ biến: Know + Have)              (Phòng thủ đa tầng tối đa)
```

1. **SFA (Single-Factor Authentication - Xác thực 1 yếu tố)**:
   * Chỉ yêu cầu **1 yếu tố duy nhất**, thường là mật khẩu.
   * *Rủi ro*: Nếu mật khẩu bị rò rỉ (phishing, brute-force, data breach), không còn lớp bảo vệ nào khác.
   * Thường thấy: Tài khoản mạng xã hội hoặc email cá nhân thông thường không bật bảo vệ nâng cao.
2. **2FA (Two-Factor Authentication - Xác thực 2 yếu tố)**:
   * Yêu cầu **2 yếu tố thuộc 2 danh mục khác nhau** (ví dụ: Password + Mã OTP điện thoại, hoặc Thẻ từ + Vân tay).
   * *Lưu ý quan trọng*: Yêu cầu 2 mật khẩu khác nhau hoặc mật khẩu + mã PIN **không** phải là 2FA/MFA (vì cùng thuộc nhóm *Something you know*).
   * Thường thấy: Ngân hàng điện tử (Internet Banking), tài khoản doanh nghiệp cơ bản.
3. **MFA (Multi-Factor Authentication - Xác thực đa yếu tố)**:
   * Bao hàm cả 2FA và có thể mở rộng lên **3 yếu tố trở lên**.
   * Kết hợp tối đa sức mạnh bảo mật để bảo vệ các mục tiêu nhạy cảm cao (hạ tầng trọng yếu, phòng nghiên cứu bí mật, dữ liệu tuyệt mật).

---

## 4. Nguyên tắc lựa chọn phương thức MFA phù hợp

Việc triển khai MFA đòi hỏi phải cân nhắc giữa **độ nhạy cảm của dữ liệu** và **trải nghiệm người dùng (UX)**:

* **Các tiêu chí xem xét**:
  1. Độ nhạy cảm của tài nguyên/dữ liệu (*Data sensitivity*).
  2. Địa điểm/môi trường truy cập (*Location of access*: mạng nội bộ vs. từ xa/công cộng).
  3. Tính tiện lợi của thiết bị (*Device convenience*).
  4. Khả năng và sự sẵn sàng của người dùng (*User capability*).

* **Áp dụng theo bối cảnh**:
  * **Môi trường rủi ro trung bình / Truy cập từ xa (Remote Access)**: Ưu tiên cân bằng an ninh và trải nghiệm mượt mà. 
    * *Giải pháp*: Kết hợp Password (*Know*) + Mã OTP sinh từ Authenticator App trên điện thoại (*Have*).
  * **Môi trường tối mật / Tối quan trọng (High-security labs, Defense, Core Banking Root)**:
    * *Giải pháp*: Kích hoạt đồng thời cả **3 yếu tố** (*Know + Have + Are* - ví dụ: PIN + Hardware Key + Sinh trắc học vân tay/mống mắt).

> [!IMPORTANT]
> **Quy tắc vàng**: Mục tiêu cuối cùng của MFA là tối đa hóa an ninh mạng mà không gây phiền hà hoặc làm phức tạp hóa quá mức quy trình làm việc của người dùng (*Enhance security without overly complicating the user experience*).
