# Lab: Evaluating Enterprise System Fit for a Growing Business (PeakPulse Case Study)

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Tác giả:** Parikshit Jain  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu bài Lab

1. Liệt kê và phân tích các quy trình vận hành cốt lõi của doanh nghiệp bán lẻ đang phát triển (PeakPulse).
2. Xác định các thách thức vận hành làm giới hạn hiệu suất và khả năng mở rộng.
3. Xác lập bộ yêu cầu hệ thống (System Requirements) gắn liền với mục tiêu kinh doanh.
4. So sánh ma trận tính năng giữa **ERP** và **CRM** đối chiếu với bộ yêu cầu.
5. Đề xuất giải pháp kiến trúc tối ưu (ERP, CRM hoặc Hybrid Solution) và bảo vệ đề xuất bằng bằng chứng vận hành và Best Practices.

---

## 🏢 Bối Cảnh Doanh Nghiệp (Scenario: PeakPulse)

- **Doanh nghiệp:** PeakPulse – Công ty thiết bị dã ngoại/thể thao tăng trưởng nhanh, bán qua cả E-commerce (Shopify) và Cửa hàng vật lý (POS).
- **Khách hàng:** Người mua lẻ và các đại lý mua sỉ (bulk buyers).
- **4 Thách thức vận hành then chốt:**
  1. *Lỗi theo dõi tồn kho (Inventory tracking errors):* Dẫn đến hết hàng (stockouts) hoặc tồn kho quá mức, gây mất doanh thu và tăng chi phí lưu kho.
  2. *Dữ liệu khách hàng không nhất quán (Inconsistent customer data):* Hình thành các "ốc đảo dữ liệu" (data silos), dịch vụ CSKH kém và marketing không hiệu quả.
  3. *Chậm trễ xử lý đơn hàng (Delays in order processing):* Thiếu tự động hóa giữa các khâu bán hàng, kho vận và giao hàng.
  4. *Giới hạn khả năng mở rộng (Scalability limitations):* Hệ thống thủ công không đáp ứng được khi lưu lượng khách tăng cao hoặc mở rộng dòng sản phẩm.

---

## 🧩 PHẦN 1: Hiểu Bối Cảnh Doanh Nghiệp (Business Context)

### Bước 1: 5 Quy Trình Vận Hành Cốt Lõi (Core Business Processes)

| Quy trình cốt lõi | Mô tả chi tiết |
|---|---|
| **Inventory management** | Theo dõi mức tồn kho, tự động đặt hàng bổ sung và giám sát vận hành kho bãi. |
| **Order processing** | Xử lý đơn hàng đa kênh (online & in-store), xác thực thanh toán và theo dõi vận chuyển. |
| **Customer management** | Lưu trữ hồ sơ khách hàng 360 độ, phân khúc và hỗ trợ chiến dịch marketing mục tiêu. |
| **Financial management** | Ghi nhận chi phí, theo dõi doanh thu đa kênh, đối soát dòng tiền và lập báo cáo tài chính. |
| **Supply chain coordination** | Quản lý quan hệ nhà cung cấp, mua sắm nguyên vật liệu và điều phối lịch nhập hàng. |

### Bước 2: 4 Thách Thức Vận Hành (Operational Challenges)

| Thách thức | Ảnh hưởng đến hoạt động kinh doanh |
|---|---|
| **Inventory tracking errors** | Gây tình trạng bán vượt tồn (overselling) hoặc đọng vốn, tăng chi phí lưu kho. |
| **Inconsistent customer data** | Dữ liệu bị phân mảnh, nhân viên CSKH không có lịch sử mua sắm, giảm trải nghiệm khách. |
| **Delays in order processing** | Thiếu tự động hóa gây chậm trễ từ khâu duyệt đơn đến giao hàng, làm khách hàng thất vọng. |
| **Scalability limitations** | Hệ thống quá tải khi vào mùa cao điểm, cản trở kế hoạch mở rộng chi nhánh và danh mục mới. |

### Bước 3: Xác Lập Yêu Cầu Hệ Thống (System Requirements)

| Phân nhóm yêu cầu | Yêu cầu kỹ thuật & chức năng cụ thể |
|---|---|
| **Data Management** | Truy cập dữ liệu tập trung, nhất quán thời gian thực (Real-time centralized data). |
| **Inventory & Orders** | Tự động hóa cập nhật tồn kho đa kênh, phát cảnh báo tồn kho và điều phối đơn tự động. |
| **Customer Engagement** | Phân khúc khách hàng, quản lý chiến dịch tiếp thị và hệ thống ticket CSKH. |
| **Integration & Scalability** | Tích hợp liền mạch qua REST API với Shopify, POS và mở rộng linh hoạt theo tải. |
| **Reporting & Analytics** | Dashboard trực quan hóa KPI bán hàng, báo cáo tài chính và hiệu quả chuỗi cung ứng. |

---

## ⚖️ PHẦN 2: So Sánh Hệ Thống ERP và CRM

### Bước 1: Trọng Tâm Của Từng Hệ Thống (Primary Focus)

- **ERP (Enterprise Resource Planning):** Tập trung vào **Back-office & Vận hành nội bộ** (Quản lý kho, chuỗi cung ứng, xử lý đơn hàng, kế toán & tài chính, nhân sự).
- **CRM (Customer Relationship Management):** Tập trung vào **Front-office & Khách hàng** (Quản lý phễu bán hàng, hồ sơ khách hàng 360 độ, tự động hóa marketing, chăm sóc khách hàng).

### Bước 2: Ma Trận Đối Chiếu Tính Năng (Feature Comparison Matrix)

| Yêu cầu kinh doanh | Hệ thống ERP | Hệ thống CRM |
|---|:---:|:---:|
| **Inventory management** | ✔ Hỗ trợ toàn diện theo dõi kho & tự động hóa | ✖ Không thiết kế để quản lý kho |
| **Order processing** | ✔ Tự động hóa trọn gói quy trình Order-to-Cash | ✖ Chỉ hỗ trợ tạo báo giá/đơn bán ban đầu |
| **Customer data centralization** | ✖ Hỗ trợ cơ bản thông tin thanh toán/giao hàng | ✔ Chuyên sâu hồ sơ 360 độ, hành vi & tương tác |
| **Marketing campaign management** | ✖ Không hỗ trợ quản lý chiến dịch marketing | ✔ Hỗ trợ đầy đủ phân khúc, email & lead scoring |
| **Financial reporting** | ✔ Kế toán, sổ cái, doanh thu & dòng tiền chi tiết | ✖ Không hỗ trợ báo cáo kế toán chuyên sâu |
| **Supply chain coordination** | ✔ Quản trị nhà cung cấp, mua sắm & logistics | ✖ Không hỗ trợ chuỗi cung ứng |
| **Customer engagement** | ✖ Giới hạn ở việc xuất hóa đơn | ✔ Hỗ trợ đa kênh (Chat, Email, Support Tickets) |
| **Real-time data access** | ✔ CSDL tập trung cho toàn bộ vận hành nội bộ | ✔ CSDL tập trung cho hoạt động khách hàng |
| **Scalability** | ✔ Khả năng scale giao dịch, đa kho, đa tiền tệ | ✔ Khả năng scale lượng contacts và đội ngũ sales |
| **Integration with Shopify** | ✔ Tích hợp đồng bộ tồn kho, đơn hàng, giá bán | ✔ Tích hợp đồng bộ khách hàng và lịch sử mua |

### Bước 3: Đánh Giá Độ Phù Hợp (Fit Analysis)

> **Nhận định:** Nếu bắt buộc phải chọn **1 hệ thống đơn lẻ**, thì **ERP** là hệ thống phù hợp hơn cho PeakPulse vì phần lớn các vấn đề nghẽn cổ chai nghiêm trọng nhất của họ (tồn kho, xử lý đơn hàng, chuỗi cung ứng, tài chính) nằm ở khối vận hành back-office. Tuy nhiên, để giải quyết triệt để 100% bài toán kinh doanh bao gồm cả dữ liệu khách hàng và marketing, một giải pháp kết hợp (**Hybrid Solution**) là lý tưởng nhất.

---

## 🏆 PHẦN 3: Đề Xuất & Bảo Vệ Giải Pháp (Recommendation & Justification)

### Bước 1: Đề Xuất Hệ Thống (System Recommendation)

> **Đề xuất:** PeakPulse nên triển khai một **Hệ thống ERP trên nền tảng Cloud tích hợp sẵn module CRM (hoặc kết hợp Cloud ERP với CRM chuyên biệt qua API)** như *Oracle NetSuite*, *Microsoft Dynamics 365*, hoặc kết hợp *NetSuite ERP + Salesforce/HubSpot CRM*.

### Bước 2: Luận Cứ Bảo Vệ (Justification)

- **Operational Efficiency:** Tự động hóa quy trình từ khâu đặt hàng trên Shopify $\rightarrow$ trừ kho $\rightarrow$ đóng gói tại WMS $\rightarrow$ xuất hóa đơn kế toán, loại bỏ hoàn toàn lỗi nhập tay.
- **Centralized Data:** Xóa bỏ ốc đảo dữ liệu; mọi phòng ban từ Kho, Bán hàng, CSKH đến Tài chính đều nhìn thấy một "nguồn sự thật duy nhất" (Single Source of Truth).
- **Scalability:** Kiến trúc Cloud SaaS giúp hệ thống tự động mở rộng theo lưu lượng truy cập mà không lo sập server trong mùa cao điểm.
- **CRM Flexibility:** Module CRM đảm nhiệm việc phân khúc khách hàng, cá nhân hóa tiếp thị và cung cấp công cụ cho đội CSKH xử lý ticket tức thời.

### 💡 Best Practice Tip (Từ bài đọc Implementation):
> **Khuyến nghị triển khai:** Chọn giải pháp **Cloud-based (SaaS)** và áp dụng **Chiến lược triển khai cuốn chiếu (Phased Rollout)** — ưu tiên triển khai các module cốt lõi (Kho, Đơn hàng, Kế toán) trước trong giai đoạn 1, sau đó tích hợp CRM và tự động hóa marketing trong giai đoạn 2; kết hợp đào tạo người dùng bài bản để giảm thiểu tối đa rủi ro gián đoạn kinh doanh.

---

## 📝 Tóm Tắt Nhanh

- **PeakPulse** cần giải quyết đồng thời bài toán **Vận hành (Kho, Đơn, Kế toán)** và bài toán **Khách hàng (Dữ liệu 360, Marketing)**.
- **ERP** giải quyết các bài toán gốc rễ về vận hành back-office; **CRM** hoàn thiện trải nghiệm khách hàng front-office.
- **Giải pháp tối ưu:** Hybrid Cloud ERP + CRM tích hợp với Shopify & POS.
