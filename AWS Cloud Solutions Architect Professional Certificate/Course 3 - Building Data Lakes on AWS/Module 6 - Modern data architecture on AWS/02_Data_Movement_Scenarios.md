# Data Movement Scenarios

**Khóa học:** Course 3 - Building Data Lakes on AWS  
**Module:** Module 6 - Modern data architecture on AWS  
**Chủ đề:** Data Movement Scenarios (Các kịch bản luân chuyển dữ liệu)

---

## 1. Bối cảnh & Thách thức (Business Context)

* **Vấn đề thực tế:** Doanh nghiệp thu thập khối lượng dữ liệu khổng lồ từ nhiều silo khác nhau vào Data Lake để phân tích chuyên sâu và chạy AI/ML. Đồng thời, họ cũng sử dụng nhiều kho lưu trữ dữ liệu chuyên biệt (*purpose-built data stores*) như NoSQL, Search Service, Data Warehouse để đáp ứng các bài toán nghiệp vụ khác nhau.
* **Thách thức:** Khi dữ liệu tăng trưởng theo cấp số nhân, việc di chuyển dữ liệu ra/vào Data Lake và qua lại giữa các kho dữ liệu trở nên phức tạp, rời rạc và khó kiểm soát (*complex and messy*).
* **Giải pháp - Modern Data Architecture:** Tích hợp Data Lake, Data Warehouse và các data store chuyên biệt thành một kiến trúc thống nhất, cho phép:
  * Quản trị dữ liệu tập trung (*Unified Governance*).
  * Luân chuyển dữ liệu mượt mà (*Seamless Data Movement*).
  * Mở rộng linh hoạt với chi phí tối ưu (*Scalable & Cost-effective*).

---

## 2. Chi tiết 3 Kịch bản Luân chuyển dữ liệu (Data Movement Patterns)

Trong kiến trúc dữ liệu hiện đại, **Amazon S3 / Data Lake** luôn là trung tâm của hệ sinh thái, được bao quanh bởi các dịch vụ phân tích chuyên biệt. Dòng chảy dữ liệu được phân thành 3 hướng chính:

```
                  ┌───────────────────────────────┐
                  │    Amazon S3 (Data Lake)      │
                  │   [Single Source of Truth]    │
                  └───────┬───────────────▲───────┘
          Inside-Out      │               │   Outside-In
          (Đẩy ra ngoài) │               │   (Nạp vào trong)
                          ▼               │
┌───────────────────────────┐           ┌───────────────────────────┐
│ Purpose-Built Store A     │           │ Purpose-Built Store B     │
│ (Redshift, Neptune, etc.) ├──────────►│ (DynamoDB, Aurora, etc.)  │
└───────────────────────────┘           └───────────────────────────┘
               Around the Perimeter (Không qua Data Lake)
```

---

### 1. Inside-Out Data Movement (Từ trong ra ngoài)
* **Bản chất:** 
  * Data Lake đóng vai trò là **Nguồn chân lý duy nhất (Single Source of Truth)**.
  * Toàn bộ dữ liệu đa dạng (structured từ RDBMS, unstructured từ media/tài liệu) được ingest và lưu trữ tập trung tại Data Lake. Sau đó, **một tập con (*subset*) dữ liệu** được trích xuất và đẩy ra các kho dữ liệu chuyên dụng để phục vụ nhu cầu phân tích đặc thù.
* **Mục đích:** Hỗ trợ các công cụ phân tích chuyên sâu (Search Analytics, Knowledge Graphs, BI Reporting).
* **Use Cases thực tế:**
  * Trích xuất dữ liệu từ S3 nạp vào **Amazon Neptune** để xây dựng đồ thị tri thức (Knowledge Graph).
  * Đẩy log và metadata sang **Amazon OpenSearch Service** để phục vụ phân tích tìm kiếm và dashboard giám sát.
  * Đồng bộ tập dữ liệu đã làm sạch vào **Amazon Redshift** để chạy báo cáo kinh doanh hàng ngày.

---

### 2. Outside-In Data Movement (Từ ngoài vào trong)
* **Bản chất:**
  * Ứng dụng nghiệp vụ ưu tiên sử dụng kho lưu trữ phù hợp nhất với tải vận hành (*operational workload*).
  * Sau đó, dữ liệu từ các kho chuyên biệt này được xuất ngược về Data Lake để phân tích tổng thể hoặc kết hợp với các nguồn dữ liệu khác.
* **Mục đích:** Tận dụng tối đa sức mạnh tính toán phân tán, ETL quy mô lớn và khả năng huấn luyện AI/ML của Data Lake.
* **Use Cases thực tế:**
  * **Ngành Gaming:** Một công ty game sử dụng **Amazon DynamoDB** để lưu trạng thái game (*game state*), thông tin người chơi (*player data*), lịch sử phiên chơi (*session history*) và bảng xếp hạng (*leaderboards*) với độ trễ thấp. Định kỳ, dữ liệu này được export về **Amazon S3 Data Lake** để phân tích hành vi người chơi và cải thiện trải nghiệm game.
  * Trích xuất transaction log từ **Amazon Aurora / RDS** và mạng xã hội đổ vào Data Lake để **Amazon SageMaker** huấn luyện mô hình gợi ý sản phẩm (Recommendation System).

---

### 3. Around the Perimeter Data Movement (Quanh chu vi)
* **Bản chất:**
  * Dữ liệu luân chuyển **trực tiếp giữa các kho dữ liệu chuyên biệt với nhau**, hoàn toàn **không cần đi qua (traverse) Data Lake**.
  * Cả hai dịch vụ đều nằm trong cùng một kiến trúc hiện đại, nhưng giao tiếp điểm - nối - điểm để tối ưu độ trễ và giảm tải I/O.
* **Mục đích:** Giảm tải (*offload*) cho cơ sở dữ liệu chính, tối ưu hiệu năng và phục vụ trực tiếp các ứng dụng chuyên biệt.
* **Use Cases thực tế:**
  * Sao chép hồ sơ khách hàng (*customer profile data*) từ **Cơ sở dữ liệu quan hệ (Relational DB / Aurora)** sang **NoSQL Database (DynamoDB)** để tăng tốc độ phản hồi cho dashboard báo cáo.
  * Đồng bộ dữ liệu từ CSDL tác nghiệp sang **Amazon OpenSearch Service** để giải phóng các truy vấn tìm kiếm toàn văn phức tạp đè lên cơ sở dữ liệu chính.

---

## 3. Bảng tổng hợp so sánh các kịch bản

| Tiêu chí | Inside-Out | Outside-In | Around the Perimeter |
| :--- | :--- | :--- | :--- |
| **Hướng dữ liệu** | Data Lake $\rightarrow$ Specialized Data Store | Specialized Data Store $\rightarrow$ Data Lake | Data Store A $\rightarrow$ Data Store B (Bỏ qua Data Lake) |
| **Vai trò Data Lake** | Trung tâm, **Single Source of Truth** | Nền tảng phân tích tổng hợp & AI/ML | Nằm ngoài luồng truyền, không bị chiếm dụng I/O |
| **Mục đích chính** | Phục vụ phân tích chuyên biệt (Search, Graph, BI) | Phân tích sâu, tổng hợp đa nguồn, ML | Tối ưu hiệu năng, giảm độ trễ, offload tải |
| **Ví dụ AWS thực tế** | • S3 $\rightarrow$ **Neptune** (Knowledge Graph)<br>• S3 $\rightarrow$ **OpenSearch** (Search Analytics)<br>• S3 $\rightarrow$ **Redshift** (Reporting) | • **DynamoDB** (Game data/Leaderboard) $\rightarrow$ S3 (Player Analytics)<br>• **Aurora/RDS** $\rightarrow$ S3 $\rightarrow$ **SageMaker** (ML Models) | • Relational DB $\rightarrow$ **NoSQL DB** (Reporting dashboards)<br>• Aurora/DynamoDB $\rightarrow$ **OpenSearch** (Full-text search) |
