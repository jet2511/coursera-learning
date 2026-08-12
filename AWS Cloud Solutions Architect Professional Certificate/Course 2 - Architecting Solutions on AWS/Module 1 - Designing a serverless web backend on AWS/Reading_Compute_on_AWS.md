# Tóm tắt bài học: Tổng quan về Dịch vụ tính toán trên AWS (Compute on AWS)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Chi tiết về AWS Lambda, API Gateway, EC2, và các Dịch vụ Container (ECS, EKS, Fargate)  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. AWS Lambda (Phi máy chủ - Serverless Compute)
* **Định nghĩa:** Dịch vụ thực thi code theo sự kiện (event-driven) trong môi trường runtime cô lập và an toàn (gọi là *Execution Environment*).
* **Thời gian chạy tối đa:** Giới hạn **15 phút/lần thực thi**. Các tiến trình cần thời gian dài hơn bắt buộc phải dùng dịch vụ tính toán khác.
* **Mô hình trách nhiệm:** 
  * **Người dùng:** Chỉ chịu trách nhiệm quản lý và viết mã nguồn (code).
  * **AWS:** Quản lý toàn bộ hạ tầng bên dưới (dung lượng CPU, RAM, mạng, cập nhật hệ điều hành, vá lỗi bảo mật, tự động ghi log và giám sát). Người dùng không thể SSH hay tùy biến hệ điều hành.
* **Mô hình chi phí:** Thanh toán chính xác theo thời gian thực thi thực tế (tính bằng mili-giây). Không có tài nguyên chạy rảnh rỗi (*idling resources*), tối ưu chi phí tối đa.
* **Use Cases phổ biến:** Web/IoT/Mobile backends, xử lý dữ liệu/tệp tin, xử lý luồng sự kiện hoặc tin nhắn.

---

## 2. Amazon API Gateway (Quản lý và Xuất bản API)
* **Định nghĩa:** Dịch vụ quản lý hoàn toàn giúp tạo, phát hành, bảo trì, giám sát và bảo mật các API RESTful hoặc WebSocket ở mọi quy mô.
* **Vai trò trong thiết kế:** Đóng vai trò là "cổng trước" (front door) tiếp nhận request từ internet để chuyển tiếp an toàn tới backend (ở đây là Lambda) mà không làm lộ trực tiếp Lambda ra môi trường ngoài.
* **Tính năng tích hợp sẵn:** 
  * Quản lý lưu lượng truy cập (Traffic management).
  * Hỗ trợ CORS (Cross-Origin Resource Sharing).
  * Xác thực và phân quyền (Authorization & Access control).
  * Điều tiết lưu lượng (Throttling) để chống DDoS.
  * Giám sát hiệu năng và quản lý phiên bản API (Version management).
* **Mô hình chi phí:** Không phí khởi tạo, trả tiền dựa trên số lượng request API nhận được và lượng dữ liệu truyền đi (Data transferred out). Giảm giá theo cấp bậc sử dụng.

---

## 3. Amazon EC2 & AWS Elastic Beanstalk (Máy chủ truyền thống)
* **Amazon EC2:** Máy chủ ảo đám mây, tùy biến cao (chọn hệ điều hành, cài đặt mạng, bảo mật và toàn bộ phần mềm).
  * **Hạn chế:** Người dùng phải chịu gánh nặng vận hành lớn (tự cấu hình dung lượng, tự thiết lập tính chịu lỗi đa AZ, tự vá lỗi bảo mật). Rất khó tối ưu chi phí cho các ứng dụng có lưu lượng truy cập trồi sụt đột biến (*spiky demand*).
* **AWS Elastic Beanstalk:** Nền tảng tự động triển khai và co giãn ứng dụng chạy trên EC2 (PaaS), giúp giảm bớt cấu hình nhưng người dùng vẫn phải chịu trách nhiệm và có toàn quyền kiểm soát các EC2 instance bên dưới.

---

## 4. AWS Container Services (Dịch vụ Container)
Hạ tầng quản lý container của AWS được chia làm 3 mảng: Registry (lưu trữ ảnh), Orchestration (điều phối), và Compute (tính toán).

### 4.1. Amazon ECS (Elastic Container Service)
* Dịch vụ điều phối container độc quyền của AWS, được quản lý hoàn toàn.
* Tích hợp sâu với các dịch vụ bảo mật của AWS, cho phép phân quyền chi tiết xuống tận từng container riêng lẻ.
* Mặc định tích hợp chạy Serverless thông qua **AWS Fargate**.

### 4.2. Amazon EKS (Elastic Kubernetes Service)
* Dịch vụ Kubernetes được quản lý hoàn toàn trên AWS, đảm bảo duy trì độ sẵn sàng cao cho Kubernetes Control Plane trên nhiều AZs.
* Tự động phát hiện và thay thế các instance control plane bị lỗi, hỗ trợ cập nhật phiên bản Kubernetes tự động.
* Tương thích hoàn toàn với bất kỳ môi trường Kubernetes chuẩn nào khác (on-premises hoặc cloud khác).

### 4.3. AWS Fargate (Compute Serverless cho Container)
* Cho phép chạy container trên ECS hoặc EKS mà **không cần quản lý máy chủ ảo EC2**. Người dùng chỉ cần khai báo dung lượng CPU, RAM, cấu hình mạng và IAM.
* **Fargate Spot:** Cho phép tận dụng các tài nguyên dư thừa của AWS với mức giá rẻ hơn nhiều (tiết kiệm đến 70%), phù hợp với các tác vụ chịu được gián đoạn (AWS sẽ thông báo trước 2 phút khi cần lấy lại tài nguyên).

---

## 5. Lý do lựa chọn kiến trúc
* **Tại sao chọn Lambda + API Gateway:** Đáp ứng yêu cầu hạn chế gánh nặng vận hành (*operational overhead*), co giãn tự động tốt đối với lưu lượng trồi sụt (*spiky demand*) và tối ưu chi phí tốt nhất cho ứng dụng web backend.
* **Tại sao không chọn Container (ECS/EKS/Fargate):** Mặc dù Fargate đáp ứng tốt kỹ thuật, khách hàng từ chối do đội ngũ lập trình và vận hành của họ **chưa có kỹ năng quản lý công nghệ container** trong nhà và muốn tập trung học các dịch vụ cloud-native đơn giản hơn trước (Lambda, DynamoDB).
