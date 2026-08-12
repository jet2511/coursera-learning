# Lab Summary: Configure High Availability for Your Application

**Khóa học:** AWS Cloud Technical Essentials  
**Vị trí:** Week 4 - Monitoring & Optimization

---

## 1. Mục tiêu của Lab (Objectives)
Sau khi hoàn thành bài thực hành này, bạn sẽ có khả năng:
* **Review EC2 Instance & Web App:** Xem xét cấu hình hiện tại của Amazon EC2 instance và ứng dụng web danh bạ nhân viên.
* **Tạo Application Load Balancer (ALB) & Target Group:** Thiết lập hệ thống cân bằng tải để điều phối lượng truy cập một cách hiệu quả giữa nhiều Availability Zones (AZs).
* **Tạo Launch Template:** Định nghĩa cấu hình phần cứng, hệ điều hành (AMI), và script khởi chạy ứng dụng (User Data) để làm nền tảng tự động co giãn.
* **Cấu hình Auto Scaling Group (ASG):** Thiết lập nhóm tự động co giãn dựa trên các chính sách giám sát tải CPU.
* **Stress Test:** Thử nghiệm giả lập quá tải để kiểm chứng tính năng tự động mở rộng theo chiều ngang (horizontal scaling) của hệ thống.

---

## 2. Kịch bản Lab (Scenario)
Ứng dụng danh bạ nhân viên (**Employee Directory**) đang hoạt động tốt trên một EC2 instance đơn lẻ nằm trong một public subnet đơn nhất. Nhằm ngăn ngừa rủi ro hệ thống bị quá tải khi lượng truy cập tăng đột biến, bạn được giao nhiệm vụ thiết lập Application Load Balancer và Auto Scaling group để giúp ứng dụng có khả năng co giãn ngang tự động theo nhu cầu thực tế của doanh nghiệp.

---

## 3. Các bước thực hiện chi tiết (Tasks)

### Task 1: Review EC2 Instance và Ứng dụng Web hiện tại
1. Truy cập dịch vụ **EC2** trên AWS Management Console.
2. Tìm instance mang tên `Web Application` đang ở trạng thái *Running*.
3. Dùng liên kết `PublicWebApplicationURL` để truy cập ứng dụng web trên trình duyệt.
4. Điều hướng tới **Administration** -> **Configuration** để ghi nhận Availability Zone (AZ) hiện tại của máy chủ.

### Task 2: Tạo Application Load Balancer
1. **Khởi tạo ALB:** 
   * Tên: `Web-Application-ALB`.
   * Mạng (Network): Chọn **Lab VPC** và chọn tất cả các Availability Zones được liệt kê (ví dụ: `us-west-2a` và `us-west-2b`).
   * Security Group: Gỡ bỏ nhóm mặc định, thêm nhóm có tên chứa `LoadBalancerSG`.
2. **Tạo Target Group:**
   * Chọn loại đích là **Instances**, đặt tên là `lab-app-target-group`.
   * Mở rộng cấu hình nâng cao (*Advanced health check settings*) để cấu hình các ngưỡng giám sát sức khỏe máy chủ:
     * **Healthy threshold:** 2 (Số lần kiểm tra thành công để coi là khỏe mạnh)
     * **Unhealthy threshold:** 5 (Số lần thất bại để coi là không khỏe mạnh)
     * **Timeout:** 20 (Thời gian chờ phản hồi tối đa)
     * **Interval:** 30 (Khoảng thời gian giữa các lần kiểm tra)
   * Đăng ký EC2 instance `Web Application` hiện tại vào làm Target.
3. **Liên kết & Xác thực:**
   * Quay lại giao diện cấu hình ALB, làm mới listener và chọn Target Group vừa tạo.
   * Hoàn tất tạo ALB và chờ trạng thái chuyển từ *provisioning* sang *active*.
   * Dùng **DNS Name** của ALB để truy cập ứng dụng thành công trên trình duyệt.

### Task 3: Tạo Launch Template
Launch Template cung cấp cấu hình chuẩn hóa cho các instance mới được sinh ra bởi ASG:
1. Đặt tên: `lab-app-launch-template`.
2. **AMI:** Chọn bản **Amazon Linux 2023 AMI** mới nhất, kiến trúc 64-bit (x86).
3. **Instance type:** `t3.micro`.
4. **Key pair:** Chọn *Don't include in launch template*.
5. **Security Group:** Chọn nhóm bảo mật chứa tên `LoadBalancerSG`.
6. **Advanced details:**
   * **IAM instance profile:** Chọn `EmployeeDirectoryAppRole` (Cấp quyền đọc ghi S3 và DynamoDB).
   * **Metadata version:** Chọn *V1 and V2 (Token optional)*.
   * **User Data:** Dán script Bash tự động cài đặt các thành phần phụ thuộc khi EC2 khởi động (Cập nhật 3 biến môi trường `IMAGES_BUCKET`, `INSTALLATION_BUCKET`, và `YOUR_DEFAULT_AWS_REGION` lấy từ bảng thông tin phòng Lab):
     ```bash
     #!/bin/bash -ex
     # Cấu hình các biến môi trường từ Lab
     IMAGES_BUCKET=UPDATE_WITH_IMAGES_BUCKET_NAME
     INSTALLATION_BUCKET=UPDATE_WITH_INSTALLATION_BUCKET_NAME
     YOUR_DEFAULT_AWS_REGION=UPDATE_WITH_ACTUAL_REGION

     # Cập nhật hệ thống & Cài đặt Node.js qua NVM
     yum -y update
     aws s3 cp s3://$INSTALLATION_BUCKET/install.sh - | bash
     export NVM_DIR="$HOME/.nvm"
     [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
     nvm install 20

     # Cài đặt stress tool để thử tải
     yum -y install stress

     # Tải mã nguồn ứng dụng từ S3 và giải nén
     mkdir -p /var/app
     aws s3 cp s3://$INSTALLATION_BUCKET/app.zip .
     unzip app.zip -d /var/app/
     cd /var/app/

     # Cấu hình môi trường chạy cho ứng dụng
     export PHOTOS_BUCKET=$IMAGES_BUCKET
     export DEFAULT_AWS_REGION=$YOUR_DEFAULT_AWS_REGION
     export SHOW_ADMIN_TOOLS=1

     # Khởi động ứng dụng
     npm install
     npm start
     ```

### Task 4: Tạo Auto Scaling Group
1. Đặt tên ASG: `app-asg` và liên kết với Launch Template vừa tạo.
2. **Network:** Chọn **Lab VPC** và cả 2 subnet **Public Subnet 1**, **Public Subnet 2**.
3. **Cân bằng tải:** Chọn *Attach to an existing load balancer* và kết nối tới `lab-app-target-group | HTTP`.
4. **Health checks:** Tích chọn *Turn on Elastic Load Balancing health checks*.
5. **Cấu hình kích thước nhóm (Group size):**
   * Desired capacity: 2
   * Minimum capacity: 2
   * Maximum capacity: 4
6. **Scaling Policy:** Thiết lập chính sách **Target tracking scaling policy**:
   * Chỉ số theo dõi: *Average CPU utilization*
   * Ngưỡng kích hoạt co giãn (Target value): 30%
   * Thời gian khởi động (Instance warmup): 300 giây
7. **SNS Notification:** Tạo topic `lab-app-sns-topic` để nhận email thông báo tự động mỗi khi có instance được thêm hoặc bớt trong nhóm. (Nhớ xác nhận Subscription trong email).
8. **Dọn dẹp instance cũ:** Sau khi ASG đã tạo thành công 2 instance mới và chúng đạt trạng thái *healthy* trong Target Group, tiến hành **Terminate** instance `Web Application` gốc để hệ thống hoàn toàn chạy trên hạ tầng co giãn mới.

### Task 5: Thử nghiệm Tính sẵn sàng cao và Co giãn tự động
1. **Kiểm tra tính Sẵn sàng cao (High Availability):**
   * Truy cập DNS Name của ALB và liên tục F5 trang web.
   * Xác minh Availability Zone hiển thị tại trang cấu hình thay đổi linh hoạt giữa các AZ khác nhau.
2. **Kiểm tra tính Co giãn tự động (Auto Scaling):**
   * Tại trang quản trị ứng dụng web, chọn **Stress Application Server For: 10 minutes** để giả lập quá tải CPU lên instance hiện tại.
   * Sau vài phút, kiểm tra tab *Targets* của Target Group. Bạn sẽ thấy ASG tự động tạo thêm các EC2 instance mới (lên tối đa là 4 instances) để phân tải CPU đang bị quá ngưỡng 30%.
   * Kiểm tra hộp thư cá nhân để nhận email thông báo sự kiện thay đổi capacity từ dịch vụ SNS.
