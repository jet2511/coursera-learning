# Assignment Overview: Test Planning and Case Design Using TDD and BDD

- **Khóa học:** IBM System Design - Capstone Project
- **Module:** Module 5 - System Testing and Deployment Strategies
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Đánh giá enterprise test plans, phát hiện lỗ hổng coverage, và thiết kế test cases chuẩn TDD/BDD đáp ứng chuẩn kiến trúc & quy định (KYC, AML, MFA) cho hệ thống Digital Core của Retail Bank.

---

## 1. Tóm tắt các nhiệm vụ (Tasks)

| Task | Tên nhiệm vụ | Nội dung cốt lõi |
| :--- | :--- | :--- |
| **Task 1** | **Review & Annotate Test Plan** | Phân tích sample enterprise test plan; chỉ ra test case thiếu, trùng lặp hoặc sai lệch. Nêu bật tiêu chí nghiệm thu yếu, thiếu negative testing và vi phạm compliance (KYC, AML, MFA). |
| **Task 2** | **Build Requirements Traceability Matrix (RTM)** | Xây dựng ma trận RTM kết nối yêu cầu với test case tương ứng; phát hiện thiếu mapping/thiếu coverage, đảm bảo truy vết toàn diện giữa functional & regulatory mandates. |
| **Task 3** | **Create TDD-style Test Cases** | Thiết kế 2-3 test cases theo phong cách TDD cho module cốt lõi (Loan Eligibility Engine, KYC Validation, hoặc Fraud Rules Engine). Xác định rõ: Preconditions, Inputs, Execution steps, Expected outputs, Edge cases. |
| **Task 4** | **Write BDD Scenarios (Gherkin)** | Viết 2 kịch bản BDD chuẩn Gherkin syntax (`Given-When-Then`) mô hình hóa luồng khách hàng thực tế (Account creation, Fund transfers, hoặc Failed verification). |
| **Task 5** | **Validate Test Coverage & Quality** | Dùng checklist để rà soát toàn bộ: đảm bảo 100% requirements được map, bao quát negative/compliance scenarios, cấu trúc test đồng nhất với architecture và business workflow. |

---

## 2. Danh sách sản phẩm cần nộp (Deliverables)

1. **Annotated Enterprise Test Plan:** Bản ghi chú chi tiết các lỗi, thiếu sót và quan sát kỹ thuật trên test plan mẫu.
2. **Requirements Traceability Matrix (RTM):** Bảng ma trận truy vết đầy đủ kèm ghi chú về mức độ coverage.
3. **2 - 3 TDD-style Test Cases:** Bộ test case TDD chi tiết cho service ngân hàng được chọn.
4. **2 BDD Gherkin Scenarios:** Bộ kịch bản BDD phản ánh đúng user journey.
5. **Test Coverage Validation Checklist:** Bảng kiểm tra xác nhận độ hoàn chỉnh và tuân thủ compliance.
