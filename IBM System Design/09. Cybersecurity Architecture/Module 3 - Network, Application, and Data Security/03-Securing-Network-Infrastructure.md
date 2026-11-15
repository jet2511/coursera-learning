# Securing Network Infrastructure & Component Placement

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Tài liệu**: Reading: Securing Network Infrastructure (Thời lượng: ~10 phút)  
> **Tác giả**: Dee Dee Collette (IBM)

---

## 📌 Tổng Quan (Overview)
Trong việc thiết kế sơ đồ mạng an toàn (Secure Network Architecture Diagram), việc **đặt đúng vị trí** của từng thành phần phần cứng và thiết bị an ninh là yếu tố then chốt nhằm ngăn chặn rủi ro thâm nhập, phân luồng lưu lượng và đảm bảo nguyên tắc phòng thủ đa tầng (**Defense in Depth**).

```mermaid
flowchart LR
    Internet((Internet / ISP Line)) <--> Modem[Modem\n(Network Edge)]
    Modem <--> ExtRouter[External Router]
    ExtRouter <--> ExtFW[External Firewall]
    
    subgraph DMZ["DMZ (Buffer Zone)"]
        WebSrv[Web Server]
        MailSrv[Email Server]
        DNSSrv[DNS Server]
        FTPSrv[FTP Server]
        VPNSrv[VPN Server]
    end
    
    ExtFW <--> DMZ
    ExtFW <--> IntFW[Internal Firewall]
    
    subgraph InternalLAN["Internal Protected Network (LAN)"]
        IDS[IDS - Intrusion Detection System]
        IntSwitch[Core / Access Switch]
        WirelessRouter[Wireless Router / AP]
        Workstations[End-user Workstations]
        Printers[Printers / IoT]
        DBServer[(Internal Core DB/Servers)]
        
        IDS -.-> IntSwitch
        IntSwitch --> Workstations
        IntSwitch --> Printers
        IntSwitch --> DBServer
        IntSwitch <--> WirelessRouter
    end
    
    IntFW <--> IDS
```

---

## 🏗️ Chi tiết Vị trí & Vai trò của các Thành phần Mạng

### 1. Modem (Cổng biên kết nối)
- **Vị trí**: Nằm ở đường biên ngoài cùng của mạng (**Network Edge**).
- **Vai trò**: Là cổng kết nối trực tiếp với đường dây của nhà cung cấp dịch vụ Internet (ISP - qua cáp quang, DSL, Cable).
- **Kết nối**: Nối trực tiếp từ đường ISP vào Modem, và từ Modem nối tới Router để cấp quyền truy cập Internet cho toàn bộ mạng nội bộ.

### 2. Router (Bộ định tuyến)
- **Vị trí**: Đóng vai trò trung tâm kết nối giữa các mạng riêng biệt (ví dụ: kết nối giữa mạng nội bộ LAN và mạng Internet bên ngoài).
- **Mạng phức tạp**: Các router tạo thành tuyến đường trung chuyển giữa vùng biên (Edge) và vùng mạng lõi (Core - nơi xử lý lưu lượng dung lượng cao nhất).
- **Vai trò**: Phân tích và điều hướng lưu lượng theo lộ trình tối ưu và hiệu quả nhất. Trong mô hình đa mạng LAN, mỗi router điều phối giao tiếp nội bộ và kết nối các LAN với nhau để chia sẻ tài nguyên.

### 3. Switch (Bộ chuyển mạch)
- **Vị trí**: Nằm ở "trái tim" của hạ tầng mạng cục bộ (**LAN Core/Distribution**).
- **Vai trò**: Đóng vai trò điều phối kết nối tập trung giữa các thiết bị đầu cuối như máy tính, máy in, server nội bộ trong cùng một mạng LAN.
- **Tương tác**: Switch thường kết nối lên Router để dẫn lưu lượng ra ngoài Internet, đảm bảo băng thông và độ trễ giao tiếp nội bộ được tối ưu.

### 4. Firewall (Tường lửa)
- **Vị trí chiến lược**: Đặt ở tiền tuyến an ninh (**Front line**), làm chốt kiểm soát an toàn giữa mạng nội bộ được bảo vệ (Protected) và mạng bên ngoài tiềm ẩn rủi ro (Unprotected).
- **Vị trí điển hình**: Thường đặt ngay sau Router để toàn bộ lưu lượng ra/vào mạng đều phải đi qua sự kiểm duyệt của nó.
- **Chức năng**: Soi chiếu tất cả các gói tin (Packet), cho phép (permit) hoặc từ chối (deny) lưu lượng dựa theo tập luật an ninh định sẵn.

### 5. Demilitarized Zone - DMZ (Vùng phi quân sự / Vùng đệm)
- **Vị trí**: Nằm giữa mạng nội bộ (LAN) và mạng công cộng bên ngoài (Internet). Thường nằm giữa router/firewall hướng ngoại và router/firewall nội bộ.
- **Mục tiêu**: Giảm thiểu nguy cơ các cuộc tấn công bên ngoài có thể tiếp cận trực tiếp vào các thành phần lõi của mạng nội bộ.
- **Các hệ thống thường được đặt trong DMZ**:
  - **Web Servers**: Cung cấp giao diện web cho người dùng Internet qua trình duyệt.
  - **Email Servers**: Tiếp nhận và chuyển tiếp thư điện tử gửi/nhận từ bên ngoài.
  - **DNS Servers**: Phân giải tên miền thành địa chỉ IP cho các yêu cầu từ bên ngoài.
  - **FTP Servers**: Phục vụ truyền/nhận tệp tin ra ngoài.
  - **VPN Servers**: Tiếp nhận kết nối từ xa của người dùng từ Internet vào trước khi xác thực.

### 6. Intrusion Detection System - IDS (Hệ thống phát hiện xâm nhập)
- **Vị trí**: Đặt tại các vị trí hiểm yếu để giám sát và phân tích lưu lượng. Thường đặt **sau Firewall và trước Network Switch** để kiểm tra sâu luồng dữ liệu nội bộ.
- **Vai trò**:
  - Quét tìm các dấu hiệu bất thường, mẫu hành vi (signatures) hoặc dấu vết của việc xâm nhập trái phép.
  - Tạo thêm một tầng phát hiện cảnh báo bổ sung phía sau Firewall và DMZ, bắt các mối đe dọa mà firewall đã vô tình bỏ lọt.

### 7. Wireless Router (Bộ định tuyến không dây)
- **Vị trí**: Đặt tại vị trí chiến lược trong LAN.
- **Vai trò**: Vừa là router vừa là điểm truy cập không dây (Wireless Access Point - AP).
- **Chức năng**: Mở rộng kết nối cho các thiết bị di động/không dây vào mạng có dây truyền thống và ra Internet, quản lý đồng thời cả hai luồng truyền thông có dây và không dây.

---

## 🎯 Bảng Tổng Hợp Vị Trí Thành Phần Theo Kiến Trúc Bảo Mật

| Thành phần | Vị trí sơ đồ | Chức năng chính | Lưu ý an ninh |
| :--- | :--- | :--- | :--- |
| **Modem** | Biên mạng (Edge) | Chuyển đổi tín hiệu ISP | Thiết bị cửa ngõ vật lý |
| **Router** | Giữa các mạng (Edge & Core) | Điều hướng & định tuyến gói tin | Cấu hình ACL, tắt các port/dịch vụ không dùng |
| **Firewall** | Sau Router, trước LAN / DMZ | Lọc lưu lượng theo Rule | Chốt chặn kiểm soát bắt buộc |
| **DMZ** | Vùng đệm giữa 2 Firewall/Routers | Chứa Server public (Web, Mail, DNS, VPN) | Cô lập hoàn toàn, cấm truy cập tự do vào LAN |
| **IDS** | Sau Firewall, trước Switch | Giám sát & cảnh báo xâm nhập | Không chặn gói (khác IPS), tập trung phát hiện bất thường |
| **Switch** | Trung tâm mạng nội bộ (LAN Core) | Kết nối máy trạm, máy in, server | Cấu hình VLAN để chia nhỏ phân đoạn nội bộ |
| **Wireless Router** | Tầng truy cập nội bộ (Access Layer) | Cung cấp mạng không dây | Bắt buộc mã hóa WPA3/WPA2, tách riêng SSID Guest |
