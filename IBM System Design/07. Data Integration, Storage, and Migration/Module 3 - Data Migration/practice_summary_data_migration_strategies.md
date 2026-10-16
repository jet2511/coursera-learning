# Practice Summary: Choosing & Justifying Data Migration Strategies

> **Course:** IBM System Design — 07. Data Integration, Storage, and Migration  
> **Module:** Module 3 - Data Migration  
> **Topic:** Strategy Selection (Big Bang vs. Trickle/Phased), Trade-off Analysis & High-Stakes Adaptation

---

## 1. Tổng quan hai chiến lược di chuyển dữ liệu (Data Migration Strategies)

| Tiêu chí | Big Bang Migration | Trickle / Phased Migration |
| :--- | :--- | :--- |
| **Cơ chế** | Chuyển toàn bộ dữ liệu qua hệ thống mới trong một mốc thời gian ngắn (ví dụ: cuối tuần). | Chia nhỏ dữ liệu/hệ thống và di chuyển từng đợt qua nhiều tuần/tháng. |
| **Tốc độ cutover** | Nhanh, hệ thống mới hoạt động ngay. | Kéo dài thời gian chuyển giao. |
| **Độ phức tạp kỹ thuật** | Thấp hơn trong khâu đồng bộ song song, nhưng cực kỳ rủi ro ở bước cutover & rollback. | Cao hơn (cần dual-run, cơ chế đồng bộ dữ liệu song song như Change Data Capture - CDC). |
| **Rủi ro vận hành** | **Rất cao**: Lỗi một điểm có thể làm sập toàn bộ luồng nghiệp vụ. | **Thấp**: Rủi ro được cô lập theo từng module nhỏ; rollback linh hoạt. |
| **Khả năng kiểm thử** | Hạn chế trong cửa sổ downtime ngắn. | Rất cao; kiểm thử, đối soát (reconciliation) kỹ lưỡng theo từng giai đoạn. |

---

## 2. Kịch bản 1: Bán lẻ (RetailCorp) & Phân tích Trade-offs

### 2.1. Lựa chọn chiến lược
* **Lựa chọn:** **Strategy B (Trickle Migration)**
* **Lý do cốt lõi:** Bảo đảm tính liên tục của nghiệp vụ (Business Continuity) và giảm thiểu rủi ro gián đoạn bán hàng/doanh thu.

### 2.2. Biện minh quyết định (Justifying the Decision: Cost vs. Disruption vs. Quality)
1. **Business Disruption vs. Timeline:**
   * Một đợt cutover thất bại theo kiểu Big Bang có thể làm tê liệt toàn bộ giao dịch bán lẻ tại cửa hàng và online.
   * Kéo dài timeline đổi lại việc khoanh vùng rủi ro, không bao giờ làm dừng hoạt động kinh doanh hàng ngày.
2. **Data Quality vs. Speed:**
   * Phân kỳ cho phép kiểm tra tính toàn vẹn và đối soát dữ liệu (data reconciliation) theo thời gian thực giữa hệ thống cũ và mới.
   * Ngăn chặn tình trạng phát sinh rác/sai lệch dữ liệu quy mô lớn sau cutover.
3. **Total Cost of Ownership (TCO):**
   * Chi phí vận hành song song hai hệ thống (dual-run overhead) trong vài tháng đóng vai trò như một khoản **"phí bảo hiểm"**.
   * Chi phí này rẻ hơn rất nhiều so với thiệt hại mất doanh thu, danh tiếng và chi phí khẩn cấp để rollback/khắc phục sự cố nếu Big Bang thất bại.

---

## 3. Kịch bản 2: Môi trường rủi ro cao (Healthcare System)

### 3.1. Ràng buộc khắt khe
* **Data Accuracy:** Ràng buộc pháp lý nghiêm ngặt (HIPAA, tiêu chuẩn y tế); sai sót dữ liệu đe dọa trực tiếp đến tính mạng bệnh nhân.
* **Zero Downtime:** Hệ thống bệnh viện, phòng cấp cứu/ICU hoạt động liên tục 24/7/365.

### 3.2. Điều chỉnh chiến lược
* **Quyết định:** Vẫn giữ nguyên tắc của **Strategy B (Trickle)** nhưng nâng cấp kỹ thuật thực thi:
  1. **Strict Parallel-Run (Dual-System) với Change Data Capture (CDC):** Bắt và đồng bộ thay đổi dữ liệu thời gian thực giữa hai bên, nhân viên y tế truy cập hồ sơ bệnh án liền mạch không gián đoạn.
  2. **Automated Cross-Validation & Reconciliation:** Tự động đối soát 100% bản ghi bệnh án trước khi bàn giao quyền điều khiển chính cho hệ thống mới.
  3. **Phased Cutover theo mức độ rủi ro:** Chuyển giao các bộ phận rủi ro thấp trước (ví dụ: viện phí ngoại trú, quản lý kho dược) trước khi chuyển các khoa thiết yếu (khoa cấp cứu, phòng mổ, ICU) nhằm đảm bảo luôn có phương án fallback an toàn.

---

## 4. Kiến thức mở rộng đề xuất (Next Steps)
* **ETL vs. ELT trong Migration:** 
  * **ETL:** Chuẩn hóa và làm sạch dữ liệu ngoài luồng trước khi đẩy vào kho mới (phù hợp với Big Bang hoặc hệ thống khắt khe về format).
  * **ELT:** Tận dụng năng lực tính toán phân tán của Modern Cloud Data Warehouse (Snowflake, BigQuery, Databricks) để load dữ liệu thô nhanh chóng, sau đó transform trong kho (tối ưu hóa throughput cho Trickle/CDC).
