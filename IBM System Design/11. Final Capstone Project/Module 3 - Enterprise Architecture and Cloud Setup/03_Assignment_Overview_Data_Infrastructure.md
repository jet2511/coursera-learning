# Assignment Overview: Data Infrastructure
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Giai đoạn này tập trung vào việc thiết kế **Hạ tầng dữ liệu doanh nghiệp (Enterprise Data Infrastructure)** và **Sơ đồ luồng dữ liệu (Data Flow Diagram - DFD)** nhằm hợp nhất các hệ thống dữ liệu đang bị phân mảnh của Ngân hàng bán lẻ (**Retail Bank**). 
Mục tiêu là trực quan hóa luồng tích hợp đầu-cuối (End-to-End Data Integration) từ các nguồn dữ liệu rời rạc, đi qua pipeline ETL/ELT an toàn, đạt chuẩn kiểm toán (Auditability), tuân thủ các quy định bảo mật quyền riêng tư tài chính (KYC, AML, PCI-DSS, GDPR), và cấp dữ liệu cho kho dữ liệu tập trung phục vụ phân tích và báo cáo pháp lý.

---

## 2. Ba nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Xác định các thành phần luồng dữ liệu (Data Flow Components)
- **Công cụ:** Lucidchart, Draw.io hoặc Mermaid.
- **Ký hiệu DFD chuẩn mực:**
  - **External Entities (Thực thể nguồn/đích):** CRM, Core Banking, Loan Management System, Transaction Log Sources, Regulatory Bodies, Business Dashboards.
  - **Processes (Tiến trình xử lý):** Các tác vụ trích xuất (Extraction), làm sạch dữ liệu (Data Cleansing/Validation), ẩn danh hóa (Data Masking), mã hóa (Encryption), và nạp dữ liệu (Loading).
  - **Data Stores (Kho lưu trữ dữ liệu):** Staging Layer (Vùng đệm), Centralized Data Warehouse / Lakehouse, Audit Trail Logs.
  - **Data Flows (Luồng dữ liệu):** Các mũi tên có nhãn rõ ràng mô tả dữ liệu di chuyển và trạng thái.

### Task 2: Xây dựng sơ đồ DFD tích hợp dữ liệu hoàn chỉnh (Data Flow Diagram)
- **Nguồn dữ liệu đầu vào:** CRM, Loan Management, Core Banking, Transaction Logs.
- **Các giai đoạn của ETL Pipeline:**
  - **Extract (Trích xuất):** Kết nối an toàn qua API / Change Data Capture (CDC) / Batch Ingestion.
  - **Transform (Chuyển đổi & Chuẩn hóa):** Kiểm tra tính hợp lệ dữ liệu (Data Validation Points), chuẩn hóa cấu trúc, làm giàu dữ liệu (Data Enrichment), thực thi che giấu dữ liệu nhạy cảm (**Data Masking** cho số thẻ, PII), và mã hóa chuẩn ngân hàng (**AES-256**).
  - **Load (Nạp dữ liệu):** Chuyển dữ liệu vào Staging Layer, xử lý và nạp vào Enterprise Data Warehouse.
- **Dấu mốc kiểm toán (Audit Trail Markers):** Ghi nhận nhật ký kiểm toán bất biến (Immutable Logs) cho mọi thao tác truy cập và chuyển đổi dữ liệu nhằm đáp ứng thanh tra pháp lý.

### Task 3: Đối soát checklist thẩm định kiến trúc dữ liệu (Checklist Validation)
- Xác nhận sự hiện diện đầy đủ của các hệ thống cốt lõi.
- Kiểm tra tính module hóa và khả năng chịu tải của các pipeline ETL.
- Xác nhận các vùng đệm (Staging) và kho lưu trữ (Warehouse) được phân tầng rành mạch.
- Thẩm định các giải pháp an ninh dữ liệu: Mã hóa lưu trữ (At Rest), truyền tải (In Transit), che giấu thông tin (Masking/Tokenization), và phân quyền truy cập (RBAC).
- Đảm bảo tính truy vết toàn diện (Traceability) phục vụ báo cáo định kỳ cho Ngân hàng Nhà nước/Cơ quan quản lý và các dashboard Tableau/BI.

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Data Flow Diagram File:** `Retail_Data_Infrastructure_DataFlowDiagram.png` (hoặc `.pptx`) trực quan hóa kiến trúc hợp nhất dữ liệu và pipeline ETL.
- [ ] **2. Data Infra Validation Checklist:** `Data_Infra_Validation_Checklist.xlsx` (hoặc bảng Markdown đối soát) chứng minh đáp ứng 100% các tiêu chí tích hợp, bảo mật và tuân thủ.
- [ ] **3. Chú giải màu sắc & Ký hiệu (Legend & Color-coding):** Bảng chú giải phân biệt rõ ràng giữa Entities, ETL Processes, Data Stores và Security Markers để tăng tính thẩm mỹ và chuyên nghiệp.
