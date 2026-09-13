# AWS Lake Formation Basic Permission Model

## 1. Bản chất & Lợi ích của Fine-Grained Permissions
- **Thống nhất kiểm soát (Unified Access Control):** Lake Formation hợp nhất quyền truy cập xuyên suốt các tầng: Analytics engines (Athena, EMR, Redshift Spectrum), Glue Data Catalog, và Storage (S3).
- **Phân quyền chi tiết dạng cơ sở dữ liệu (Database-style permissions):**
  - Kiểm soát tới cấp độ: **Table**, **Column**, và thậm chí **Row-level**.
  - Tuân thủ nguyên tắc đặc quyền tối thiểu (Least Privilege).
- **Tối ưu chi phí & Quản trị dữ liệu (Single Source of Truth):**
  - Không cần tạo bản sao (replicate) nhiều dataset khác nhau cho các team khác nhau để giấu cột/hàng nhạy cảm.
  - Tiết kiệm dung lượng lưu trữ trên S3 $\rightarrow$ Giảm chi phí lưu trữ trên đám mây.
- **Tuân thủ quy định & Kiểm toán (Compliance & Auditing):**
  - Giám sát và ghi nhận audit log: Ai truy cập cái gì, từ đâu và vào lúc nào (who, what, where, when).

---

## 2. Chiến lược phân quyền: Coarse-Grained (IAM) vs Fine-Grained (Lake Formation)
Để tránh bị quá mở quyền (permissive) hoặc quản lý hàng trăm IAM policy phức tạp:

| Thành phần | Phạm vi quản lý | Khuyến nghị cấu hình |
| :--- | :--- | :--- |
| **AWS IAM** | **Coarse-grained (Phạm vi thô)** | - Cấp quyền cho user/role tương tác với các AWS service cần thiết (VD: quyền mở Athena console, gọi API S3 cơ bản).<br>- Giúp giảm số lượng IAM policies phải duy trì. |
| **AWS Lake Formation** | **Fine-grained (Phạm vi chi tiết)** | - Trực tiếp quản trị quyền trên dữ liệu thực tế: Data Catalog, S3 locations, và data rows/columns.<br>- Quản lý ai được SELECT, ALTER, DROP trên database/table/column nào. |

> **Lưu ý quan trọng về Backwards Compatibility:**
> Mặc định trong Lake Formation có thiết lập **Use only IAM access control** (nhóm IAMAllowedPrincipals được gán full quyền trên catalog) để tương thích ngược với Glue Catalog cũ. Khi muốn dùng Fine-grained permissions của Lake Formation, cần **bỏ chọn/gỡ bỏ** quyền này để tránh việc IAM vô tình bypass toàn bộ rào chắn của Lake Formation.

---

## 3. Các Personas (Nhóm quyền điển hình) trong Lake Formation
1. **Data Lake Administrator (Quản trị viên Data Lake):**
   - Full quyền trên toàn bộ resources và data locations (S3).
   - Cấp phát (grant) hoặc thu hồi (revoke) quyền của các principals khác (kể cả chính mình).
   - Tạo database và cấp quyền tạo database cho người khác.
2. **Database Creator (Người tạo Database):**
   - Có toàn quyền quản trị trên database và table do chính họ tạo ra.
   - Có thể chỉ định (designate) user/role khác trở thành Database Creator.
3. **Table Creator (Người tạo Table):**
   - Có quyền quản trị trên các bảng (tables) do chính họ tạo ra.
   - Có quyền xem database chứa các bảng đó để quản lý bảng của mình.
