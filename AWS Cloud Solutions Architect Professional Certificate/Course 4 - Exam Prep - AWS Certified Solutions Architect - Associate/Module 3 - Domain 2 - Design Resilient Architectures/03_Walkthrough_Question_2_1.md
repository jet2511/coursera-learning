# Walkthrough Question 2.1: Message Deduplication & Exactly-Once Processing (SAA-C03)

## 1. Đề Bài (Scenario)
> **Đề bài:** Một API nhận khối lượng lớn dữ liệu cảm biến (*sensor data*). Dữ liệu này được ghi vào một hàng đợi (*queue*) trước khi được xử lý để tạo các báo cáo dự báo và phân tích xu hướng. Trong kiến trúc hiện tại, một số bản ghi dữ liệu đang bị nhận và xử lý nhiều hơn một lần (**processed more than once**).
> 
> Một Solutions Architect cần điều chỉnh kiến trúc như thế nào để đảm bảo các bản ghi trùng lặp **không bị xử lý lặp lại (duplicate records are not processed)**?

---

## 2. Phân Tích Yêu Cầu & Từ Khóa (Keyword Breakdown)
- **High volume of sensor data:** Cần một giải pháp có khả năng đệm/hàng đợi dữ liệu tốt.
- **Written to queue before being processed:** Kiến trúc hiện tại sử dụng hàng đợi (Queue).
- **Records processed more than once:** Đang gặp vấn đề trùng lặp bản ghi (At-least-once delivery của Standard Queue).
- **Ensure duplicate records are not processed:** Yêu cầu xử lý chính xác một lần (**Exactly-Once Processing**) và loại bỏ trùng lặp (**Deduplication**).

---

## 3. Các Phương Án Lựa Chọn (Options)
- **A.** Configure the API to send the records to Amazon Kinesis Data Streams.
- **B.** Configure the API to send the records to Amazon Kinesis Data Firehose.
- **C.** Configure the API to send the records to Amazon Simple Notification Service (SNS).
- **D.** **Configure the API to send the records to Amazon Simple Queue Service (Amazon SQS) FIFO queue.** *(Đáp án chính xác)*

---

## 4. Giải Thích Chi Tiết & Phân Tích Đáp Án

### Đáp án đúng: D (Amazon SQS FIFO queue)
- **Amazon SQS FIFO Queue** được thiết kế đặc biệt cho các trường hợp yêu cầu:
  1. **Strict Ordering (First-In, First-Out):** Thứ tự tin nhắn gửi và nhận được bảo toàn tuyệt đối.
  2. **Exactly-Once Processing:** Tin nhắn được gửi đúng một lần và tồn tại cho đến khi consumer xử lý và xóa nó.
  3. **Message Deduplication:** SQS FIFO tự động loại bỏ các tin nhắn trùng lặp trong khoảng thời gian 5 phút (*Deduplication ID / Content-based Deduplication*), ngăn chặn hoàn toàn việc duplicate records.

### Tại sao các đáp án khác sai?
- **A (Amazon Kinesis Data Streams) — SAI:**
  - Kinesis Data Streams cung cấp bảo đảm phân phối ít nhất một lần (**At-least-once delivery**). 
  - Vẫn có thể sinh ra bản ghi trùng lặp do **Producer retries** (gặp lỗi mạng khi gửi bản ghi và gửi lại) hoặc **Consumer retries** (worker crash trong quá trình xử lý checkpoint). Muốn chống trùng lặp trên Kinesis, ứng dụng phải tự cài đặt cơ chế Deduplication ở phía Consumer (Idempotent processing).
- **B (Amazon Kinesis Data Firehose) — SAI:**
  - Tương tự Data Streams, Kinesis Data Firehose cũng có thể gây trùng lặp dữ liệu khi tải vào S3/Redshift nếu có sự cố retry trong quá trình đẩy dữ liệu.
- **C (Amazon SNS) — SAI:**
  - SNS là dịch vụ **Pub/Sub (Publish/Subscribe Messaging)**, không phải là hàng đợi lưu trữ đệm (Queuing). 
  - SNS đẩy tin nhắn tức thời (Push-based) và không đệm giữ tin nhắn cho worker pull về xử lý batch/báo cáo như yêu cầu đề bài.

---

## 5. Bảng So Sánh Chiến Lược Hàng Đợi & Streaming trên AWS (Exam Quick Reference)

| Dịch vụ | Thứ tự tin nhắn (Ordering) | Cơ chế phân phối (Delivery Guarantee) | Deduplication tự động | Use Case phù hợp |
| :--- | :--- | :--- | :--- | :--- |
| **SQS Standard** | Best-effort ordering | At-least-once delivery | ❌ Không (Ứng dụng phải xử lý Idempotent) | Tải cực lớn, throughput không giới hạn, chấp nhận lặp tin |
| **SQS FIFO** | **Strict FIFO** | **Exactly-once processing** | **✅ Có (Tự động trong 5 phút)** | Giao dịch tài chính, đơn hàng, dữ liệu cảm biến cần chống lặp |
| **SNS Standard** | Best-effort ordering | At-least-once | ❌ Không | Fan-out notification tới nhiều subscribers |
| **SNS FIFO** | Strict FIFO | Exactly-once | ✅ Có | Fan-out tin nhắn có thứ tự sang các SQS FIFO queues |
| **Kinesis Data Streams** | Thứ tự theo Partition Key | At-least-once | ❌ Không (Xử lý ở tầng consumer code) | Real-time analytics, ingest log/stream song song quy mô lớn |

---

## 6. Mẹo Thi SAA-C03 (Exam Tip)
> Khi gặp câu hỏi liên quan đến **Queue** và có yêu cầu **"Prevent duplicates"**, **"Process only once"** hoặc **"Preserve order strictly"** $\rightarrow$ Luôn ưu tiên xem xét giải pháp **Amazon SQS FIFO queue**.
