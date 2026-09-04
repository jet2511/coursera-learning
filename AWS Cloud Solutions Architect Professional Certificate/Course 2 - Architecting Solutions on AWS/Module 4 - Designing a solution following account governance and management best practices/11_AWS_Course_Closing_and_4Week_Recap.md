# Course 2 Recap & Closing: Architecting Solutions on AWS

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Course Closing & Comprehensive 4-Week Journey Recap  

---

## 1. Tổng kết toàn diện hành trình 4 tuần (Course 2 Retrospective)

Khóa học **Architecting Solutions on AWS** trang bị tư duy và năng lực thiết kế giải pháp cho Solutions Architect thông qua 4 bài toán khách hàng thực chiến đại diện cho 4 xu hướng kiến trúc đám mây chủ đạo:

| Tuần | Chủ đề trọng tâm | Mục tiêu kiến trúc | Công nghệ & Dịch vụ cốt lõi |
| :---: | :--- | :--- | :--- |
| **Week 1** | **Serverless & Event-Driven Web** | Tách rời thành phần (*Decoupled*), tự động co giãn không giới hạn, không cần quản trị máy chủ. | `API Gateway`, `AWS Lambda`, `DynamoDB`, `Amazon SQS`, `Amazon SNS` |
| **Week 2** | **Serverless Big Data Analytics** | Thu thập, lưu trữ dạng Data Lake và phân tích dữ liệu lớn thời gian thực với chi phí tối ưu. | `Kinesis Data Firehose`, `Amazon S3`, `Amazon Athena`, `Amazon QuickSight` |
| **Week 3** | **Hybrid Cloud & Container Migration** | Điều phối container và đồng bộ hóa cơ sở dữ liệu liên tục giữa On-Premises và AWS Cloud. | `ECS Anywhere`, `AWS Systems Manager (SSM)`, `AWS DMS`, `AWS Storage Gateway` |
| **Week 4** | **Multi-Account Governance & Landing Zone** | Thiết lập ranh giới bảo mật cứng, xóa bỏ Root login, tự động hóa cấp phát tài khoản chống drift. | `AWS Organizations`, `AWS Control Tower`, `IAM Identity Center (SSO)`, `AWS Service Catalog`, `CloudTrail` / `CloudWatch Logs` |

---

## 2. Chi tiết từng chặng kiến trúc

### 2.1. Week 1: Serverless & Event-Driven Decoupled Architecture
* **Bài toán:** Xây dựng backend ứng dụng web hiện đại, có khả năng tự động co giãn không giới hạn và tính sẵn sàng cao mà không cần quản trị máy chủ.
* **Mô hình cốt lõi:**
  * **Event-Driven Architecture (Kiến trúc hướng sự kiện):** Phân tách (decouple) các thành phần giao tiếp qua hàng đợi và kênh phát tin.
  * **Dịch vụ chủ lực:**
    * **Amazon API Gateway:** Cổng tiếp nhận RESTful/WebSocket APIs bảo mật.
    * **AWS Lambda:** Xử lý logic nghiệp vụ serverless theo sự kiện.
    * **Amazon DynamoDB:** Cơ sở dữ liệu NoSQL độ trễ mili-giây, scale tự động.
    * **Amazon SQS & SNS:** SQS đệm tin nhắn chống nghẽn; SNS pub/sub phát thông báo đa kênh.

---

### 2.2. Week 2: Serverless Big Data Analytics Pipeline
* **Bài toán:** Thu thập, lưu trữ và phân tích lượng dữ liệu khổng lồ từ chuỗi nhà hàng để phục vụ ra quyết định kinh doanh theo thời gian thực.
* **Mô hình cốt lõi:**
  * **Serverless Analytics:** Phân tích dữ liệu lớn mà không cần dựng cụm Hadoop/Spark tốn kém.
  * **Dịch vụ chủ lực:**
    * **Amazon Kinesis Data Firehose:** Thu nạp luồng streaming logs/orders tự động nén và đổ về S3.
    * **Amazon S3:** Kho dữ liệu trung tâm (**Data Lake**) với độ bền 11 số 9.
    * **Amazon Athena:** Truy vấn trực tiếp file trên S3 bằng SQL chuẩn (Serverless ad-hoc query).
    * **Amazon QuickSight:** Trực quan hóa dữ liệu bằng biểu đồ, dashboard kinh doanh thông minh (BI).

---

### 2.3. Week 3: Hybrid Deployment & Container Migration
* **Bài toán:** Doanh nghiệp muốn hiện đại hóa ứng dụng bằng Container nhưng vẫn phải giữ một phần hệ thống tại trung tâm dữ liệu on-premises để tuân thủ quy định hoặc tận dụng hạ tầng cũ.
* **Mô hình cốt lõi:**
  * **Hybrid Container Orchestration:** Điều phối container đồng nhất cả trên Cloud lẫn On-Premises.
  * **Dịch vụ chủ lực:**
    * **Amazon ECS Anywhere:** Quản lý và chạy container trên hạ tầng on-premises thông qua control plane của Amazon ECS.
    * **AWS Systems Manager (SSM):** Đăng ký và quản lý bảo mật các server on-premises như một tài nguyên AWS.
    * **AWS Database Migration Service (AWS DMS):** Di chuyển và đồng bộ cơ sở dữ liệu liên tục với thời gian downtime tối thiểu.
    * **AWS Storage Gateway:** Cầu nối lưu trữ lai giữa hạ tầng tại chỗ và đám mây AWS (File, Volume, Tape).

---

### 2.4. Week 4: Multi-Account Governance & Enterprise Landing Zone
* **Bài toán:** Khách hàng startup tăng trưởng nhanh, hệ thống bị rối loạn trên một Single Account khổng lồ và đối mặt với rủi ro bảo mật (đăng nhập bằng Root, lỡ tay xóa tài nguyên Prod, áp lực audit SOC 2 / PCI DSS).
* **Mô hình cốt lõi:**
  * **Multi-Account Governance & Landing Zone:** Tạo ranh giới cứng giữa các môi trường, tự động hóa cấp phát tài khoản và thực thi guardrails bảo vệ.
  * **Dịch vụ chủ lực:**
    * **AWS Organizations & SCPs:** Phân tầng OUs, áp dụng Service Control Policies làm hàng rào giới hạn quyền tối đa (chống xóa S3 Prod, khóa quyền Root).
    * **AWS IAM Identity Center (SSO):** Tập trung hóa định danh, phân quyền qua Groups/Permission Sets, xóa bỏ hoàn toàn thói quen dùng Root account.
    * **Centralized CloudTrail & CloudWatch Logs:** Gom toàn bộ nhật ký API audit và app logs về Shared Services Account.
    * **AWS Control Tower & AWS Service Catalog:** Cấp phát tài khoản tự động (Account Factory) chống Account Drift và cung cấp danh mục sản phẩm IT tự phục vụ (Self-Service) an toàn cho developers.

---

## 3. Khẩu quyết của Solutions Architect

> *"Work hard, have fun, and make history."*

Khóa học kết thúc với sự hoàn thiện của bộ tư duy thiết kế giải pháp: **Decoupled**, **Serverless-First**, **Hybrid-Ready**, và **Multi-Account Governed**. Đây là nền tảng vững chắc để tự tin bước vào bài kiểm tra tốt nghiệp (**Final Assessment**) và áp dụng vào các dự án kiến trúc đám mây thực tế.
