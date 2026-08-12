# Tóm tắt bài học: Lựa chọn dịch vụ tính toán Serverless (Selecting a Serverless Compute Service)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Phân tích, so sánh các dịch vụ Compute trên AWS và đưa ra lựa chọn phù hợp  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Phân loại dịch vụ Compute trên AWS (aws.amazon.com/products/compute)
AWS chia các dịch vụ tính toán thành các danh mục chính:
1. **Instances (Không phải Serverless):**
   * **Amazon EC2:** Máy chủ ảo truyền thống trên đám mây, cho phép toàn quyền kiểm soát hệ điều hành và cấu hình.
   * **Amazon Lightsail:** Phương thức đơn giản hóa để chạy EC2 cho các dự án nhỏ, cấu hình nhanh.
   * **AWS Batch:** Dịch vụ chạy các tác vụ xử lý theo lô (batch processing).
2. **Containers (Ứng dụng Container):**
   * **Amazon ECS / Amazon EKS:** Các công cụ điều phối container (orchestration).
   * **AWS Fargate:** Nền tảng tính toán serverless dành cho container (không cần quản lý máy chủ EC2 bên dưới).
3. **Serverless (Hoàn toàn phi máy chủ):**
   * **AWS Lambda:** Thực thi mã nguồn theo sự kiện (event-driven), được xây dựng cloud-native để tối ưu hóa lợi ích đám mây.

---

## 2. So sánh và Đánh giá các phương án giải pháp

### 2.1. Tại sao không chọn Amazon EC2?
Mặc dù có thể chuyển dịch nguyên bản hệ thống on-premises lên EC2 (*lift-and-shift*) và hệ thống hoạt động bình thường, nhưng giải pháp này không tối ưu vì nó giữ lại gánh nặng vận hành (vá lỗi OS, quản lý hạ tầng mạng ảo, tự cấu hình Auto Scaling). Mục tiêu là tìm giải pháp **tốt nhất**, chứ không chỉ dừng lại ở giải pháp **chạy được**.

### 2.2. So sánh AWS Fargate vs AWS Lambda
* **AWS Fargate:** Về mặt kỹ thuật, Fargate đáp ứng cực tốt mọi yêu cầu (mở rộng tự động, đẩy log lên CloudWatch, hiệu năng cao, chi phí tối ưu nhờ Fargate Spot). Tuy nhiên, rào cản lớn nhất là **đội ngũ kỹ sư của khách hàng chưa có kinh nghiệm vận hành container**.
* **AWS Lambda:** Là lựa chọn tối ưu nhất. 
  * Đội ngũ phát triển của khách hàng đã bắt đầu học cách viết code cho Lambda và DynamoDB ở các dự án di chuyển trước.
  * Lambda chạy trên các microVM (dùng công nghệ *Firecracker*) - tự động sinh ra khi có request và tự hủy khi hết yêu cầu. Khách hàng hoàn toàn không mất chi phí cho thời gian máy chủ chạy rảnh rỗi (*idle time*).

---

## 3. Khởi dựng kiến trúc mới: Hai khối ghép đầu tiên (Building Blocks)

### Khối 1: AWS Lambda (Thành phần Compute chính)
* Đảm nhận chạy mã nguồn xử lý của Orders Service.
* Cần refactor (viết lại) lại mã nguồn từ monolith thành các hàm độc lập được kích hoạt theo cơ chế Trigger (Sự kiện).

### Khối 2: Amazon API Gateway (Thành phần Web Interface)
* Đóng vai trò làm "cửa ngõ" đứng trước để tiếp nhận các yêu cầu HTTP từ clients và kích hoạt AWS Lambda phía sau.
* **Lợi ích vượt trội:**
  * **Thay thế Web Server truyền thống:** Khách hàng không cần cài đặt hay duy trì Apache/Nginx nữa.
  * **Xử lý trực tiếp tác vụ phụ:** API Gateway có thể tự xử lý việc xác thực (Authentication) và kiểm tra định dạng dữ liệu (Basic Validation), giúp giảm tải dung lượng code cần phải viết trong Lambda.
  * **Giám sát tập trung:** Tích hợp trực tiếp với **Amazon CloudWatch** và **Amazon CloudWatch Logs** để ghi nhận trạng thái hệ thống.
  * Cả API Gateway và Lambda đều có tính năng tự co giãn và tối ưu chi phí cực kỳ hiệu quả.
