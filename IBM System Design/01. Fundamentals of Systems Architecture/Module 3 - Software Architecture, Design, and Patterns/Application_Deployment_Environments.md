# Môi trường Triển khai Ứng dụng (Application Deployment Environments)

Tài liệu này tổng hợp các kiến thức về các loại môi trường ứng dụng trong vòng đời phát triển phần mềm và các tùy chọn triển khai hạ tầng (on-premises và cloud).

---

## 1. Môi trường Ứng dụng (Application Environment) là gì?
Là sự kết hợp của các tài nguyên phần cứng và phần mềm cần thiết để chạy một ứng dụng, bao gồm:
* Mã nguồn ứng dụng hoặc các tệp thực thi nhị phân (binary executables).
* Ngăn xếp phần mềm (software stack) như hệ điều hành, thư viện, middleware và ứng dụng bên thứ ba.
* Thành phần mạng và cơ sở hạ tầng.
* Phần cứng vật lý hoặc ảo hóa (CPU, RAM, bộ lưu trữ).

---

## 2. Các Môi trường Tiền sản xuất (Pre-production Environments)
Đây là các môi trường mà ứng dụng trải qua trong các giai đoạn chuẩn bị trước khi phát hành chính thức:
* **Môi trường Phát triển (Development - Dev):** Nơi lập trình viên trực tiếp viết mã nguồn (thường là máy trạm cá nhân của lập trình viên).
* **Môi trường Kiểm thử (Quality Assurance - QA / Testing):** Nơi đội ngũ kiểm thử (QA) thực thi các bài test để đánh giá chất lượng các thành phần ứng dụng.
* **Môi trường Staging (Dự phòng sản xuất):** Môi trường được cấu hình sao cho sao chép (replicate) giống với môi trường production nhất có thể, dùng để chạy thử nghiệm cuối cùng trước khi go-live (không mở cho người dùng chung).

---

## 3. Môi trường Sản xuất (Production Environment - Prod)
* Là môi trường chạy thực tế của ứng dụng để phục vụ tất cả người dùng cuối (có thể lên đến hàng ngàn hoặc hàng triệu người dùng đồng thời).
* Khác với các môi trường pre-production, môi trường Prod bắt buộc phải tính toán và xử lý tải ứng dụng thực tế (load).
* Phải đáp ứng nghiêm ngặt các yêu cầu phi chức năng như **bảo mật (security), độ tin cậy (reliability), khả năng mở rộng (scalability)**, do đó cấu trúc hạ tầng Prod phức tạp hơn nhiều so với các môi trường còn lại.

---

## 4. Các Tùy chọn Triển khai Hạ tầng (Deployment Options)

### A. Triển khai Tại chỗ (On-premises)
* Hệ thống và cơ sở hạ tầng được đặt bên trong cơ sở vật lý của tổ chức, thường nằm sau tường lửa (firewall) để ngăn chặn truy cập trái phép.
* **Ưu điểm:** Khả năng kiểm soát cao, tính bảo mật tối đa đối với ứng dụng và dữ liệu nhạy cảm.
* **Nhược điểm:** Tổ chức phải tự chịu trách nhiệm mua sắm phần cứng, hạ tầng mạng, bảo trì và vận hành. Chi phí đầu tư ban đầu và vận hành thường đắt đỏ hơn so với Cloud.

### B. Triển khai Điện toán Đám mây (Cloud Deployments)
Được chia thành 3 mô hình triển khai chính:
1. **Public Cloud (Đám mây công cộng):** 
   * Tận dụng hạ tầng hỗ trợ phần mềm qua Internet mở trên phần cứng thuộc sở hữu của nhà cung cấp Cloud (AWS, Azure, GCP, IBM Cloud...).
   * Phần cứng và tài nguyên được chia sẻ giữa nhiều công ty (multi-tenancy). 
   * Có ưu thế lớn về khả năng mở rộng nhanh chóng và tối ưu hóa chi phí.
2. **Private Cloud (Đám mây riêng):**
   * Hạ tầng đám mây được cấp phát riêng cho mục đích sử dụng độc quyền của một tổ chức duy nhất. 
   * Có thể chạy trực tiếp tại trung tâm dữ liệu của doanh nghiệp (on-premises) hoặc do bên thứ ba quản lý và vận hành.
   * Mang lại tính bảo mật cao và khả năng tùy biến linh hoạt tối đa.
3. **Hybrid Cloud (Đám mây lai):**
   * Sự kết hợp liền mạch giữa Public Cloud và Private Cloud để tối ưu hóa lợi ích của cả hai mô hình về mặt chi phí, bảo mật, tính linh hoạt và khả năng mở rộng.

---

## 5. Tóm tắt nhanh (Key Takeaways)
1. Các môi trường ứng dụng chính bao gồm: **Development, Testing (QA), Staging, và Production**.
2. Môi trường **Production** đòi hỏi sự phức tạp cao để đáp ứng các tiêu chuẩn phi chức năng (bảo mật, tải thực tế, tính ổn định).
3. Doanh nghiệp có thể chọn triển khai phần cứng vật lý tại chỗ (**On-premises**) hoặc linh hoạt sử dụng các nền tảng đám mây (**Public, Private, hoặc Hybrid Cloud**).
