# Module 5: AWS Lake Formation additional configurations and capabilities

## Bài học: Demo - LF-Tags

### 1. Mục tiêu Demo
Thực hành trực quan trên AWS Lake Formation Console về:
1. Định nghĩa các cặp khóa-giá trị LF-Tags.
2. Gán LF-Tags ở cấp độ Table và kế thừa / ghi đè ở cấp độ Column (Schema).
3. Cấp quyền truy cập (Grant Permissions) cho IAM User/Role dựa trên LF-Tags (LF-TBAC).

---

### 2. Các bước thực hiện chi tiết

#### Bước 1: Khởi tạo LF-Tags (Add Lake Formation Tag)
- Điều hướng: `Lake Formation Console` -> `Tags and permissions` -> `LF-Tags` -> `Add LF-Tag`.
- Tạo các cặp Key - Values:
  - **Tag 1:** Key = `classification`, Values = `['secret', 'not-so-secret']`.
  - **Tag 2:** Key = `job`, Values = `['analyst', 'developer', 'admin']`.

#### Bước 2: Gán LF-Tags cho Table và Cột (Assign & Inherit)
- **Gán ở cấp độ Table:**
  - Vào `Data catalog` -> `Tables` -> Chọn bảng dữ liệu đã làm sạch (`clean data`).
  - Chọn `Actions` -> `Edit LF-Tags`.
  - Thêm Tag:
    - `classification: secret`
    - `job: admin`
  - *Lưu ý về tính kế thừa (Inheritance):* Khi gán tag ở cấp Table, toàn bộ các cột bên trong tự động kế thừa (inherited) các giá trị tag này làm giá trị mặc định. Đây là nguyên tắc bảo mật tối ưu: mặc định coi mọi cột là `secret` để tránh rủi ro rò rỉ dữ liệu.
- **Ghi đè (Override) ở cấp Column:**
  - Mở chi tiết bảng -> Chọn `Edit schema`.
  - Chọn các cột không nhạy cảm (ví dụ: `name`, `address`, `city`, `state`, `phone`, `email`).
  - Nhấp `Edit LF-Tags` và cập nhật lại:
    - `classification: not-so-secret`
    - `job: developer`
  - Lưu schema. Các cột này sẽ mang tag mới thay vì kế thừa giá trị cấp Table.

#### Bước 3: Cấp quyền truy cập dựa trên Tags (Grant Tag Permissions)
- Tags đứng một mình chưa phát huy tác dụng; cần gán quyền cho User/Group tương ứng.
- Điều hướng: `Tags and permissions` -> tab `Tag permissions` -> `Grant permission`.
- **Cấu hình cấp quyền:**
  - **Principal:** Chọn User hoặc Role cụ thể (ví dụ: `development user`).
  - **LF-Tags & Values:** 
    - Có 2 tùy chọn: Cấp cho tất cả các giá trị của tag hoặc chọn đích danh từng cặp `Key - Value`.
    - Chọn giá trị cụ thể: `job = developer`.
  - **Permissions:**
    - Cấp quyền cho chính User/Role đó (`Tag permissions`).
    - Tùy chọn cấp quyền cho phép User này được quyền gán tiếp tag cho người khác (`Grantable permissions`).
  - Bấm `Grant` để hoàn tất.

---

### 3. Nguyên tắc kiến trúc rút ra
- **Kế thừa an toàn (Fail-safe inheritance):** Đặt tag có mức độ nhạy cảm cao nhất ở cấp Table/Database (default to restrictive), sau đó mới nới lỏng dần bằng cách override ở cấp cột cụ thể.
- **Tối ưu quản trị quy mô (Decoupled Scalability):** Việc cấp quyền dựa trên Tag (LF-TBAC) giúp phân tách giữa việc quản trị dữ liệu (gán nhãn schema) và quản trị danh tính IAM. Khi có thêm cột mới hoặc nhân sự mới gia nhập nhóm dev, không cần can thiệp viết lại các policy IAM phức tạp.
