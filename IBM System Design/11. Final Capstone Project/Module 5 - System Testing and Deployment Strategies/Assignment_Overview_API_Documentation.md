# Assignment Overview: API Documentation

- **Khóa học:** IBM System Design - Capstone Project
- **Module:** Module 5 - System Testing and Deployment Strategies
- **Chủ đề:** API Documentation for Retail Bank's Digital Core
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Xây dựng tài liệu đặc tả API chuẩn doanh nghiệp tài chính, mô hình hóa luồng dữ liệu (Data Flow Diagram), xác lập cơ chế xác thực/ủy quyền bảo mật (OAuth2, JWT, mTLS) và chuẩn hóa xử lý mã lỗi cho ABC Bank.

---

## 1. Tóm tắt các bước thực hiện (What You Will Do)

| Bước | Tên bước | Nội dung cốt lõi |
| :--- | :--- | :--- |
| **Step 1** | **Identify Key APIs** | Xác định và lập danh mục các API nội bộ & đối tác: Auth API, Transaction API, Fraud Detection API, Onboarding/KYC API, Loan Eligibility API, Notification API, Credit Bureau API. |
| **Step 2** | **Document API Endpoints** | Đặc tả kỹ thuật chi tiết các endpoint: HTTP Method (GET/POST/PUT/DELETE), đường dẫn URL, Headers, Parameters, Request Body, Response payload và mã lỗi. |
| **Step 3** | **Provide Example Requests & Responses** | Cung cấp mẫu gọi API thực tế qua cURL / OpenAPI / Postman (Sample Request JSON, Success Response JSON, Error Response JSON). |
| **Step 4** | **Define Status Codes & Error Handling** | Chuẩn hóa bảng mã lỗi HTTP (200/201, 400/401/403/404, 500/503) và cấu trúc payload báo lỗi thống nhất (`errorCode`, `message`, `timestamp`, `traceId`). |
| **Step 5** | **Illustrate Data Flow Diagrams** | Vẽ sơ đồ luồng dữ liệu tương tác giữa các service: *Mobile App $\rightarrow$ API Gateway $\rightarrow$ Transaction Service $\rightarrow$ Fraud Service $\rightarrow$ Core Banking Ledger $\rightarrow$ Notification*. |
| **Step 6** | **Document Auth & Authorization** | Mô tả các cơ chế bảo mật: OAuth2.0 Token Flows (Authorization Code + PKCE), JWT validation, mTLS cho kết nối backend nhạy cảm, API Keys và IP whitelisting. |
| **Step 7** | **Validate API Documentation** | Sử dụng Checklist để kiểm tra tính đầy đủ, tính khả thi khi kiểm thử và sự sẵn sàng bàn giao cho đội ngũ phát triển/tích hợp. |

---

## 2. Danh sách sản phẩm cần nộp (What You Will Deliver)

1. **API Inventory Table:** Bảng danh mục toàn bộ API nội bộ & bên ngoài.
2. **Endpoint Documentation (Tối thiểu 2 APIs):** Tài liệu đặc tả chi tiết 2 APIs quan trọng (ví dụ: Payments / Transaction API và Onboarding / KYC API).
3. **Example API Requests & Responses:** Mẫu JSON request/response và cURL chi tiết.
4. **Status Code Matrix:** Bảng ma trận mã trạng thái và chuẩn hóa cấu trúc lỗi.
5. **API Data Flow Diagram:** Sơ đồ trực quan luồng dữ liệu liên microservices.
6. **Authentication & Authorization Summary:** Tài liệu bảo mật token, mTLS và phân quyền RBAC.
7. **Validation Checklist:** Bảng kiểm tra xác nhận tính hoàn thiện của tài liệu API.
