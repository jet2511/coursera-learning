# More Application Development Tools

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Tools in Software Development
- **Hình thức:** Video (Thời lượng: ~5 phút)

---

## 1. Thực hành CI/CD (Continuous Integration & Delivery/Deployment)
- **CI/CD** là phương pháp luận thực hành tiêu chuẩn tốt nhất (best practice) của các đội ngũ DevOps giúp phát hành các thay đổi mã nguồn thường xuyên và tin cậy.
- **Continuous Integration (CI):**
  - Đảm bảo mã nguồn mới được tích hợp vào nhánh chính thường xuyên (hàng ngày hoặc hàng giờ).
  - Tự động chạy build và automated tests để phát hiện lỗi xung đột từ sớm.
- **Continuous Delivery / Continuous Deployment (CD):**
  - Bắt đầu ngay khi CI hoàn tất.
  - Tự động đóng gói và triển khai phiên bản build tới môi trường testing, staging hoặc trực tiếp lên production.

---

## 2. Công cụ Build (Build Tools) & Tự động hóa Build
- **Vai trò:** Chuyển đổi mã nguồn thành các file nhị phân (binaries/executables) có thể thực thi hoặc cài đặt được; thiết lập cờ biên dịch (compile flags) và quản lý dependencies.
- **Các tác vụ tự động hóa (Build Automation Tasks):**
  1. Tải các dependencies/thư viện phụ thuộc.
  2. Biên dịch (compile) mã nguồn sang binary code.
  3. Đóng gói (package) binary code thành artifacts (JAR, WAR, executable...).
  4. Chạy bộ kiểm thử tự động (running tests).
  5. Triển khai (deployment) lên hệ thống đích.
- **Hai phân loại Build Tools:**
  - **Build-automation utilities:** Tiện ích trực tiếp biên dịch và liên kết mã nguồn (ví dụ: `Webpack` - module bundler cho JS, `Babel` - JS compiler, `WebAssembly`).
  - **Build-automation servers:** Máy chủ kích hoạt các tiện ích build tự động theo lịch (scheduled) hoặc theo sự kiện trigger (như commit mã nguồn).

---

## 3. Packages & Package Managers
- **Packages (Gói phần mềm):** Là các tệp lưu trữ nén (archive files) gom toàn bộ files ứng dụng, hướng dẫn cài đặt và metadata (mô tả, phiên bản, danh sách các thư viện phụ thuộc bắt buộc).
- **Package Manager (Trình quản lý gói):** Tự động hóa các tác vụ tìm kiếm, cài đặt, cập nhật, kiểm tra tính toàn vẹn (checksums/chứng chỉ số) và gỡ cài đặt phần mềm.

### Phân loại Package Managers theo nền tảng & ngôn ngữ:
| Danh mục | Nền tảng / Ngôn ngữ | Công cụ tiêu biểu |
| :--- | :--- | :--- |
| **Hệ điều hành (OS Level)** | **Linux** | `DPKG` (Debian/Ubuntu), `RPM` (Red Hat/CentOS) |
| | **Windows** | `Chocolatey` |
| | **macOS** | `Homebrew`, `MacPorts` |
| | **Android** | `Package Manager` |
| **Ngôn ngữ lập trình (Language Level)** | **Java** *(Trọng tâm chứng chỉ)* | **`Maven`**, **`Gradle`** |
| | **Node.js / JavaScript** | `npm` |
| | **Python** | `pip`, `Conda` |
| | **Ruby** | `RubyGems` |
