# Process Narratives

## 1. Khái niệm & Thuật ngữ quan trọng
- **Process Narrative (Bản tường thuật quy trình):** Văn bản mô tả chi tiết bằng lời những gì diễn ra tại từng bước trên bản đồ quy trình (*Process Map*).
  - *Hình ảnh ẩn dụ:* Nếu **Process Map** là bản đồ địa hình dẫn đường trước chuyến đi bộ leo núi, thì **Process Narrative** là cuốn nhật ký hành trình ghi chép chi tiết những việc đã làm, lý do thực hiện (*why*), công cụ và bằng chứng để người sau có thể tái lập và tin cậy.
- **Internal Controls (Kiểm soát nội bộ):** Các cơ chế, chính sách đảm bảo hoạt động tuân thủ chuẩn mực kế toán và quản trị rủi ro.
- **Audit Compliance (Tuân thủ kiểm toán):** Yêu cầu bắt buộc từ luật định/chính sách; cung cấp dấu vết kiểm toán (*audit trail*) minh bạch về các điểm kiểm soát và người chịu trách nhiệm.
- **Process Owner (Chủ sở hữu quy trình):** Người được chỉ định chịu trách nhiệm chính trong việc cập nhật, bảo trì tính chính xác của bản tường thuật khi có thay đổi.

---

## 2. Mối quan hệ tương hỗ: Process Map vs. Process Narrative

| Đặc tính | Process Map (Bản đồ) | Process Narrative (Văn bản tường thuật) |
| :--- | :--- | :--- |
| **Hình thức** | Trực quan (Sơ đồ, Flowchart, Swimlanes) | Văn bản (Word, Excel / Spreadsheet) |
| **Trọng tâm** | Dòng chảy công việc, kết nối, các điểm rẽ nhánh | Chi tiết hoạt động, bối cảnh, mục đích, logic điều kiện |
| **Lợi ích kết hợp** | Giữ sơ đồ tinh gọn, không bị quá tải chi tiết | Chứa toàn bộ ngoại lệ (*exceptions*), công cụ sử dụng và tiêu chí duyệt |

---

## 3. Case Study: Invoice Approval Process (Duyệt hóa đơn)
- **Luồng trực quan trên Map:** Tiếp nhận hóa đơn từ nhà cung cấp $\rightarrow$ Phê duyệt $\rightarrow$ Ghi nhận giao dịch tài chính $\rightarrow$ Kết thúc.
- **Chi tiết bổ sung qua Narrative:**
  - *Ai làm (Who):* Nhân viên kế toán công nợ (AP Clerk) đối chiếu 3 chiều (3-way match: PO, Hóa đơn, Biên bản nhận hàng); Kế toán trưởng ký duyệt.
  - *Công cụ gì (Tools):* Hệ thống ERP (SAP/Oracle), phần mềm OCR quét hóa đơn.
  - *Xử lý ngoại lệ (Exceptions):* Nếu hóa đơn lệch quá 5% so với PO thì liên hệ lại nhà cung cấp để đối soát.

---

## 4. 5 Giá trị then chốt của Process Narrative
1. **Tuân thủ kiểm toán & Quy định (Regulatory & Audit Compliance):** Cung cấp bằng chứng minh bạch về quyền hạn và quyết định cho kiểm toán viên.
2. **Đơn giản hóa bản đồ (Process Simplification):** Giữ bản đồ trực quan sạch sẽ; mọi logic phức tạp được chuyển sang narrative.
3. **Chuyển giao tri thức & Onboarding (Knowledge Transfer):** Giúp nhân viên mới hiểu nhanh cả "cách làm" lẫn "lý do tại sao phải làm".
4. **Chuẩn hóa & Nhất quán (Consistency & Standardization):** Thống nhất thuật ngữ và cấu trúc vận hành liên phòng ban.
5. **Nền tảng cải tiến liên tục (Continuous Improvement):** Phơi bày sự chậm trễ trong quyết định, các điểm chồng chéo để làm căn cứ tự động hóa (automation).

---

## 5. Best Practices khi viết Process Narrative
- **Pair Symbol with Context:** Mỗi ký hiệu trên sơ đồ (nhiệm vụ, hình thoi điều kiện, tài liệu) phải ứng với một mục chú thích/nội dung trong narrative.
- **Concise but Complete:** Mô tả súc tích nhưng đầy đủ 4 yếu tố: **Ai làm (Who)**, **Dùng công cụ/dữ liệu gì (Tools/Data)**, **Điều kiện kích hoạt bước kế tiếp (Trigger)**, và **Bằng chứng hoàn tất (Evidence)**.
- **Maintain Version History:** Quản lý lịch sử phiên bản và phân công rõ Process Owner cập nhật định kỳ.
- **Standard Template:** Chuẩn hóa bảng biểu gồm các cột: `Step No.` | `Description` | `Role` | `Inputs` | `Outputs` | `Exceptions/Comments`.
