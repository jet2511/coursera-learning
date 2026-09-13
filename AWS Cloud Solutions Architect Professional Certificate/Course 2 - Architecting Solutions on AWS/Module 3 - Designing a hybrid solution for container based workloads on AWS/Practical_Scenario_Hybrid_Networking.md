# Practical Scenario: Hybrid Networking & Connectivity Design (Insurance Company Case)

## 1. Overview & Business Challenge
Doanh nghiệp bảo hiểm (Customer #3) di chuyển một số containerized workloads lên AWS theo mô hình **Hybrid Cloud**.
* **Yêu cầu then chốt:**
  * **Low & Predictable Latency:** Độ trễ thấp và ổn định cho các nghiệp vụ lõi.
  * **High Uptime & SLA:** Tính sẵn sàng và ổn định cao cho ứng dụng quan trọng (mission-critical).
  * **Seamless Communication:** Liên lạc thông suốt, bảo mật giữa on-premises data centers và AWS VPCs.

---

## 2. Primary Connection Method: AWS Direct Connect (DX)

* **Khuyến nghị:** Chọn **AWS Direct Connect (DX)** làm phương thức kết nối chính.
* **Lý do lựa chọn:**
  * **Dedicated Physical Connection:** Thiết lập kênh truyền riêng biệt, bỏ qua hoàn toàn mạng Internet công cộng.
  * **Ultra-Low & Consistent Latency:** Đảm bảo độ trễ tối thiểu, tránh biến động jitter do nghẽn mạng công cộng.
  * **Enterprise-Grade SLA & High Throughput:** Băng thông lớn (1 Gbps - 100 Gbps), đáp ứng tải công việc xử lý dữ liệu bảo hiểm nhạy cảm.

---

## 3. Complementary Services for Resiliency, Security & Scalability

Để hoàn thiện kiến trúc hybrid cloud đạt chuẩn doanh nghiệp (robust, secure, and scalable), Direct Connect cần kết hợp với:

### a. AWS Transit Gateway (Scalability & Centralized Hub)
* Đóng vai trò Hub trung tâm theo mô hình **Hub-and-Spoke**.
* Cho phép một kết nối Direct Connect liên kết linh hoạt tới hàng chục/hàng trăm VPC và microservices mà không cần cấu hình full-mesh phức tạp.

### b. Redundancy & High Availability (Failover Strategy)
* **AWS Site-to-Site VPN:** Giải pháp failover tự động, tiết kiệm chi phí để duy trì uptime khi đường Direct Connect gặp sự cố.
* **Secondary Direct Connect Link:** Với các hệ thống cực kỳ quan trọng, sử dụng đường DX thứ 2 khác địa điểm PoP (Direct Connect Location) để đạt mức 99.99% SLA.

### c. Encryption in Transit (Security & Compliance)
* Dữ liệu bảo hiểm/tài chính đòi hỏi bảo mật nghiêm ngặt:
  * **MACsec (Layer 2 encryption):** Mã hóa ở cấp độ đường truyền phần cứng (line-rate) giữa router on-premises và AWS Direct Connect port.
  * **IPsec VPN over Direct Connect (Layer 3 encryption):** Tạo VPN tunnel chạy qua đường Direct Connect để mã hóa end-to-end.

### d. Direct Connect Gateway (Multi-Region / Multi-VPC)
* Cho phép kết nối Direct Connect on-premises truy cập tới nhiều VPC trải rộng trên nhiều AWS Regions khác nhau mà không cần mua thêm đường truyền vật lý tại từng Region.

---

## 4. Architectural Summary Diagram

```text
[On-Premises Data Center]
      │
      ├─────────────────────── (Primary: Low Latency / Dedicated) ───────────────────────┐
      │                                                                                  ▼
[Customer Router] ──── (MACsec / IPsec Encryption) ────> [AWS Direct Connect Location] ──> [Direct Connect Gateway]
      │                                                                                  │
      ├─────────────────────── (Backup / Failover) ──────────────────────────────────────┤
      │                                                                                  ▼
      └──────── (Public Internet / Encrypted IPsec) ───> [AWS Site-to-Site VPN] ────────> [AWS Transit Gateway]
                                                                                                  │
                                                                   ┌──────────────────────────────┼──────────────────────────────┐
                                                                   ▼                              ▼                              ▼
                                                            [Core Services VPC]            [Workloads VPC A]              [Workloads VPC B]
```
