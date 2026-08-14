# Bài Thực hành: Thiết kế Hệ thống Đặt vé Trực tuyến bằng Sơ đồ UML (Lab - Design MovieGo Booking System)

Tài liệu này tổng hợp toàn bộ hướng dẫn, thông số kỹ thuật và 4 bản vẽ thiết kế sơ đồ UML hoàn chỉnh cho nền tảng đặt vé xem phim trực tuyến **MovieGo**.

---

## 1. Tổng quan Kịch bản (Scenario - MovieGo)
Hệ thống đặt vé xem phim **MovieGo** phục vụ 3 nhóm đối tượng:
* **Khách hàng (Customer):** Tìm kiếm phim, chọn suất chiếu, đặt vé và thanh toán qua cổng thanh toán bảo mật.
* **Quản trị viên (Admin):** Quản lý lịch chiếu phim và theo dõi danh sách các đơn đặt vé.
* **Cổng thanh toán (Payment Gateway):** Hệ thống bên thứ ba xử lý giao dịch tài chính an toàn.

Hệ thống cần 4 mô hình UML chuẩn hóa để làm tài liệu kiến trúc và hướng dẫn phát triển:
1. **Sơ đồ Use Case:** Xác định phạm vi và các chức năng của từng tác nhân.
2. **Sơ đồ Lớp (Class Diagram):** Thiết kế cấu trúc tĩnh, thuộc tính và liên kết cơ sở dữ liệu.
3. **Sơ đồ Tuần tự (Sequence Diagram):** Mô tả thứ tự gửi message trong quy trình "Đặt vé".
4. **Sơ đồ Hoạt động (Activity Diagram):** Thể hiện luồng tiến trình, rẽ nhánh điều kiện và phân làn trách nhiệm (Swimlanes).

---

## 2. Phần 1: Sơ đồ Use Case (Use Case Diagram)

### **Thành phần thiết kế:**
* **Ranh giới hệ thống:** `Online Booking System`
* **Tác nhân (Actors):** Customer, Admin, Payment Gateway.
* **Use Cases:**
  * *Customer:* Browse Movies (Xem danh mục phim), Book Ticket (Đặt vé), Make Payment (Thanh toán).
  * *Admin:* Manage Schedule (Quản lý lịch chiếu), View Bookings (Xem đơn đặt vé).
  * *Payment Gateway:* Liên kết với Use Case `Make Payment`.
* **Mối quan hệ:** `Make Payment` mở rộng (`<<extend>>`) từ `Book Ticket`.

```mermaid
flowchart TD
    %% Actors
    Customer[Khách hàng - Customer]
    Admin[Quản trị viên - Admin]
    PaymentGateway[Cổng thanh toán - Payment Gateway]

    %% System Boundary
    subgraph OnlineBookingSystem [Ranh giới hệ thống: Online Booking System]
        UC_Browse((Browse Movies))
        UC_Book((Book Ticket))
        UC_Pay((Make Payment))
        UC_Schedule((Manage Schedule))
        UC_ViewBookings((View Bookings))

        %% Relationships
        UC_Pay -.->|&lt;&lt;extend&gt;&gt;| UC_Book
    end

    %% Actor Associations
    Customer --- UC_Browse
    Customer --- UC_Book
    Customer --- UC_Pay
    
    Admin --- UC_Schedule
    Admin --- UC_ViewBookings

    PaymentGateway --- UC_Pay
```

---

## 3. Phần 2: Sơ đồ Lớp (Class Diagram)

### **Cấu trúc Lớp, Thuộc tính và Bản số (Multiplicity):**
* **Customer:** `CustomerID` : int (PK), `Name` : string, `Email` : string, `Phone` : string
* **Admin:** `AdminID` : int (PK), `Name` : string, `Email` : string, `Role` : string
* **Movie:** `MovieID` : int (PK), `Title` : string, `Duration` : string, `Genre` : string, `Rating` : string
* **Showtime:** `ShowtimeID` : int (PK), `MovieID` : int (FK), `Date` : date, `Time` : string, `AvailableSeats` : int, `TotalSeats` : int
* **Ticket:** `TicketID` : int (PK), `ShowtimeID` : int (FK), `SeatNumber` : string, `Price` : decimal, `BookingID` : int (FK)
* **Booking:** `BookingID` : int (PK), `CustomerID` : int (FK), `ShowtimeID` : int (FK), `BookingDate` : date, `Status` : string
* **Payment:** `PaymentID` : int (PK), `BookingID` : int (FK), `Amount` : decimal, `PaymentDate` : date, `Status` : string

### **Mối quan hệ (Multiplicity theo đáp án Coursera):**
* `Customer` **1 : N** `Booking`
* `Showtime` **N : 1** `Movie`
* `Showtime` **1 : N** `Ticket`
* `Booking` **1 : N** `Ticket`
* `Booking` **N : 1** `Showtime`
* `Booking` **1 : 1** `Payment`

```mermaid
classDiagram
    class Customer {
        +int customerId PK
        +string name
        +string email
        +string phone
    }

    class Admin {
        +int adminId PK
        +string name
        +string email
        +string role
    }

    class Movie {
        +int movieId PK
        +string title
        +string duration
        +string genre
        +string rating
    }

    class Showtime {
        +int showtimeId PK
        +int movieId FK
        +date date
        +string time
        +int availableSeats
        +int totalSeats
    }

    class Ticket {
        +int ticketId PK
        +int showtimeId FK
        +string seatNumber
        +decimal price
        +int bookingId FK
    }

    class Booking {
        +int bookingId PK
        +int customerId FK
        +int showtimeId FK
        +date bookingDate
        +string status
    }

    class Payment {
        +int paymentId PK
        +int bookingId FK
        +decimal amount
        +date paymentDate
        +string status
    }

    Customer "1" --> "0..*" Booking : places
    Showtime "0..*" --> "1" Movie : belongs to
    Showtime "1" --> "0..*" Ticket : has
    Booking "1" --> "1..*" Ticket : contains
    Booking "0..*" --> "1" Showtime : for
    Booking "1" --> "1" Payment : paid by
```

---

## 4. Phần 3: Sơ đồ Tuần tự (Sequence Diagram) - Kịch bản "Book Ticket"

### **Luồng tương tác các đối tượng:**
1. Khách hàng duyệt phim trên Booking System.
2. Booking System kiểm tra ghế trống với đối tượng Showtime.
3. Khách hàng chọn suất chiếu và yêu cầu đặt vé.
4. Booking System gửi yêu cầu thanh toán (bất đồng bộ) tới Cổng thanh toán.
5. Cổng thanh toán gửi phản hồi xác nhận thanh toán.
6. Booking System gọi Ticket để khởi tạo vé.
7. Booking System gửi xác nhận đặt vé thành công tới Khách hàng.

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Khách hàng (Customer)
    participant System as Booking System
    participant Showtime as Showtime
    participant PG as Payment Gateway
    participant Ticket as Ticket

    Customer->>System: 1. Browse Movies
    activate System
    System->>Showtime: 2. Check Availability
    activate Showtime
    Showtime-->>System: 3. Return Available Seats
    deactivate Showtime

    Customer->>System: 4. Select Showtime & Book Ticket
    System-)PG: 5. Make Payment (Asynchronous)
    activate PG
    PG-->>System: 6. Payment Confirmation
    deactivate PG

    System->>Ticket: 7. Generate Ticket
    activate Ticket
    Ticket-->>System: 8. Return Ticket Info
    deactivate Ticket

    System-->>Customer: 9. Ticket Confirmation
    deactivate System
```

---

## 5. Phần 4: Sơ đồ Hoạt động (Activity Diagram) - Quy trình "Book Ticket"

### **Phân làn trách nhiệm (Swimlanes) & Điểm quyết định:**
* **Làn Customer:** Tìm phim, chọn suất chiếu.
* **Làn Booking System:** Kiểm tra ghế, đặt vé, gửi xác nhận.
* **Làn Payment Gateway:** Xử lý giao dịch thanh toán.
* **Điểm quyết định 1:** Ghế còn trống không? (Nếu Không -> Kết thúc).
* **Điểm quyết định 2:** Thanh toán thành công không? (Nếu Không -> Kết thúc).

```mermaid
flowchart TD
    subgraph Customer [Làn Khách hàng - Customer]
        Start([● Bắt đầu]) --> Browse[1. Browse Movies]
        Browse --> SelectST[2. Select Showtime]
    end

    subgraph System [Làn Hệ thống - Booking System]
        SelectST --> CheckSeats{Ghế còn trống?}
        CheckSeats -- Không --> NoSeatMsg[Báo hết vé] --> EndFail1([⦿ Kết thúc])
        CheckSeats -- Có --> BookTicket[3. Book Ticket & Tạo đơn]
    end

    subgraph PaymentGateway [Làn Cổng thanh toán - Payment Gateway]
        BookTicket --> MakePayment[4. Make Payment]
        MakePayment --> PaySuccess{Thanh toán thành công?}
        PaySuccess -- Không --> PayFailMsg[Báo lỗi giao dịch] --> EndFail2([⦿ Kết thúc])
    end

    subgraph SystemConfirm [Làn Hệ thống Xác nhận]
        PaySuccess -- Có --> ConfirmBooking[5. Confirm Booking & Tạo vé]
        ConfirmBooking --> EndSuccess([⦿ Đặt vé thành công])
    end
```

---

## 6. Tổng kết
Bài thực hành đã cung cấp giải pháp thiết kế kiến trúc toàn diện cho hệ thống **MovieGo**:
* Phân định rõ chức năng và phạm vi qua **Use Case Diagram**.
* Định hình khung cơ sở dữ liệu quan hệ và mô hình hướng đối tượng qua **Class Diagram**.
* Xác lập luồng API và message tuần tự qua **Sequence Diagram**.
* Trực quan hóa quy trình nghiệp vụ và các điểm kiểm tra lỗi rẽ nhánh qua **Activity Diagram**.
