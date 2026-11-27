# Lab Guide: Modernizing Digital Banking Operations at a Retail Bank (Final Capstone Presentation)

Tài liệu hướng dẫn tổng hợp, thiết kế và hoàn thiện bài thuyết trình Capstone đồ án **Hiện đại hóa hoạt động Ngân hàng Bán lẻ (Retail Bank Modernization)**.

---

## 1. Mục tiêu và Yêu cầu cốt lõi (Core Objectives & Deliverables)
- **Mục tiêu:** Tổng hợp toàn bộ các Artifacts đã xây dựng từ Module 1 đến Module 5 thành một slide thuyết trình poster-style chuyên nghiệp, mang tầm kiến trúc sư giải pháp (Solutions / Systems Architect).
- **Template gốc:** Đã tải và lưu tại thư mục dự án `Template-Final Project.pptx` và nhân bản sẵn thành `FinalSubmission.pptx`.
- **Checklist đánh giá:** Đã tải sẵn `Final Presentation Submission Checklist.docx`.
- **Quy tắc xuất bản:**
  - Xóa slide hướng dẫn (Instruction) và mục lục (Table of Contents).
  - Xóa toàn bộ placeholder vàng hướng dẫn trên từng slide.
  - Áp dụng nguyên tắc **6×6**: tối đa 6 bullets/slide, mỗi bullet $\le 6$ từ.
  - Sử dụng bảng trực tiếp (copy từ Word/Excel), không chụp ảnh màn hình của bảng.
  - Sơ đồ, kiến trúc, luồng DFD/Sequence/ERD phải nhúng trực tiếp hình ảnh rõ nét kèm caption ngắn gọn, rõ ràng (chỉ rõ giai đoạn và phạm vi dữ liệu).
  - Font chữ: Heading $\ge 32\text{pt}$, Body text $\ge 24\text{pt}$. Không dùng hiệu ứng animation.
  - Xuất ra file **PDF** phục vụ nộp bài cuối kỳ.

---

## 2. Cấu trúc 24 phần chi tiết cần đưa vào Slide

| STT | Phần (Section) | Nội dung & Nguồn Artifacts từ các Module trước |
| :---: | :--- | :--- |
| **1** | **Executive Summary** | - Tối đa 6–7 bullets trên 1 slide duy nhất.<br>- Bắt đầu bằng Problem Statement $\rightarrow$ 2–3 Key Data-driven Insights $\rightarrow$ Khuyến nghị hành động (Recommended Actions). |
| **2** | **Introduction** | Gồm 3 phần rõ ràng: **Opportunity** (Tại sao ngân hàng bán lẻ cần hiện đại hóa), **Approach** (Phương pháp tiếp cận: phỏng vấn bên liên quan, làm sạch dữ liệu, thiết kế ERD/Kiến trúc), **Key Hypotheses/Questions** (Giả thuyết kiến trúc đã được kiểm chứng). |
| **3** | **Objectives** | 4–6 mục tiêu chiến lược của dự án (cải thiện thông lượng giao dịch, tính sẵn sàng cao, bảo mật tuân thủ, v.v.) đồng bộ với BRD & Charter. |
| **4** | **Project Charter** | Tóm tắt từ Lab Charter: Phạm vi dự án (Scope), mục tiêu, các deliverables cốt lõi, timeline cấp cao (Milestones). |
| **5** | **Stakeholder Register** | Bảng danh sách các bên liên quan: Tên, vai trò (Role), mức độ ảnh hưởng (Influence), mức độ quan tâm (Interest level), ghi chú chính. |
| **6** | **Stakeholder Engagement Plan** | Kế hoạch tương tác: Tần suất liên lạc (Frequency), kênh/phương pháp truyền thông (Methods), người chịu trách nhiệm. |
| **7** | **Business Requirements Document (BRD)** | Trích xuất các yêu cầu nghiệp vụ trọng yếu: Phạm vi, mục tiêu, giả định (Assumptions), chỉ số thành công (Success Metrics). |
| **8** | **Use Case Diagram (Requirements)** | Sơ đồ Use Case tổng quan từ lab Requirements: Tương tác giữa Actors và hệ thống ngân hàng mới. |
| **9** | **Requirements Traceability Matrix (RTM)** | Bảng ma trận RTM: Requirement ID, Description, Stakeholder, Owner, Priority, Mapped Objective, Acceptance Criteria, Status, Related Risks. |
| **10** | **Work Breakdown Structure (WBS)** | Sơ đồ phân rã công việc WBS dạng cây phân cấp (hierarchy) rõ ràng, dễ đọc. |
| **11** | **Network Diagram** | Sơ đồ mạng lưới công việc: Các hoạt động theo kế hoạch, phụ thuộc tuần tự, đường găng (critical path nếu có). |
| **12** | **SWOT Analysis** | Bảng phân tích ma trận 4 góc: Điểm mạnh (S), Điểm yếu (W), Cơ hội (O), Thách thức (T). |
| **13** | **Risk Register** | Bảng quản lý rủi ro: Risk ID, Cause, Event, Impact, Risk Owner, Category, Probability, Impact Rating, Risk Score, Trigger Response. |
| **14** | **Risk Matrix** | Ma trận rủi ro dạng lưới xác suất vs tác động (Likelihood vs Impact Grid), phân vùng màu (Green/Yellow/Red). |
| **15** | **Process Model** | Quy trình quản lý đơn hàng/giao dịch: Sơ đồ dòng quy trình (Flowchart) kèm chi tiết các thành phần chính. |
| **16** | **System Design** | Bộ sơ đồ thiết kế hệ thống hoàn chỉnh:<br>- System Context Model / DFD (Level 0 & Level 1)<br>- Use Case Diagram<br>- Sequence Diagram |
| **17** | **Proof of Concept (PoC)** | Báo cáo thực nghiệm giải pháp:<br>- PoC Objective and Scope<br>- PoC Setup and Tools<br>- Limitations and Recommendations |
| **18** | **Database Design** | Bộ thiết kế CSDL toàn diện:<br>- Conceptual ERD & Logical ERD<br>- Data Dictionary<br>- Normalization & Chi tiết các bảng khóa chính/ngoại<br>- Data Migration Strategy |
| **19** | **Test Planning (TDD & BDD)** | Chiến lược QA/Kiểm thử:<br>- Test Plan tổng quan<br>- Bộ Test Cases theo TDD (Unit) & BDD (Cucumber/Gherkin Given-When-Then) |
| **20** | **CI/CD Workflow & Monitoring Plan** | Khung triển khai và vận hành:<br>- CI Workflow & CD Pipeline Diagram<br>- Hướng dẫn cấu hình CSDL, API Gateway, CI/CD<br>- Monitoring Framework & Cloud Components<br>- Backup & Disaster Recovery Plan (BDR / RPO / RTO) |
| **21** | **Key Findings** | 3 phát hiện kiến trúc quan trọng nhất rút ra từ các lab, gắn với số liệu định lượng (metrics). |
| **22** | **Key Recommendations** | 3–4 khuyến nghị ưu tiên hàng đầu, nêu rõ tác động kỳ vọng (expected impact) cho ngân hàng. |
| **23** | **Conclusion** | Kết luận trong 3–4 bullet points: Tác động tổng thể, lợi ích đạt được và các bước triển khai tiếp theo (Next Steps). |
| **24** | **Appendix** | Tài liệu bổ trợ, phụ lục kỹ thuật, bảng dữ liệu chi tiết, link mã nguồn tham chiếu. |

---

## 3. Danh mục tệp đã chuẩn bị trong thư mục Module 6
- `Template-Final Project.pptx`: File template gốc từ IBM/Coursera.
- `FinalSubmission.pptx`: File slide làm việc trực tiếp (đã copy từ template).
- `Final Presentation Submission Checklist.docx`: Bảng checklist tiêu chí đánh giá nộp bài.
- `Reading - Additional Resources.md`: Tổng hợp toàn bộ lab links tham khảo từ Module 1 đến Module 5.
- `Reading - Overview How to Present Your Findings.md`: Nguyên tắc và bí quyết trình bày kết quả kiến trúc.
