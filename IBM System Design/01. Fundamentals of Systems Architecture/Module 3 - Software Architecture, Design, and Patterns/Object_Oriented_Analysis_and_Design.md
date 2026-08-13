# Phân tích và Thiết kế Hướng Đối tượng (Object-Oriented Analysis and Design - OOAD)

Phân tích và Thiết kế Hướng Đối tượng (OOAD) là một phương pháp tiếp cận để phân tích và thiết kế hệ thống phần mềm khi hệ thống đó sẽ sử dụng các ngôn ngữ lập trình hướng đối tượng (OOP) như Java, C++, hoặc Python để phát triển.

---

## 1. Đối tượng (Objects) và Lớp (Classes)
* **Đối tượng (Objects):**
  * Là trung tâm của OOAD.
  * Chứa dữ liệu (data) và sở hữu các hành vi (behaviors) quy định những hành động mà đối tượng đó có thể thực hiện.
  * Một đối tượng cụ thể còn được gọi là một **thực thể (instance)**.
* **Lớp (Classes):**
  * Là bản thiết kế (blueprint) hoặc khuôn mẫu (template) chung để tạo ra các đối tượng.
  * Lớp định nghĩa các thuộc tính (properties) và phương thức (methods) chung, nhưng không gán giá trị cụ thể cho các thuộc tính đó.
* **Thể hiện hóa (Instantiation):**
  * Là quá trình tạo ra một đối tượng cụ thể từ một lớp trong mã nguồn. 
  * Chỉ sau khi instantiation thành công, các thuộc tính của lớp mới được gán cho những giá trị cụ thể, và các phương thức của đối tượng mới có thể được gọi để thực thi hành động (ví dụ: tạo hoặc hủy lịch hẹn).
* **Lợi ích:** OOAD giúp chia nhỏ hệ thống thành các đối tượng tương tác độc lập, cho phép nhiều lập trình viên phát triển đồng thời các phần khác nhau của ứng dụng.

---

## 2. Sơ đồ Lớp (Class Diagram) trong UML
* **Định nghĩa:** Là một sơ đồ UML cấu trúc tĩnh (structural UML diagram) được sử dụng phổ biến nhất trong OOAD để biểu diễn cấu trúc của hệ thống.
* **Thành phần:**
  * Mỗi hộp đại diện cho một Lớp, hiển thị các thuộc tính gồm: dữ liệu/thuộc tính (properties) và các hành động/phương thức khả dụng (methods).
  * Hiển thị mối quan hệ giữa các lớp trong hệ thống.
* **Tính kế thừa (Inheritance):**
  * Một lớp con (subclass) sẽ thừa hưởng các thuộc tính và phương thức của lớp cha (parent class), đồng thời có thể bổ sung các thuộc tính và phương thức riêng của nó.
  * *Ví dụ:* 
    * Lớp `Nurse` (Y tá), `Doctor` (Bác sĩ) và `Technician` (Kỹ thuật viên) là các lớp con kế thừa từ lớp cha `MedicalPersonnel` (Nhân viên y tế).
    * Lớp `Specialist` (Bác sĩ chuyên khoa) là lớp con của `Doctor`.
    * Do đó, bác sĩ có tất cả khả năng của nhân viên y tế, và bác sĩ chuyên khoa có tất cả khả năng của một bác sĩ thông thường.

---

## 3. Tóm tắt nhanh (Key Takeaways)
1. **OOAD** là quá trình lập kế hoạch cho một hệ thống phần mềm dựa trên các hành vi của các đối tượng tương tác.
2. **Đối tượng** chứa dữ liệu và hành vi; **Lớp** đóng vai trò là bản thiết kế cho đối tượng.
3. **Class Diagram** là sơ đồ cấu trúc UML thể hiện thuộc tính, phương thức và mối quan hệ kế thừa giữa các lớp trong hệ thống.
