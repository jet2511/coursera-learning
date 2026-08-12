# Tóm tắt bài học: Phân tích chi tiết yêu cầu của Khách hàng số 1 (Customer #1: Requirements Breakdown)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Phân tích chi tiết yêu cầu nghiệp vụ để định hình thiết kế kiến trúc  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Bối cảnh Monolith & Nhu cầu tái cấu trúc
* **Kiến trúc hiện tại:** Orders Service đang chạy như một khối mã nguồn đơn khối (**Monolithic**). Mọi tác vụ từ tiếp nhận đơn hàng, xử lý logic đến gọi API các dịch vụ hạ nguồn đều được gộp chung trong một gói code duy nhất.
* **Mục tiêu:** Phá vỡ cấu trúc Monolith này thành nhiều thành phần độc lập và thiết lập liên kết lỏng lẻo (**Loosely Coupled**). Điều này nhằm ngăn chặn một lỗi nhỏ ở một tiến trình kéo sập toàn bộ luồng xử lý đơn hàng (loại bỏ điểm lỗi đơn lẻ - *Single Point of Failure*).

---

## 2. Bóc tách và định hướng giải pháp cho 4 yêu cầu cốt lõi

### 2.1. Tự động co giãn (Managed Scaling) cho phần Compute & Database
* **Giải pháp đề xuất:** Ưu tiên tối đa các dịch vụ **Serverless (Không máy chủ)**.
* **Đặc điểm:** Các dịch vụ serverless tự động co giãn lên/xuống theo lưu lượng truy cập thực tế mà không cần kỹ sư can thiệp cấu hình thủ công.
* **Hệ quả thiết kế:** Loại bỏ việc sử dụng Amazon EC2 khỏi các lựa chọn hàng đầu cho phần compute trong kiến trúc này.

### 2.2. Giải phóng liên kết các thành phần (Decoupling) để tăng tính bền vững (Resilience)
* **Giải pháp đề xuất:** Áp dụng mô hình kiến trúc hướng sự kiện (**Event-Driven Architecture**).
* **Đặc điểm:** Chia nhỏ Orders Service thành 3 quy trình độc lập:
  1. *Xác nhận nhận đơn hàng (Order Acceptance)*
  2. *Xử lý đơn hàng (Order Processing)*
  3. *Gọi dịch vụ hạ nguồn (Downstream Calls)*
* **Lợi ích:** Đảm bảo rằng nếu một tiến trình gặp sự cố (ví dụ: API kế toán bị nghẽn), việc tiếp nhận đơn hàng mới từ khách hàng vẫn diễn ra bình thường và không bị gián đoạn.

### 2.3. Giám sát và ghi nhật ký tập trung (Centralized Monitoring & Logging)
* **Giải pháp đề xuất:** Sử dụng **Amazon CloudWatch** và **Amazon CloudWatch Logs**.
* **Lợi ích:** Gom toàn bộ trạng thái hoạt động và log hệ thống về một nơi tập trung duy nhất, giúp việc debug, giám sát lỗi và khắc phục sự cố trở nên nhanh chóng, trực quan. Hầu hết các dịch vụ serverless trên AWS đều tích hợp sẵn CloudWatch rất mượt mà.

### 2.4. Tối ưu hóa Chi phí, Hiệu năng và Vận hành (Cost, Performance, Operational Overhead)
* **Thứ tự ưu tiên quyết định thiết kế:** 
  1. Chi phí (Cost) - Động lực chính.
  2. Hiệu năng (Performance).
  3. Vận hành (Operational Overhead).
* **Ưu điểm của Serverless:** Bản thân mô hình serverless đã tự động tối ưu hóa cả 3 yếu tố này (không trả tiền cho máy chủ rảnh rỗi, tự động đáp ứng hiệu năng, AWS tự lo phần bảo trì hệ thống bên dưới).

---

## 3. Kế hoạch triển khai thiết kế
Hệ thống sẽ được thiết kế từng phần độc lập (block-by-block), lắp ráp thành kiến trúc hoàn chỉnh, và cuối cùng sẽ quay lại phân tích sâu các phương án cấu hình tối ưu để cân bằng tốt nhất giữa chi phí và hiệu suất hoạt động.
