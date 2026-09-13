# Lab 3: Build a Data Lake using AWS Lake Formation

## 1. Tổng quan Lab (Lab Overview & Architecture)
- **Mục tiêu:** Xây dựng Data Lake với AWS Lake Formation, sử dụng AWS Glue Crawler để tự động quét schema dữ liệu từ S3, tạo Glue ETL Job chuyển đổi dữ liệu từ CSV sang Apache Parquet (dạng Columnar format), phân quyền truy cập qua Lake Formation và kiểm chứng hiệu năng truy vấn trên Amazon Athena.
- **Kiến trúc luồng xử lý:**
  1. `S3 Bucket` (chứa `data/movies_csv/movies.csv`) $\rightarrow$ Đăng ký Data Lake Location trong **AWS Lake Formation**.
  2. Tạo Database `movies-db` trong **AWS Glue Data Catalog**.
  3. Dùng **AWS Glue Crawler** quét S3 data $\rightarrow$ Tạo table metadata `data`.
  4. Phân quyền `SELECT` qua **Lake Formation** $\rightarrow$ Truy vấn thử nghiệm với **Amazon Athena**.
  5. Tạo **AWS Glue Visual ETL Job** (`ParquetConversion`) $\rightarrow$ Convert dữ liệu CSV sang Parquet lưu về S3 `ParquetDataLocation`.
  6. Chạy lại Crawler $\rightarrow$ Tạo bảng `movies_parquet` và `movies_csv`.
  7. So sánh hiệu năng truy vấn (Data Scanned & Execution Time) giữa CSV và Parquet trên **Athena**.

---

## 2. Hướng dẫn thực hành từng bước (Step-by-Step Guide)

### Task 1: Khám phá môi trường Lab (Explore Lab Environment)
1. Mở AWS Console, tìm kiếm dịch vụ **S3**.
2. Chọn bucket có tiền tố `databucket...`.
3. Kiểm tra 2 folder chính:
   - `data/`: Nơi chứa dataset nguồn (`movies_csv/movies.csv` chứa dữ liệu phim 1920-2018).
   - `results/`: Thư mục lưu kết quả truy vấn Athena.

---

### Task 2: Cấu hình AWS Lake Formation (Set up Lake Formation)

#### Task 2.1: Đăng ký Amazon S3 Data Storage
1. Vào **AWS Lake Formation** console.
2. Nếu xuất hiện popup *Welcome to Lake Formation*, giữ mặc định **Add myself** $\rightarrow$ chọn **Get started**.
3. Menu trái $\rightarrow$ chọn **Data lake locations** (trong mục Administration) $\rightarrow$ bấm **Register location**.
4. Cấu hình:
   - **Amazon S3 path:** Dán giá trị `SourceDataLocation` (cung cấp ở panel trái bài lab).
   - **IAM role:** Chọn `LakeFormationServiceRole`.
   - Bấm **Register location**.
5. Menu trái $\rightarrow$ chọn **Data locations** (trong mục Permissions) $\rightarrow$ bấm **Grant**.
6. Cấu hình cấp quyền:
   - **IAM users and roles:** Chọn `AdminGlueServiceRole`.
   - **Storage locations:** Dán giá trị `SourceDataLocation`.
   - Bấm **Grant**.

#### Task 2.2: Tạo Database trong Data Catalog
1. Menu trái $\rightarrow$ chọn **Databases** (trong mục Data catalog) $\rightarrow$ bấm **Create database**.
2. Cấu hình:
   - **Name:** `movies-db`
   - **Location:** Dán giá trị `SourceDataLocation`.
   - Bấm **Create database**.

---

### Task 3: Thu thập Metadata bằng AWS Glue Crawler (Crawl data)

#### Task 3.1 & 3.2: Tạo và chạy Crawler
1. Tìm kiếm và mở dịch vụ **AWS Glue**.
2. Menu trái $\rightarrow$ **Tables** $\rightarrow$ bấm **Add tables using crawler**.
3. Cấu hình:
   - **Name:** `movies-table` $\rightarrow$ **Next**.
   - Bấm **Add a data source** $\rightarrow$ chọn S3 path dán `SourceDataLocation` $\rightarrow$ **Add an S3 data source** $\rightarrow$ **Next**.
   - **Existing IAM role:** Chọn `AdminGlueServiceRole` $\rightarrow$ **Next**.
   - **Target database:** Chọn `movies-db` $\rightarrow$ **Next**.
   - Bấm **Create crawler**.
4. Bấm **Run crawler**. Đợi trạng thái chuyển từ `RUNNING` $\rightarrow$ `STOPPING` $\rightarrow$ `READY` (State: `Completed`).

#### Task 3.3 & 3.4: Cấp quyền truy cập Table qua Lake Formation
1. Chuyển sang **AWS Lake Formation** console $\rightarrow$ Menu trái chọn **Tables** (dưới Data Catalog).
2. Tích chọn bảng `data` $\rightarrow$ chọn **Actions** $\rightarrow$ **Grant**.
3. Cấu hình:
   - **Principals (IAM users and roles):** Chọn role chứa `AWSLabsUser` (role hiện tại của bạn).
   - **Table permissions:** Tích `Select`.
   - **Grantable permissions:** Tích `Select`.
   - Bấm **Grant**.

#### Task 3.5: Truy vấn kiểm tra trên Amazon Athena
1. Mở dịch vụ **Athena** $\rightarrow$ chọn **Launch query editor** (nếu có popup workgroup, bấm **Acknowledge**).
2. Xác nhận Database chọn `movies-db`. Chạy query:
   ```sql
   SELECT * FROM "data" LIMIT 10;
   ```
3. **Challenge A (Đếm phim thể loại Action):**
   ```sql
   SELECT COUNT(*) AS action_movies FROM "data" WHERE genres_0 = 'Action';
   ```
   *(Kết quả trả về chính xác: 1002 bản ghi)*.

---

### Task 4: Chuyển đổi dữ liệu sang Parquet bằng AWS Glue ETL (Transform data)

#### Task 4.1: Tạo Glue Visual ETL Job
1. Mở **AWS Glue** $\rightarrow$ Menu trái chọn **ETL Jobs** $\rightarrow$ chọn **Visual ETL**.
2. **Thêm Source node:**
   - Tab *Sources* $\rightarrow$ chọn **AWS Glue Data Catalog**.
   - Cấu hình Source: **Database:** `movies-db`, **Table:** `data`.
3. **Thêm Target node:**
   - Bấm icon dấu `+` $\rightarrow$ Tab *Targets* $\rightarrow$ chọn **Amazon S3**.
   - Cấu hình Target:
     - **Format:** `Parquet`
     - **Compression Type:** `Uncompressed`
     - **S3 Target Location:** Dán giá trị `ParquetDataLocation` (từ panel bài lab).
4. **Cấu hình Job details:**
   - Chọn tab **Job details** ở thanh công cụ.
   - **Name:** `ParquetConversion`
   - **IAM Role:** `AdminGlueServiceRole`
   - Mở rộng *Advanced properties* $\rightarrow$ **Script filename:** `ParquetConversion.py`.
   - Mục *Connections* $\rightarrow$ **Additional network connections:** Chọn `GlueNetworkConnection`.
5. Bấm **Save** $\rightarrow$ Bấm **Run**.
6. Chuyển sang tab **Runs** theo dõi đến khi status chuyển sang **Succeeded**.

#### Task 4.2 & 4.3: Crawl lại dữ liệu Parquet và cấp quyền
1. Vào lại **AWS Glue** $\rightarrow$ **Crawlers** $\rightarrow$ chọn `movies-table` $\rightarrow$ bấm **Run**. Đợi crawler hoàn tất.
2. Lúc này trong Data Catalog sẽ có các bảng: `data`, `movies_csv`, `movies_parquet`.
3. Mở **Lake Formation** $\rightarrow$ **Tables** $\rightarrow$ chọn bảng `movies_csv` và `movies_parquet` $\rightarrow$ **Actions** $\rightarrow$ **Grant**:
   - Cấp quyền `Select` (cả Table permissions và Grantable permissions) cho role chứa `AWSLabsUser`.

#### Task 4.4: So sánh hiệu năng Athena Query (CSV vs Parquet)
1. Chạy query trên dữ liệu **CSV**:
   ```sql
   SELECT COUNT(*) AS action_movies FROM "movies_csv" WHERE genres_0 = 'Action';
   ```
2. Chạy query trên dữ liệu **Parquet**:
   ```sql
   SELECT COUNT(*) AS action_movies FROM "movies_parquet" WHERE genres_0 = 'Action';
   ```
3. **Kết luận so sánh (Key Takeaway):**
   - **Số kết quả:** Đều ra 1002 bản ghi.
   - **Data scanned (Dữ liệu quét):** Parquet có dung lượng quét **nhỏ hơn đáng kể** so với CSV nhờ cơ chế lưu trữ dạng cột (Columnar Storage) và Column Pruning (chỉ đọc đúng cột `genres_0`), giúp giảm chi phí truy vấn Athena ($5/TB scan) và tăng tốc độ xử lý khi dữ liệu lên tới hàng triệu dòng.
