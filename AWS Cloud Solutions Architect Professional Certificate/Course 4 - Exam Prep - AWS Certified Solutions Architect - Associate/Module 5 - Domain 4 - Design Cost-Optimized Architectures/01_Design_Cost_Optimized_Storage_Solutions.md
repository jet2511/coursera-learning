# Design Cost-Optimized Storage Solutions

## 1. Tổng quan & Nguyên tắc cốt lõi
- **Mục tiêu:** Thiết kế và chọn lựa giải pháp lưu trữ trên AWS vừa đáp ứng yêu cầu kỹ thuật vừa tối ưu chi phí (Cost-Effective / Cost-Optimized).
- **Nguyên tắc chọn đúng loại lưu trữ (Storage Types):**
  - **Object Storage:** Amazon S3 (không dùng S3 khi ứng dụng yêu cầu file system/block storage).
  - **Block Storage:** Amazon EBS (gắn với EC2), Ephemeral Instance Store (tạm thời, kèm theo giá instance).
  - **File Storage:** Amazon EFS, FSx.

---

## 2. Chiến lược tối ưu chi phí theo từng dịch vụ lưu trữ

### A. EC2 Instance Store vs Amazon EBS
- **Instance Store (Ephemeral Storage):**
  - Chi phí lưu trữ rẻ nhất (đã bao gồm trong chi phí chạy hàng giờ của EC2 instance).
  - Không dùng cho dữ liệu bền vững dài hạn (mất khi dừng/terminate instance).
- **Amazon EBS (Persistent Storage):**
  - Chi phí tính riêng ngoài EC2.
  - **Right-sizing:** Tránh over-provisioning dung lượng lưu trữ.
  - **Volume Type Switching:** 
    - Đánh giá IOPS thực tế sử dụng so với IOPS đang trả tiền.
    - Chuyển từ *Provisioned IOPS (io1/io2)* sang *General Purpose (gp2/gp3)* nếu workload đáp ứng tốt với burst/baseline IOPS.
  - **Xóa Unattached Volumes:** Sử dụng **AWS Trusted Advisor** để phát hiện và xóa các volume EBS không gắn vào EC2 nào (kèm chiến lược snapshot archive phù hợp trước khi xóa).
  - **Tự động hóa vòng đời Snapshot:** Dùng **Amazon Data Lifecycle Manager (DLM)** hoặc **AWS Backup** để tự động tạo và xóa các snapshot/backup cũ đã hết hạn lưu trữ.

---

### B. Amazon S3 (Object Storage)
- **Đặc điểm:** Chi phí rẻ, độ bền 11 số 9 (99.999999999%), không giới hạn dung lượng lưu trữ.
- **Tối ưu theo Storage Classes (Tiers):**
  - Cân nhắc giữa **Storage cost** (chi phí lưu trữ) và **Retrieval cost/time** (chi phí/thời gian truy xuất).
  - **S3 Lifecycle Policies:** Tự động chuyển đổi toàn bộ object trong bucket sang tier thấp hơn (Standard $\to$ Standard-IA $\to$ Glacier $\to$ Glacier Deep Archive) hoặc tự động xóa sau khoảng thời gian xác định.
  - **S3 Intelligent-Tiering:** Tự động theo dõi access patterns và chuyển từng object sang access tier tối ưu nhất mà không ảnh hưởng hiệu năng và không tốn phí retrieval.
  - **Requester Pays Buckets:** Cấu hình để bên yêu cầu tải dữ liệu (requester) chịu chi phí request và data transfer/download thay vì bucket owner.

---

### C. Di chuyển dữ liệu lớn & Môi trường Hybrid (Data Migration)
- **Các công cụ hỗ trợ:** AWS DataSync, AWS Snow Family, AWS Transfer Family, AWS Storage Gateway.
- **Di chuyển dữ liệu lớn (Vài TB đến PB - ví dụ 250 TB archived data):**
  - **AWS Snowball / Snow Family:** Giải pháp nhanh nhất, an toàn và tiết kiệm chi phí nhất để import dữ liệu từ On-Premises lên S3 mà không làm nghẽn băng thông mạng Internet.
- **Tối ưu chi phí Data Transfer:**
  - Sử dụng **Amazon CloudFront** (CDN) để cache dữ liệu gần người dùng hơn, giảm chi phí truyền dữ liệu ra ngoài (Data Transfer Out).
  - Sử dụng **AWS Direct Connect** cho kết nối dedicated private băng thông lớn giữa On-Premises và AWS.

---

## 3. Công cụ Giám sát & Quản lý Chi phí (Cost Monitoring & Governance)

| Dịch vụ / Tính năng | Vai trò trong Tối ưu Chi phí |
| :--- | :--- |
| **AWS Cost Explorer** | Báo cáo tài chính trực quan cấp cao (high-level interactive reports), hỗ trợ drill-down xem chi tiết theo service/tag. |
| **AWS Cost and Usage Reports (CUR)** | Báo cáo chi tiết nhất về chi phí theo từng giờ, ngày, tháng, product, resource tag. |
| **AWS Budgets** | Đặt ngưỡng ngân sách, cảnh báo và kích hoạt **hành động tự động (automated actions)** khi chi phí/dự báo vượt ngưỡng. |
| **AWS Trusted Advisor** | Đưa ra khuyến nghị cụ thể: phát hiện unattached EBS volumes, underutilized resources, idle instances. |
| **Cost Allocation Tags** | Gắn thẻ tài nguyên để phân bổ chi phí, lọc và phân tích chi tiết trong Cost Explorer. |
| **AWS Organizations & Control Tower** | Quản lý **Consolidated Billing** (tổng hợp hóa đơn để đạt mức chiết khấu bậc thang theo volume), quản lý tập trung tài nguyên. |
| **Amazon CloudWatch** | Theo dõi metrics tài nguyên (CPU, RAM, Storage, IOPS) để thiết lập baseline cho right-sizing. |
| **AWS Auto Scaling** | Đảm bảo số lượng instance co giãn chính xác theo nhu cầu tải, tránh lãng phí compute. |

---

## 4. Key Exam Takeaways
1. **S3 Lifecycle vs Intelligent-Tiering:**
   - Đã biết trước lịch trình/thời gian lưu trữ $\to$ Dùng **Lifecycle Configuration**.
   - Chưa rõ hoặc access patterns thay đổi bất thường $\to$ Dùng **Intelligent-Tiering**.
2. **EBS Cost Optimization:**
   - Dùng **Trusted Advisor** để tìm volume không gắn (unattached).
   - Dùng **Data Lifecycle Manager (DLM)** để dọn dẹp EBS snapshots cũ.
   - Chuyển đổi volume type (IOPS $\to$ gp2/gp3) nếu không dùng hết IOPS cam kết.
3. **Data Transfer Cost:**
   - Dữ liệu ngoại tuyến lớn (250 TB+) $\to$ Chọn **Snowball**.
   - Giảm egress Internet $\to$ Chọn **CloudFront**.
4. **Báo cáo chi phí:**
   - Báo cáo tài chính trực quan, high-level $\to$ **Cost Explorer**.
   - Báo cáo chi tiết nhất từng giờ/từng tag $\to$ **Cost and Usage Report (CUR)**.
