# The Cost of Poor Platform Governance

> **Course**: Microsoft DevOps Engineering  
> **Module**: Course 1 - DevOps Platforms & Source Control  
> **Topic**: Platform Governance & Compliance by Design  

---

## 1. Tổng quan & Tình huống thực tế (Case Study)

- **Sự cố MOVEit Transfer (2023)**:
  - Ảnh hưởng hơn **2.700 tổ chức** và **93,3 triệu cá nhân**, trở thành một trong những vụ tấn công chuỗi cung ứng (supply chain attack) lớn nhất lịch sử.
  - **Bài học cho Platform Owners**: Lỗi phần mềm (software flaw) là điều có thể xảy ra, nhưng thảm họa thực sự đến từ **sự thiếu hụt trong phân quyền tách biệt (segregated access) và các cơ chế kiểm soát an ninh xung quanh hệ thống**.

---

## 2. Tiêu chuẩn tuân thủ & Nguyên tắc cốt lõi

Các khung tiêu chuẩn không đơn thuần là thủ tục giấy tờ ("bureaucratic checkboxes") mà là **khung ngăn ngừa thảm họa**:

| Tiêu chuẩn | Trọng tâm |
| :--- | :--- |
| **SOX (Sarbanes-Oxley Act)** | Yêu cầu kiểm soát nghiêm ngặt những ai có quyền can thiệp vào dữ liệu tài chính. |
| **ISO 27001** | Yêu cầu phương pháp tiếp cận có hệ thống để quản lý an toàn thông tin. |

### 🔑 Nguyên tắc Phân tách Nhiệm vụ (Segregation of Duties - SoD)
- **Định nghĩa**: Không một cá nhân đơn lẻ nào được nắm giữ toàn quyền để vừa **khởi tạo (initiate)**, **phê duyệt (approve)**, vừa **thực thi (complete)** một hành động nhạy cảm mà không có sự kiểm tra chéo (second set of eyes).
- Việc một lập trình viên có thể đơn phương truy cập hoặc thay đổi hệ thống chạm tới dữ liệu nhạy cảm là vi phạm trực tiếp nguyên tắc SoD.

---

## 3. Rủi ro quản trị trong Azure DevOps

### ⚠️ Kịch bản điểm lỗi đơn lẻ (Single Point of Failure):
- Một kỹ sư có quyền hạn quá rộng (broad permissions) trên toàn bộ project trong Azure DevOps.
- Kỹ sư đó có thể tự tạo pipeline mới, kết nối tới môi trường Production thông qua Service Connection có sẵn, và deploy code mà **không cần qua bất kỳ quy trình review hay approval nào**.
- Đây là kịch bản rủi ro cao nhất mà kiểm toán viên (auditors) và kẻ tấn công luôn tìm kiếm.

### ⚠️ Sai lầm "Mặc định là An toàn" (Out-of-the-Box Assumption):
- **Thực tế**: Azure DevOps cung cấp rất nhiều tính năng kiểm soát mạnh mẽ:
  - *Approval checks* (kiểm tra phê duyệt)
  - *Environment resource permissions* (phân quyền tài nguyên môi trường)
  - *Branch policies* (chính sách nhánh)
- **Rủi ro**: Các tính năng này **KHÔNG được bật mặc định**. Giả định rằng hệ thống cài đặt ban đầu đã an toàn là một sai lầm nghiêm trọng.

---

## 4. Giải pháp: Xây dựng cơ chế "Compliance by Design"

Thay vì áp đặt các thủ tục hành chính cồng kềnh (red tape), quản trị nền tảng hiệu quả giúp tạo ra các **hành lang an toàn (guardrails)** để lập trình viên tự do sáng tạo và tự chủ:

1. **Phân vùng cách ly (Deliberate Separation)**:
   - Sử dụng các Project riêng biệt để cô lập phạm vi truy cập và tài nguyên.
2. **Quản lý Agent Pools chặt chẽ**:
   - Phân định rõ phạm vi (scope) và quyền hạn của các Agent Pool dùng cho build/deploy.
3. **Thiết lập Approval Checks & Gateways**:
   - Bắt buộc kiểm tra phê duyệt trước khi pipeline chạm tới các môi trường nhạy cảm (Staging, Production).
4. **Tự động hóa tuân thủ**:
   - Chuyển đổi việc tuân thủ từ "bảng checklist thủ công" thành **tính năng tự động hóa được tích hợp sẵn trong kiến trúc nền tảng (Automated Architecture)**.
