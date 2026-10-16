# Course Wrap-Up: Data Integration, Storage, and Migration

> Tổng kết toàn bộ khóa học — ôn tập các khái niệm cốt lõi theo 3 chủ đề chính.

---

## 1. Data Integration (Tích hợp dữ liệu)

- **Định nghĩa:** Quá trình kết hợp dữ liệu từ nhiều nguồn khác nhau để tạo ra một **unified view** (góc nhìn thống nhất).
- **Ứng dụng:** Data analysis, reporting, business intelligence.

### Các Integration Patterns phổ biến:
| Pattern | Mô tả |
| :--- | :--- |
| **Point-to-point** | Kết nối trực tiếp từng cặp hệ thống |
| **ETL** (Extract-Transform-Load) | Trích xuất → Biến đổi → Nạp vào đích |
| **ELT** (Extract-Load-Transform) | Trích xuất → Nạp thô → Biến đổi tại đích |
| **Data Virtualization** | Tầng ảo hóa, truy vấn tại chỗ, không di dời dữ liệu |
| **Data Replication** | Sao chép dữ liệu sang hệ thống khác để HA/DR |

### Security Challenges khi tích hợp dữ liệu:
- **Data leakage** — rò rỉ dữ liệu nhạy cảm
- **Complex access control** — kiểm soát truy cập phức tạp
- **Encryption** — cần mã hóa toàn diện (at-rest và in-transit)
- **Authentication & Authorization** — xác thực và phân quyền mạnh

> **Kiến trúc kỹ thuật tốt là điều kiện tiên quyết** để giải quyết các thách thức bảo mật tích hợp dữ liệu.

### Lựa chọn Data Integration Tools:
- So sánh **Open Source** vs **Proprietary** (licensing, pricing, functionality)

---

## 2. Data Storage (Lưu trữ dữ liệu)

### Secondary Storage Types:
| Loại | Đặc điểm |
| :--- | :--- |
| **HDD** | Đĩa quay cơ học, dung lượng lớn, giá rẻ |
| **SSD** | Flash memory, tốc độ cao, IOPS vượt trội |
| **Optical Storage** | Lưu trữ quang học (CD/DVD/Blu-ray) |
| **Magnetic Tape** | Băng từ, chi phí thấp, dùng cho cold archive lâu dài |

### Storage Protocols chính:
- **Fiber Channel (FC)** — tốc độ cực cao, dùng trong Enterprise SAN
- **SCSI** — chuẩn kết nối truyền thống
- **NFS** — giao thức chia sẻ file qua mạng IP (Linux/UNIX)

### Cloud Storage Solutions:
| Loại | Đặc điểm |
| :--- | :--- |
| **Object Storage** | Lưu trữ không có cấu trúc, thích hợp cho media, backup |
| **File Storage** | Phân cấp thư mục, dùng chia sẻ file |
| **Block Storage** | Raw block, dùng cho database, IOPS cao |
| **Hybrid Storage** | Kết hợp on-premises và cloud |

### Data Backup:
- **Mục đích:** Bảo vệ dữ liệu khỏi system failures, cyberattacks, accidental deletion.
- **Backup configurations:** Primary-Replica systems, Cloud backup services.

**Các kỹ thuật Backup:**
| Kỹ thuật | Mô tả |
| :--- | :--- |
| **Full Backup** | Sao lưu toàn bộ dữ liệu |
| **Incremental** | Chỉ sao lưu thay đổi kể từ backup lần cuối |
| **Differential** | Sao lưu thay đổi kể từ Full backup gần nhất |
| **Mirror** | Bản sao tức thời và luôn đồng bộ |
| **Cloud Backup** | Sao lưu lên cloud storage |
| **Time-based** | Lập lịch theo thời gian cố định |

---

## 3. Data Migration (Di dời dữ liệu)

- **Định nghĩa:** Chuyển dữ liệu giữa các hệ thống, loại storage, hoặc định dạng khác nhau.

### Các loại Migration phổ biến:
- **OLTP → OLAP** (chuyển từ hệ thống giao dịch sang phân tích)
- **On-premises → Cloud** (di dời lên đám mây)

### Các khái niệm cốt lõi trong Migration:
| Khái niệm | Ý nghĩa |
| :--- | :--- |
| **Data Mapping** | Ánh xạ trường dữ liệu nguồn-đích |
| **Data Cleansing** | Làm sạch dữ liệu trước khi di dời |
| **Data Profiling** | Phân tích chất lượng và cấu trúc dữ liệu nguồn |
| **ETL** | Pipeline biến đổi dữ liệu |
| **Cutover** | Thời điểm chuyển đổi từ hệ thống cũ sang mới |
| **Rollback** | Kế hoạch quay lại hệ thống cũ nếu có sự cố |

### 2 kiểu Data Movement chính:
| Kiểu | Mô tả |
| :--- | :--- |
| **Homogeneous Migration** | Di dời giữa cùng loại database/platform |
| **Heterogeneous Migration** | Di dời giữa các hệ thống khác loại (platform, schema, DB engine) |

---

## 4. Data Center Migration vs Cloud Migration

| | Data Center Migration | Cloud Migration |
| :--- | :--- | :--- |
| **Định nghĩa** | Di dời IT assets (servers, storage, apps) từ DC này sang DC khác | Di dời workload/data từ on-premises lên cloud |
| **Lợi ích Cloud** | — | Scalability, Flexibility, Cost Efficiency |

### 6 chiến lược Cloud Migration (6 Rs):
| Chiến lược | Mô tả |
| :--- | :--- |
| **Rehosting** (Lift & Shift) | Di dời nguyên xi lên cloud, không thay đổi |
| **Replatforming** (Lift & Reshape) | Chuyển lên cloud với một vài tối ưu nhỏ |
| **Refactoring** (Re-architect) | Thiết kế lại tận dụng cloud-native services |
| **Repurchasing** | Chuyển sang SaaS thay thế ứng dụng cũ |
| **Retiring** | Loại bỏ các ứng dụng/workloads không còn cần thiết |
| **Retaining** | Giữ lại on-premises (chưa sẵn sàng di dời) |

### Fast Upload Accelerators:
| Công cụ | Nhà cung cấp |
| :--- | :--- |
| **IBM Aspera** | IBM Cloud |
| **AWS Snowball** | Amazon Web Services |
| **Google Transfer Appliance** | Google Cloud |

---

## Tổng kết học tập

- **Mỗi module** có: Summary, Glossary, Cheat Sheet để tham chiếu nhanh.
- **Assessments:** Practice quiz sau mỗi lesson + Graded quiz sau mỗi module.
- **Hands-on Labs + Final Project:** Thực hành thực chiến công cụ và công nghệ đã học.
