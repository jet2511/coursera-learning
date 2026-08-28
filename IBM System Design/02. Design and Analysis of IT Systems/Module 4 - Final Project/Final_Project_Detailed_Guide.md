# Final Project: Chiến Lược Chuyển Đổi Số Cho Nhà Bán Lẻ Quy Mô Vừa (Detailed Guide & Analysis)

---

## 1. Tóm Tắt Tình Huống Doanh Nghiệp (Scenario Context)
- **Doanh nghiệp:** Chuỗi bán lẻ thời trang & phụ kiện quy mô vừa tại Mỹ (50 cửa hàng vật lý + 1 website E-commerce).
- **Mục tiêu 2 năm tới:** Mở rộng lên **100+ cửa hàng**, hợp nhất dữ liệu, tự động hóa tồn kho, mang lại trải nghiệm Omnichannel liền mạch.
- **Thời hạn triển khai dự án:** Hoàn thành trong vòng **9 tháng** (trước mùa cao điểm mua sắm).

---

## 2. Chi Tiết 5 Bước Thực Hiện (5 Steps Breakdown)

### Step 1: Đánh Giá Hệ Thống Hiện Tại (Assess Current Systems)
1. **Hạ tầng kỹ thuật hiện tại (As-Is Architecture):**
   - **POS tại quầy:** Thiết bị chạy Windows CE lỗi thời, driver đọc thẻ từ năm 2009, thời gian xử lý thanh toán > 5s.
   - **E-commerce:** Magento 1.9 (chạy DB MySQL riêng biệt), hiệu năng kém (CLS > 0.25, load > 2s trên 4G).
   - **Lưu trữ dữ liệu:** Mỗi cửa hàng có 1 CSDL on-premise SQL riêng biệt; đồng bộ dữ liệu về trụ sở (HQ) bằng batch job ban đêm (nightly batch).
   - **Quản lý kho (Inventory):** Nhập liệu và đối soát thủ công qua file Excel/CSV.
2. **Bảng ma trận Pain Points (Pain-Point Matrix):**
   - **Thanh toán (Checkout):** Độ trễ cao, xử lý thẻ chậm $\rightarrow$ Giảm tỷ lệ chuyển đổi, khách hàng thất vọng.
   - **Tái nhập kho (Restocking):** Quy trình thủ công $\rightarrow$ Thường xuyên thiếu hàng (stockouts), chậm trễ đặt hàng nhà cung cấp.
   - **Tiếp thị (Marketing):** Tách rời danh sách email/khách hàng giữa các kênh $\rightarrow$ Không thể chạy chiến dịch cá nhân hóa.
3. **Các điểm nghẽn cốt lõi (Key Inefficiencies):**
   - Nhập CSV thủ công & trùng lặp dữ liệu.
   - Dữ liệu khách hàng không nhất quán (No Single Customer View).
   - POS và Website chậm gây mất doanh số.
   - Không thấy được tồn kho thời gian thực (Lacks real-time inventory visibility), cản trở bán hàng đa kênh (BOPIS/BORIS).

---

### Step 2: Xác Định Yêu Cầu Của Các Bên Liên Quan (Define Stakeholder Requirements)
1. **4 Nhóm Stakeholders & Nhu cầu cốt lõi:**
   - **Khách hàng (Customers):** Mua sắm nhanh, không ma sát (load web < 2s), giỏ hàng hợp nhất (Unified cart), thấy tồn kho thời gian thực.
   - **Nhân viên cửa hàng (Store Staff):** POS tin cậy, quét/thanh toán $\le$ 5s, tra cứu tồn kho nhanh tại các điểm.
   - **Ban quản lý (Management):** Góc nhìn khách hàng 360 độ (Single Customer View), báo cáo phân tích lợi nhuận/biên độ theo thời gian thực.
   - **Đội ngũ IT (IT Team):** Kiến trúc hướng dịch vụ/API (API-first), dễ bảo trì, bảo mật & tuân thủ quy định (GDPR, PCI-DSS).
2. **Yêu cầu chức năng (Functional Requirements - FR):**
   - **FR1:** Xử lý thanh toán tại quầy POS trong thời gian $\le$ 5s.
   - **FR2:** Tự động trừ tồn kho theo thời gian thực (Real-time decrement) trên mọi kênh khi có giao dịch.
   - **FR3:** Cung cấp hồ sơ khách hàng 360° qua API kết nối tập trung.
   - **FR4:** Hỗ trợ tính năng Mua online - Nhận tại cửa hàng (**BOPIS** - Buy Online Pickup In-Store).
3. **Yêu cầu phi chức năng (Non-Functional Requirements - NFR):**
   - **NFR1:** Độ sẵn sàng của hệ thống (Availability) $\ge$ 99.9%.
   - **NFR2:** Tốc độ tải trang E-commerce < 2s trên mạng di động 4G.
   - **NFR3:** Khả năng mở rộng chịu tải gấp 3 lần (3x) lưu lượng truy cập dịp lễ tết mà không bị gián đoạn (Zero downtime).

---

### Step 3: Đánh Giá Các Giải Pháp Thay Thế (Evaluate Alternative Solutions)
1. **Bảng so sánh 3 phương án (Comparative Analysis Table):**
   - **Trọng số:** Functional Fit (40%), Scalability (20%), TCO (20%), Implementation Risk (10%), Vendor Viability (10%).

| Tiêu chí | Trọng số | Option A: Salesforce Commerce Cloud + POS | Option B: Shopify Plus + Square POS | Option C: Custom Microservices (React + Node + Spree) |
| :--- | :---: | :---: | :---: | :---: |
| **Functional Fit** | 40% | 9/10 | 8/10 | 9/10 |
| **Scalability** | 20% | 10/10 | 7/10 | 10/10 |
| **Chi phí năm 1 (TCO)** | 20% | $150,000 (Vừa) | $50,000 (Rẻ nhất) | $300,000 (Đắt nhất) |
| **Thời gian triển khai (Time to Value)** | - | 6 tháng | 3 tháng | 12 tháng |
| **Rủi ro triển khai (Risk Score)** | 10% | 15 (Vừa) | 10 (Thấp nhất) | 25 (Cao nhất) |
| **Vendor Viability** | 10% | Rất cao (Salesforce) | Rất cao (Shopify/Square) | Phụ thuộc team nội bộ/vendor |

2. **Lựa chọn & Đánh đổi (Trade-offs & Recommendations):**
   - **Option A (Salesforce):** Lựa chọn tối ưu dài hạn cho mở rộng 100+ cửa hàng, hoàn thành trong 6 tháng (< hạn mức 9 tháng), cân bằng chi phí và độ phủ tính năng.
   - **Option B (Shopify Plus):** Phù hợp triển khai nhanh (3 tháng), chi phí rẻ, nhưng khả năng scale hạn chế khi vượt 100 cửa hàng phức tạp.
   - **Option C (Custom Microservices):** Quá đắt ($300k) và mất 12 tháng (trễ hạn mức 9 tháng), rủi ro kỹ thuật cao.

---

### Step 4: Phân Tích Tính Khả Thi & Quản Trị Rủi Ro (Feasibility & Risk Analysis)
1. **Đánh giá tính khả thi (TELOS/Feasibility):**
   - **Kỹ thuật (Technical Feasibility):** Giải pháp Cloud SaaS tích hợp chuẩn qua RESTful APIs, giảm thiểu hạ tầng phần cứng on-premise tại cửa hàng.
   - **Kinh tế (Economic Feasibility):** NPV dương sau 5 năm đối với giải pháp Cloud/SaaS (Salesforce/Shopify); tối ưu TCO so với việc duy trì server on-premise riêng cho từng cửa hàng.
   - **Vận hành (Operational Feasibility):** Đào tạo nhân viên trong vòng 8 tuần; lộ trình 9 tháng ăn khớp với chu kỳ bán hàng theo mùa vụ.
2. **Sổ đăng ký rủi ro (Risk Register Excerpt):**
   - **R1: Thất thoát dữ liệu khi di chuyển (Data Migration Loss):**
     - *Xác suất (P):* 3 | *Tác động (I):* 4 | *Risk Score:* 12.
     - *Giảm thiểu (Mitigation):* Thực hiện 2 lần chạy thử nghiệm di chuyển dữ liệu (Dry runs) + Xác thực mã kiểm tra toàn vẹn (Checksum validation).
   - **R2: Sự cố gián đoạn nhà cung cấp (Vendor Outage/Downtime):**
     - *Xác suất (P):* 2 | *Tác động (I):* 5 | *Risk Score:* 10.
     - *Giảm thiểu (Mitigation):* Cam kết SLA 99.9% hợp đồng + POS hỗ trợ chế độ Offline Mode (lưu giao dịch local và tự động đồng bộ khi có mạng).

---

### Step 5: Trực Quan Hóa Kiến Trúc & Lộ Trình Triển Khai (Visuals & Roadmap)
1. **Các sơ đồ trực quan cần chuẩn bị:**
   - **DFD Context & Level 0:** Luồng dữ liệu giữa Khách hàng, POS, E-commerce, Cloud ERP/Inventory và Nhà cung cấp.
   - **ERD:** Các thực thể Customer, Order, Product, Inventory, Supplier và quan hệ liên kết.
   - **UML Diagrams:** Use Case Diagram, Sequence Diagram (Omnichannel Checkout / BOPIS), Activity Diagram (Restocking).
   - **Omnichannel Process Flow:** Quy trình mua online $\rightarrow$ Trừ tồn kho tập trung $\rightarrow$ Nhận tại cửa hàng.
2. **Lộ trình 9 tháng (9-Month Implementation Roadmap):**
   - **Tháng 1 - 2:** Hoàn thiện thiết kế kiến trúc, lựa chọn vendor, chuẩn bị dữ liệu (Data cleansing).
   - **Tháng 3 - 5:** Cấu hình Cloud Platform, tích hợp REST API, triển khai thử nghiệm dữ liệu (Data Migration Dry Runs).
   - **Tháng 6 - 7:** Pilot tại 5 cửa hàng đại diện + Đào tạo nhân viên (8 tuần).
   - **Tháng 8:** Triển khai toàn diện 50 cửa hàng + Chạy song song nghiệm thu (Cutover).
   - **Tháng 9:** Tối ưu hóa, đánh giá hiệu năng và sẵn sàng cho mùa mua sắm cao điểm & mở rộng 100+ cửa hàng.
