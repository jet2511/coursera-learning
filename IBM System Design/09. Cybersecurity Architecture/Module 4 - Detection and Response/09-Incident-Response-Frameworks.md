# Incident Response Frameworks (Các khung ứng phó sự cố)

## 1. Giới thiệu
Hai khung ứng phó sự cố phổ biến nhất được tạo ra bởi **NIST** và **SANS**. Cả hai đều có các bước tương đồng nhằm cung cấp một phương pháp tiếp cận có hệ thống để xử lý hậu quả của sự cố bảo mật.

---

## 2. NIST Incident Response Framework (4 giai đoạn)
1. **Preparation (Chuẩn bị)**: Đầu tư hạ tầng bảo mật vững chắc và đào tạo nhân viên định kỳ về quy trình ứng phó sự cố.
2. **Detection and Analysis (Phát hiện & Phân tích)**: Hệ thống giám sát phát hiện bất thường và cảnh báo; đội ngũ IT/SOC phân tích log để xác định nguyên nhân (ví dụ: phát hiện mã độc đang đánh cắp dữ liệu khách hàng).
3. **Containment, Eradication, and Recovery (Khoanh vùng, Loại bỏ & Phục hồi)**:
   - *Containment*: Cô lập server bị ảnh hưởng khỏi mạng để chặn rò rỉ dữ liệu.
   - *Eradication*: Xóa bỏ mã độc khỏi hệ thống.
   - *Recovery*: Khôi phục dữ liệu từ bản backup gần nhất và đưa hệ thống trở lại mạng sau khi đã vô hiệu hóa hoàn toàn mối đe dọa.
4. **Post-Incident Activity (Hoạt động sau sự cố)**: Điều tra nguyên nhân gốc rễ (ví dụ: email spear-phishing), củng cố biện pháp bảo mật, cập nhật đào tạo nhân viên và kiểm toán bảo mật toàn hệ thống.

---

## 3. SANS Incident Response Framework (6 giai đoạn)
1. **Preparation (Chuẩn bị)**: Thành lập đội ngũ ứng phó sự cố với vai trò, trách nhiệm rõ ràng; thiết lập hệ thống logging và monitoring.
2. **Identification (Nhận diện)**: Hệ thống giám sát cảnh báo sự cố (ví dụ: website sập đột ngột) và điều tra xác định nguyên nhân (ví dụ: tấn công DDoS).
3. **Containment (Khoanh vùng)**: Triển khai chiến lược giảm thiểu ngay lập tức (ví dụ: định tuyến lại lưu lượng qua mạng server toàn cầu để phân tải, tạm thời đưa server bị ảnh hưởng offline).
4. **Eradication (Loại bỏ)**: Chặn các IP tấn công và vá các lỗ hổng có thể đã bị khai thác.
5. **Recovery (Phục hồi)**: Đưa server trở lại hoạt động sau khi mối đe dọa được vô hiệu hóa; kiểm tra toàn diện chức năng và bảo mật trước khi vận hành bình thường.
6. **Lessons Learned (Bài học kinh nghiệm)**: Phân tích sâu nguyên nhân cuộc tấn công, cải thiện biện pháp bảo mật, đào tạo bổ sung cho nhân viên và nâng cấp chiến lược phòng chống cho tương lai.

---

## 4. Kết luận
- Việc lựa chọn NIST hay SANS không quan trọng bằng việc **tổ chức phải áp dụng một phương pháp chuẩn**.
- Một kế hoạch ứng phó sự cố (Incident Response Plan) rõ ràng giúp nhận diện, giảm thiểu và ngăn chặn sự cố leo thang thành khủng hoảng, đảm bảo phản ứng nhanh và giảm thiểu gián đoạn kinh doanh.
