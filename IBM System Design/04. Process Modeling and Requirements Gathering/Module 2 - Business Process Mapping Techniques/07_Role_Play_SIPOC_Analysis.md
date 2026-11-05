# Role Play Summary: SIPOC Analysis for Order-to-Invoice Process

## 1. Context & Business Problem
* **Process in Scope:** Order-to-Invoice (từ nhận đơn hàng đến xuất hóa đơn).
* **Current Operational Friction:**
  * **Finance:** Nghẽn thanh toán do kiểm tra tín dụng trễ (billing holds / credit check timing).
  * **Customer Service:** Khách hàng phàn nàn vì thiếu cập nhật trạng thái đơn nhất quán.
  * **Shipping:** Hàng bị giữ tại kho chờ xác nhận thanh toán/hóa đơn trước khi xử lý.
  * **IT:** Lỗi bất đồng bộ dữ liệu giữa các hệ thống (CRM, ERP, WMS).

---

## 2. SIPOC Analysis Breakdown

### 2.1. Suppliers (Bên cung cấp)
* **Customers / Clients:** Gửi đơn đặt hàng (PO), thông tin tài khoản, và địa chỉ/yêu cầu giao hàng.
* **Sales / Account Executives:** Cung cấp hợp đồng thương mại, bảng giá đặc thù và điều khoản thanh toán.
* **Finance / Credit Team:** Thiết lập hạn mức tín dụng (credit limits) và chính sách thanh toán (payment terms).
* **IT / Upstream Systems (CRM / E-commerce / EDI):** Cung cấp luồng dữ liệu tự động và dữ liệu tổng thể khách hàng (Customer Master Data).

### 2.2. Inputs (Đầu vào kích hoạt quy trình)
* **Purchase Order (PO) / Sales Order Request:** Kích hoạt chính, chứa thông tin sản phẩm, số lượng, giá thỏa thuận và địa chỉ giao hàng.
* **Customer Account & Master Data:** Lịch sử thanh toán, hạn mức tín dụng và trạng thái thuế.
* **Inventory Availability Data:** Dữ liệu tồn kho thời gian thực từ WMS.
* **Billing / Credit Rules & Contracts:** Điều khoản tín dụng (Net 30, trả trước) và quy tắc định giá.

### 2.3. Process & Critical Bottlenecks (Quy trình & Điểm nghẽn)
* **Core Steps:**
  1. Order Capture & Entry
  2. Credit Check & Order Validation
  3. Fulfillment Order Release & Allocation
  4. Picking, Packing & Shipping
  5. Goods Issue & Delivery Confirmation
  6. Invoice Generation & Dispatch

* **Root Cause Bottlenecks:**
  * **Shipping Delays (tại Step 2):** Credit Check chạy không đồng bộ (asynchronous) và duyệt billing hold thủ công làm nghẽn lệnh xuất kho.
  * **Duplicate Invoicing (tại Step 6):** Thiếu cơ chế kiểm tra trùng (idempotency key / PO uniqueness); kích hoạt billing từ cả batch tự động lẫn trigger thủ công sau khi xử lý lỗi.
  * **Hand-off Friction (Step 4 -> Step 6):** Hóa đơn phát hành trước khi có xác nhận giao hàng (Goods Issued) từ WMS đồng bộ về ERP.

### 2.4. Outputs & Business Impacts (Đầu ra & Tác động)
* **Internal Impact:**
  * Lãng phí công sức làm lại (rework), hủy hóa đơn và phát hành credit notes.
  * Kéo dài chỉ số DSO (Days Sales Outstanding) do khách hàng giữ tiền khi hóa đơn có tranh chấp.
  * Ứ đọng hàng hóa tại khu vực staging của kho bãi.
  * Xung đột nội bộ (silos) giữa Finance, CS, Shipping và IT.
* **Customer Impact:**
  * Xói mòn niềm tin đối tác do nhận hóa đơn sai/trùng.
  * Gián đoạn chuỗi cung ứng của khách do hàng giao chậm trễ.
  * CSKH không có dữ liệu thời gian thực để hỗ trợ, dẫn đến nguy cơ mất khách hàng (churn).

---

## 3. Actionable Improvement Plan & RACI Ownership

### Key Action Items:
1. **Chặn trùng hóa đơn (Immediate):**
   * Áp dụng quy tắc kiểm tra ràng buộc duy nhất (idempotency key: `PO Number + Delivery ID`).
   * Ràng buộc phát hành hóa đơn tự động duy nhất sau sự kiện "Goods Issued" (PGI) từ WMS sang ERP.
2. **Loại bỏ chậm trễ giao hàng (Process Re-alignment):**
   * Đưa Credit Check lên đầu quy trình (Upstream): tự động xác thực ngay tại khâu nhập đơn (Order Entry).
   * Áp dụng SLA xử lý billing hold thủ công tối đa 2 giờ.
3. **Đồng bộ hóa hệ thống & Minh bạch dữ liệu:**
   * Triển khai hàng đợi sự kiện (event-queues) có cơ chế retry và alert lỗi tự động giữa CRM, ERP và WMS.
   * Xây dựng dashboard tập trung cho CSKH để theo dõi trạng thái đơn hàng theo thời gian thực.

### Roles & Responsibilities:
* **IT Lead:** Thiết lập kiểm tra trùng lặp trên hệ thống ERP/Billing và tối ưu pipeline đồng bộ dữ liệu.
* **Finance Manager:** Tự động hóa duyệt hạn mức tín dụng và cam kết SLA duyệt hold trong vòng 2 giờ.
* **Shipping Manager:** Chuẩn hóa thao tác quét mã Goods Issued thời gian thực để kích hoạt billing.
* **Customer Service Lead:** Triển khai luồng thông báo tự động về tình trạng đơn hàng cho khách.
