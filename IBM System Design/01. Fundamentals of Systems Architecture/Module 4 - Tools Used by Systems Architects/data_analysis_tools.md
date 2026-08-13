# Data Analysis Tools (Các công cụ phân tích dữ liệu)

Bản tóm tắt nội dung học tập về tầm quan trọng, các phân loại công cụ phân tích dữ liệu cốt lõi và tiêu chí lựa chọn công cụ của Chuyên gia & Kiến trúc sư Hệ thống.

---

### 1. Tầm quan trọng của phân tích dữ liệu
Dữ liệu là trung tâm trong mọi quyết định của chuyên gia hệ thống. Phân tích dữ liệu giúp:
*   Nhận diện các điểm kém hiệu quả trong quy trình làm việc (workflows) hoặc hệ thống.
*   Theo dõi và giám sát các chỉ số hiệu năng hệ thống (metrics).
*   Thấu hiểu hành vi người dùng cuối.
*   Dự đoán các kịch bản/kết quả vận hành hệ thống.
*   Cung cấp bằng chứng thực tế dựa trên dữ liệu để chứng minh và thuyết phục cho các đề xuất thay đổi hệ thống.

---

### 2. Bốn nhóm công cụ phân tích dữ liệu cốt lõi

#### A. Thu thập & Làm sạch dữ liệu (Data Collection & Cleaning)
Bước bắt buộc trước khi phân tích vì dữ liệu thiếu sót hoặc không sạch sẽ dẫn đến các kết luận sai lệch.
*   **Spreadsheet (Excel, Google Sheets):** Nhập dữ liệu, định dạng và làm sạch cơ bản cho tập dữ liệu nhỏ hoặc cần thao tác nhanh.
*   **Python (Pandas, NumPy):** Làm sạch và xử lý các tập dữ liệu lớn, có khả năng tự động hóa và mở rộng tốt hơn nhiều so với bảng tính.
*   **R Language:** Ngôn ngữ lập trình chuyên dụng cho việc làm sạch dữ liệu thống kê, đặc biệt phổ biến trong học thuật và nghiên cứu chuyên sâu.

#### B. Thống kê & Phân tích chuyên sâu (Statistics & Analytics)
Hỗ trợ chạy các kiểm thử thống kê, tìm kiếm mối tương quan và xây dựng mô hình dự báo.
*   **IBM SPSS Statistics:** Giao diện đồ họa (GUI) thân thiện, được sử dụng rộng rãi trong doanh nghiệp và học thuật mà không yêu cầu kỹ năng lập trình.
*   **Python (Scikit-learn, Statsmodels):** Thư viện mạnh mẽ cho việc phân tích tùy biến, xây dựng mô hình học máy (Machine Learning) và phân tích dự báo.
*   **RStudio:** Môi trường phát triển lý tưởng cho ngôn ngữ R để phân tích hồi quy, phân cụm (clustering) và kiểm định giả thuyết.
*   **SQL (Structured Query Language):** Công cụ tối quan trọng để truy vấn và trích xuất dữ liệu trực tiếp từ các cơ sở dữ liệu quan hệ của tổ chức.

#### C. Trực quan hóa dữ liệu (Data Visualization)
Biến các số liệu thống kê khô khan thành các báo cáo trực quan, biểu đồ và dashboard tương tác để thuyết trình với stakeholders.
*   **Tableau:** Công cụ hàng đầu cho phép kết nối đa nguồn dữ liệu và thiết lập các dashboard động, tương tác cao.
*   **Microsoft Power BI:** Tích hợp chặt chẽ với hệ sinh thái Excel và Azure, phù hợp cho các doanh nghiệp dùng Microsoft Stack.
*   **Python (Matplotlib, Seaborn, Plotly):** Cung cấp khả năng tùy biến biểu đồ tối đa, dễ dàng tích hợp trực tiếp vào luồng dữ liệu tự động hoặc mã nguồn.
*   **Excel Charts:** Đơn giản, nhanh chóng và đủ dùng cho các báo cáo nội bộ quy mô nhỏ.

#### D. Trí tuệ doanh nghiệp (Business Intelligence - BI)
Tích hợp phân tích dữ liệu và trực quan hóa theo thời gian thực (real-time dashboards), lập lịch báo cáo tự động và phân quyền truy cập cho từng bộ phận.
*   **Power BI & Tableau:** Hai nền tảng BI toàn diện và phổ biến nhất.
*   **QlikSense:** Nền tảng mạnh về tích hợp dữ liệu từ nhiều nguồn khác nhau và xây dựng mô hình liên kết trực quan.
*   **Google Looker:** Ứng dụng cloud-native chuyên dụng, tích hợp sâu vào hạ tầng Google Cloud Platform (GCP).

---

### 3. Tiêu chí lựa chọn công cụ
Không có công cụ nào tối ưu cho mọi trường hợp; việc lựa chọn phụ thuộc vào các yếu tố:
1.  **Quy mô và phạm vi dự án (Project Size & Scope):** Dự án nhỏ chỉ cần Excel/SQL; dự án lớn hơn yêu cầu Python, Tableau hoặc hệ thống BI.
2.  **Kỹ năng kỹ thuật của đội ngũ (Technical Expertise):** Các công cụ viết mã (Python, R) yêu cầu lập trình viên; các công cụ kéo thả GUI (SPSS, Tableau) phù hợp với người dùng nghiệp vụ.
3.  **Độ phức tạp của dữ liệu (Data Complexity):** Dữ liệu phi cấu trúc hoặc lượng dữ liệu khổng lồ (Big Data) bắt buộc sử dụng Python/R thay vì Excel.
4.  **Nhu cầu của các bên liên quan (Stakeholders' Needs):** Nếu cần chia sẻ dashboard cập nhật theo thời gian thực giữa các phòng ban, các nền tảng BI lớn là bắt buộc.
