# Task 1: Identify Key Banking Data Entities

Bảng liệt kê 5 thực thể cốt lõi và 2 thực thể mở rộng thiết yếu cho hệ thống ngân hàng số Retail Bank.

---

## 1. Bảng nhận diện thực thể dữ liệu (Entity Identification Table)

| STT | Tên thực thể (Entity Name) | Phân loại (Type) | Mô tả nghiệp vụ & Mục đích lưu trữ (Business Description & Storage Purpose) |
| :---: | :--- | :---: | :--- |
| **1** | **Customer** | Core | Lưu trữ hồ sơ định danh cá nhân, dữ liệu định danh điện tử eKYC, phân hạng khách hàng và thông tin liên lạc (Họ tên, ngày sinh, CCCD/Passport, địa chỉ, trạng thái KYC). |
| **2** | **Account** | Core | Quản lý các tài khoản thanh toán (Checking), tài khoản tiết kiệm (Savings), hạn mức thấu chi, số dư khả dụng, số dư phong tỏa và trạng thái hoạt động gắn với từng khách hàng. |
| **3** | **Loan** | Core | Quản lý danh mục hợp đồng vay vốn (vay tiêu dùng, vay mua nhà), hạn mức phê duyệt, lãi suất, ngày giải ngân, kỳ hạn trả nợ và trạng thái nợ (nợ tiêu chuẩn, nợ xấu). |
| **4** | **Transaction** | Core | Sổ cái ghi nhận tất cả biến động số dư và giao dịch tài chính (nạp, rút, chuyển khoản nội bộ, chuyển khoản liên ngân hàng Napas/Swift) phục vụ hạch toán kế toán. |
| **5** | **Compliance Log** | Core | Lưu vết kiểm toán an ninh (Audit Trail), ghi nhận cảnh báo phòng chống rửa tiền (AML Alerts), các lần đăng nhập đáng ngờ, và báo cáo giao dịch giá trị lớn theo luật định. |
| **6** | **Card** *(Mở rộng 1)* | Additional | Quản lý các thẻ phát hành vật lý và phi vật lý (Debit Card, Credit Card) liên kết với tài khoản; lưu trữ số thẻ masked, ngày hết hạn, mã CVV mã hóa và trạng thái khóa/mở thẻ. |
| **7** | **Branch** *(Mở rộng 2)* | Additional | Quản lý mạng lưới chi nhánh, phòng giao dịch ngân hàng, mã định danh chi nhánh (Branch Code), địa chỉ địa lý, phục vụ quản trị phân vùng dữ liệu và đối soát doanh thu. |
