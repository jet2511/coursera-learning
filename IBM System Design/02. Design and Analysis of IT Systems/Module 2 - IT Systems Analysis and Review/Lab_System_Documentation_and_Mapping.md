# Lab: System Documentation and Mapping (ShipCart Case Study)

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Tác giả:** Parikshit Jain  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu bài Lab

1. Xây dựng **Process Flow Diagram (Swimlane)** cho luồng xử lý đơn hàng e-commerce.
2. Xây dựng **System Architecture Diagram theo tầng (Layered Architecture Map)**.
3. Phân tích điểm nghẽn hiệu năng (**Performance Bottleneck**) và đề xuất giải pháp tái cấu trúc (**BPR Improvement**) có luận cứ rõ ràng.

---

## 🏢 Bối Cảnh (Scenario: ShipCart)

- **Doanh nghiệp:** ShipCart – Sàn thương mại điện tử Direct-to-Customer (D2C).
- **Vấn đề:** Trì trệ trong xử lý đơn hàng (fulfillment) và theo dõi vận chuyển (tracking) do các hệ thống bị phân mảnh, thiếu tầm nhìn vào quy trình backend.
- **5 quy trình cốt lõi:**
  1. Đặt hàng (Order Placement)
  2. Xử lý thanh toán (Payment Processing)
  3. Kiểm tra tồn kho (Inventory Check)
  4. Hoàn tất đơn hàng tại kho (Order Fulfillment - Pick & Pack)
  5. Theo dõi vận chuyển (Shipment Tracking)

---

## 🧩 Phần 1: Process Flow Diagram (Swimlane Workflow)

```mermaid
sequenceDiagram
    autonumber
    actor Customer as 👤 Customer
    participant System as 💻 ShipCart System
    actor Warehouse as 🏭 Warehouse Staff
    participant Shipping as 🚚 Shipping Service

    Customer->>System: 1. Đặt hàng (Place Order)
    System->>System: 2. Xử lý thanh toán (Process Payment)
    alt Thanh toán thất bại
        System-->>Customer: Báo lỗi thanh toán & yêu cầu thử lại
    else Thanh toán thành công
        System->>System: 3. Kiểm tra kho (Check Inventory)
        alt Hết hàng (Out of Stock)
            System-->>Customer: Thông báo hết hàng & Hoàn tiền
        else Còn hàng (In Stock)
            System->>Warehouse: 4. Gửi yêu cầu soạn hàng (Order Details)
            Warehouse->>Warehouse: 5. Lấy hàng & Đóng gói (Pick and Pack)
            Warehouse->>Shipping: 6. Bàn giao đơn vị vận chuyển (Handover Package)
            Shipping->>System: 7. Xác nhận nhận hàng & Gửi Tracking Code
            System-->>Customer: 8. Cập nhật mã vận đơn & Link theo dõi
            Customer->>Shipping: 9. Tra cứu hành trình đơn hàng (Track Shipment)
        end
    end
```

---

## 🏗️ Phần 2: System Architecture Diagram (Layered Architecture)

```mermaid
graph TD
    subgraph External_Entities["External Entities (Actors & External Services)"]
        Actor_Customer["👤 Customer"]
        Actor_Warehouse["👷 Warehouse Staff"]
        Ext_Shipping["🚚 Third-Party Shipping API"]
    end

    subgraph Presentation_Layer["1. Presentation Layer"]
        UI_Customer["🌐 Customer Interface (Web / Mobile App)"]
    end

    subgraph Application_Layer["2. Application Layer"]
        OMS["📦 Order Management System (OMS)"]
        PGW["💳 Payment Gateway Service"]
        WMS["🏭 Warehouse Management System (WMS)"]
    end

    subgraph Data_Layer["3. Data Layer"]
        DB_Inventory[("🗄️ Inventory & Product Database")]
        DB_Orders[("🗄️ Orders & Transactions Database")]
    end

    %% Data Flows
    Actor_Customer <-->|Place Order / View Status| UI_Customer
    UI_Customer <-->|Order Request / Status Sync| OMS
    OMS <-->|Process Transaction| PGW
    OMS <-->|Check & Reserve Stock| DB_Inventory
    OMS <-->|Save Order Info| DB_Orders
    OMS <-->|Dispatch Fulfillment Task| WMS
    Actor_Warehouse <-->|Pick / Pack Updates| WMS
    WMS <-->|Update Physical Stock| DB_Inventory
    OMS <-->|Generate Waybill / Tracking Info| Ext_Shipping
    Ext_Shipping -.->|Real-time Tracking Updates| UI_Customer
```

---

## 📊 Phần 3: Performance Analysis & Recommendation

| Hạng mục xem xét | Chi tiết phân tích & Đề xuất |
|---|---|
| **Điểm nghẽn xác định (Bottleneck Identified)** | **Kiểm tra và cập nhật tồn kho thủ công/bất đồng bộ:** Giữa Order Management System (OMS) và CSDL kho (Inventory Database). Dữ liệu kho không cập nhật real-time dẫn đến việc hệ thống nhận đơn hàng cho các sản phẩm đã hết hàng (overselling) → Đơn hàng bị hủy, khách hàng thất vọng và tăng tải công việc xử lý thủ công cho nhân viên kho. |
| **Đề xuất cải tiến (Suggested Improvement)** | **Tích hợp đồng bộ tồn kho thời gian thực (Real-time Inventory Sync):** Triển khai phần mềm quét mã vạch/RFID tự động cập nhật số lượng tồn kho tức thời ngay khi sản phẩm được Pick/Pack hoặc nhập kho; kết nối trực tiếp cơ chế Event-driven giữa WMS và OMS. |
| **Luận cứ & Lợi ích kỳ vọng (Justification & Expected Benefits)** | 1. **Giảm độ trễ xử lý:** Loại bỏ độ trễ cập nhật tồn kho.<br>2. **Giảm thiểu hủy đơn:** Tránh bán vượt số lượng thực tế.<br>3. **Tăng Throughput:** Đẩy nhanh tốc độ xử lý đơn hàng từ khâu đặt đến đóng gói.<br>4. **Nâng cao trải nghiệm khách hàng:** Minh bạch tình trạng hàng hóa và thời gian giao nhận.<br>5. **Tối ưu chi phí vận hành:** Giảm áp lực tra soát thủ công cho nhân sự kho bãi. |

---

## 📝 Tổng Kết Bài Lab

- **Quy trình tổng thể:** Bắt đầu từ việc vẽ Swimlane Workflow để hiểu trách nhiệm từng role $\rightarrow$ Ánh xạ sang Kiến trúc phân tầng (Presentation, Application, Data, External API) để tìm điểm đứt gãy $\rightarrow$ Nhận diện Bottleneck và đưa ra giải pháp BPR.
- **Kỹ năng cốt lõi:** Trực quan hóa hệ thống thực tế (Visual Modeling) là chìa khóa để phân tích nguyên nhân gốc rễ và đề xuất giải pháp kỹ thuật có giá trị kinh doanh thực tiễn.
