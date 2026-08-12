# Tóm tắt Bài học: Hướng dẫn Xây dựng POC - Exercise 1 Walkthrough

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Hướng dẫn từng bước xây dựng Proof of Concept (POC) cho kiến trúc Serverless Orders Service  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## Tổng quan

Video hướng dẫn thực hành xây dựng POC trên AWS Console theo đúng kiến trúc đã thiết kế:
```
API Gateway → SQS → Lambda 1 → DynamoDB → DynamoDB Streams → Lambda 2 → SNS → Email
```

---

## Bước 1: Tạo IAM Policies và Roles

### Các Custom Managed Policies cần tạo

| Policy Name | Dịch vụ | API Actions được cấp phép |
|---|---|---|
| `Lambda-Read-SQS` | SQS | `DeleteMessage`, `ReceiveMessage`, `GetQueueAttributes`, `ChangeMessageVisibility` |
| `Lambda-Write-DynamoDB` | DynamoDB | `PutItem`, `DescribeTable` |
| `Lambda-DynamoDBStreams-Read` | DynamoDB Streams | `GetShardIterator`, `DescribeStream`, `ListStreams`, `GetRecords` |
| `Lambda-SNS-Publish` | SNS | `Publish`, `GetTopicAttributes`, `ListTopics` |

> **Lưu ý:** Phân biệt **Customer Managed Policies** (do bạn tự tạo và bảo trì, cần cập nhật thủ công khi có API mới) và **AWS Managed Policies** (do AWS tạo và tự động cập nhật khi có tính năng mới).

### Các IAM Roles cần tạo

| Role Name | Policies được gắn | Dùng bởi |
|---|---|---|
| `APIGateway-SQS` | AmazonSQSFullAccess (AWS managed) + CloudWatch Logs | API Gateway |
| `Lambda-SQS-DynamoDB` | `Lambda-Read-SQS` + `Lambda-Write-DynamoDB` + `LambdaBasicExecutionRole` | Lambda 1 |
| `Lambda-DynamoDBStreams-SNS` | `Lambda-DynamoDBStreams-Read` + `Lambda-SNS-Publish` + `LambdaBasicExecutionRole` | Lambda 2 |

> **Mẹo thực hành:** Copy và lưu ARN của từng Role vào text editor ngay khi tạo xong để dùng ở các bước sau.

---

## Bước 2: Tạo Amazon SQS Queue

* **Loại Queue:** Standard (không FIFO vì thứ tự không phải yếu tố quan trọng ở đây).
* **Tên:** `POC-Queue`
* **Cấu hình mặc định:** Giữ nguyên tất cả.
* **Access Policy (quan trọng):**
  * **Sender (ai được ghi vào queue):** ARN của role `APIGateway-SQS`
  * **Receiver (ai được đọc từ queue):** ARN của role `Lambda-SQS-DynamoDB`
* Sau khi tạo xong, copy ARN của Queue để dùng cho bước API Gateway.

---

## Bước 3: Tạo Amazon DynamoDB Table

* **Tên bảng:** `orders`
* **Partition Key:** `OrderID`
* **Cấu hình khác:** Giữ mặc định.
* **DynamoDB Streams:** Bật sau khi tạo bảng xong, chọn **New Image** (bao gồm toàn bộ thông tin item mới sau mỗi lần ghi).

> **Tại sao chọn "New Image"?** Lambda 2 sẽ đọc trực tiếp dữ liệu đơn hàng từ stream event. Nếu chỉ chọn Key Attributes, Lambda 2 sẽ không có đủ thông tin để publish sang SNS.

---

## Bước 4: Tạo Lambda 1 (Order Processor: SQS → DynamoDB)

* **Tên:** `POC-Lambda-1`
* **Runtime:** Python 3.9
* **Execution Role:** Chọn role sẵn có `Lambda-SQS-DynamoDB`
* **Trigger:** SQS → chọn `POC-Queue`
* **Code (Python/Boto3):**
  * Import Boto3 và khởi tạo DynamoDB client & table object **ngoài handler** (tối ưu execution environment reuse).
  * Xử lý từng record trong event payload từ SQS.
  * Gọi `table.put_item()` để ghi đơn hàng vào bảng `orders` với UUID làm `OrderID`.

### Kiểm tra (Test event)
* Tạo test event mô phỏng cấu trúc payload mà SQS gửi vào Lambda.
* Xác nhận dữ liệu đã được ghi vào DynamoDB bằng cách vào **Tables → orders → Explore Table Items**.

---

## Bước 5: Tạo Amazon SNS Topic

* **Tên:** `POC-Topic`
* **Loại:** Standard (hỗ trợ nhiều giao thức: SQS, Lambda, HTTP, SMS, Email; FIFO chỉ hỗ trợ SQS).
* **Access Policy:** Chỉnh sửa JSON trực tiếp (Advanced mode) để giới hạn quyền Publish chỉ cho role `Lambda-DynamoDBStreams-SNS`.
* **Subscription:** Tạo subscription với giao thức **Email** để kiểm tra end-to-end flow.
* Sau khi tạo xong, copy ARN của Topic để dùng trong code Lambda 2.

---

## Bước 6: Tạo Lambda 2 (Stream Dispatcher: DynamoDB Streams → SNS)

* **Tên:** `POC-Lambda-2`
* **Runtime:** Python 3.9
* **Execution Role:** Chọn role sẵn có `Lambda-DynamoDBStreams-SNS`
* **Trigger:** DynamoDB → chọn bảng `orders`
* **Code (Python/Boto3):**
  * Khởi tạo SNS client.
  * Đọc records từ DynamoDB Stream event.
  * Kiểm tra nếu event là `INSERT` → lấy dữ liệu từ `NewImage`.
  * Gọi `client.publish(TargetArn=<SNS_TOPIC_ARN>, Message=<payload>, MessageStructure='json')` để gửi sang SNS Topic.

---

## Bước 7: Tạo API Gateway (REST API)

* **Tên API:** `POC-API`, loại REST API.
* **Resource:** `/order`
* **Method:** POST
* **Integration Type:** AWS Service (Direct Integration với SQS — không qua Lambda).
* **Cấu hình Integration:**
  * **Region:** `us-east-1`
  * **AWS Service:** SQS
  * **HTTP Method:** POST
  * **Path Override:** `<AccountNumber>/<QueueName>` (lấy từ cuối ARN của SQS, thay dấu `:` bằng `/`)
  * **Execution Role:** ARN của role `APIGateway-SQS`
* **HTTP Headers:** Thêm header `Content-Type: 'application/x-www-form-urlencoded'`
* **Mapping Template (VTL):** Chuyển đổi JSON payload sang định dạng SQS hiểu được:
  ```
  Action=SendMessage&MessageBody=$input.body
  ```

---

## Bước 8: Kiểm tra End-to-End

1. Vào API Gateway Console → Test method POST `/order` với payload mẫu (ví dụ: `{ "item": "latex gloves", "customerId": "12345" }`).
2. Kiểm tra response: **Status 200** xác nhận API Gateway đã ghi thành công vào SQS.
3. Vào DynamoDB → `orders` → Explore Items: Xác nhận item đã được Lambda 1 ghi vào bảng.
4. Kiểm tra hộp thư email: Xác nhận email notification từ SNS đã được nhận.

### Quy trình Debug từng bước khi gặp lỗi

```
1. API Gateway → SQS: Kiểm tra response Status 200?
        │ Không → Xem CloudWatch Logs của API Gateway
        ▼ Có
2. SQS → Lambda 1 → DynamoDB: Item có xuất hiện trong bảng 'orders'?
        │ Không → Xem CloudWatch Logs của POC-Lambda-1 (thường là lỗi phân quyền IAM)
        ▼ Có
3. DynamoDB Streams → Lambda 2 → SNS: Có nhận được email không?
        │ Không → Xem CloudWatch Logs của POC-Lambda-2
        │         Kiểm tra DynamoDB Stream đã bật chưa?
        │         Kiểm tra Lambda 2 có đủ quyền publish SNS không?
        │         Kiểm tra địa chỉ email subscription có chính xác không?
        ▼ Có → Hệ thống hoạt động đúng!
```

---

## Bước 9: Dọn dẹp tài nguyên (Cleanup)

Xóa theo thứ tự để tránh dependency errors:
1. DynamoDB Table (tự động xóa Stream kèm theo)
2. Lambda Functions (cả 2)
3. API Gateway
4. SQS Queue
5. SNS Topic

---

## Thử thách nâng cao (Bonus Challenge)

Thay vì thực hiện mọi thứ bằng AWS Console (point-and-click), hãy thử:
* Sử dụng **AWS CLI** để tạo toàn bộ các tài nguyên qua command line.
* Hoặc sử dụng **AWS CloudFormation** / **AWS SAM** để viết toàn bộ kiến trúc dưới dạng Infrastructure as Code (IaC).
