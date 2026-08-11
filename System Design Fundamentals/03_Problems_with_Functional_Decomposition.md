# System Design Fundamentals - Problems with Functional Decomposition

## 📌 Tổng quan (Overview)
- **Khóa học**: System Design Fundamentals (Pearson / Coursera)
- **Chương**: What Not to Do
- **Bài học**: Problems with Functional Decomposition (Những vấn đề chuyên sâu của phân rã theo chức năng)
- **Thời lượng**: 3 phút 10 giây
- **Diễn giả**: Juval Löwy

---

## ⚡ 1. Phản ứng dây chuyền 1: Client bị phình to & Service biến thành "bù nhìn"

- **Client ghép nối Service**: Khi Client phải tự gọi từng Service theo thứ tự $A \rightarrow B \rightarrow C$, Client lập tức bị ô nhiễm và phình to bởi Business Logic.
- **Service bị "làm ngu" (Dumb Services)**: Để tránh lặp lại Business Logic ở cả 2 nơi (Client và Services), các kỹ sư có xu hướng rút hết logic khỏi Service, biến chúng thành các khối chuyển tiếp (pass-through building blocks) vô dụng.
- **Hậu quả**: Toàn bộ kiến trúc thực chất bị dồn hết về Client. Hệ thống trở thành một ứng dụng Client khổng lồ.

---

## 🔗 2. Phản ứng dây chuyền 2: Cố gắng sửa sai bằng Chỗi gọi nối tiếp ($A \rightarrow B \rightarrow C$)

Để tránh Client phình to, các kỹ sư thường chuyển sang cách: **Client chỉ gọi $A$, $A$ gọi $B$, $B$ gọi $C$**.  
Tuy nhiên, cách này tạo ra một thảm họa phụ thuộc chéo (Coupling Horror):

1. **Ràng buộc tham số & Logic thất bại**:
   - $A$ không còn là $A$ thuần túy. $A$ phải biết về $B$ và nhận đủ tham số để gọi $B$.
   - Nếu $B$ thất bại, logic rollback/undo $B$ phải dồn ngược vào $A$.
   - $A$ thậm chí phải nhận tham số của $C$ để truyền qua cho $B$ gọi $C$.
2. **Khó khăn với bất đồng bộ (Async)**:
   - Nếu $B$ gọi $C$ bất đồng bộ (asynchronous) hoặc qua Message Queue và $C$ thất bại, làm sao $B$ hay $A$ nhận biết được để xử lý?

---

## 🌀 3. Phản ứng dây chuyền 3: Thảm họa Hoàn tác (Undo/Rollback Disaster)

Khi chuỗi gọi đi sâu vào $C$ và gặp lỗi ở $C$:

- **Vấn đề ai xử lý Undo**: Ai sẽ đứng ra hoàn tác $A$ và $B$?
- **Hệ thống bị "chết" trạng thái**: Nếu $A$ và $B$ đã hoàn tất và kết thúc từ trước (do xử lý bất đồng bộ/queue), logic hoàn tác $A$ và $B$ lại phải nhét ngược vào bên trong $C$.
- **Sự phối hợp ma quỷ**:
  - $B$ và $C$ phải phối hợp xem ai chịu trách nhiệm undo $A$.
  - Nếu $B$ hoàn tác $A$ thất bại, $C$ xử lý thế nào?
  - Sự phục hồi nghiệp vụ của $B$ phụ thuộc vào kết quả undo $A$, nhưng $C$ làm sao biết được điều đó?
- **Kết luận**: Bạn không còn 3 Services độc lập nữa, mà đã tạo ra một **"Giant Clique of Doom"** (Một khối liên kết ma quỷ/tử thần duy nhất).

---

## 📈 4. Sự bùng nổ Độ phức tạp phi tuyến tính (Runaway Complexity)

- **Không tăng theo cấp số cộng**: Độ phức tạp tích lũy của hệ thống dạng này **không tăng tuyến tính** ($2 + 3 + 4 + 5$), mà tăng theo hình xoắn ốc/phản ứng dây chuyền không thể kiểm soát (**Runaway Reaction**).
- Với 3 services đã hỗn loạn như trên, khi hệ thống lên tới 13 hay 30 services, nó sẽ hoàn toàn sụp đổ.
- **Hậu quả cuối cùng**: Tạo ra một lượng Nợ kỹ thuật khổng lồ (**horrendously complex technical debt**) và một hệ thống rối rắm mà không ai còn có thể hiểu hay bảo trì nổi.

---

## 💡 Điểm đúc kết chính (Key Takeaways)

1. **Chuyển logic từ Client sang Service chéo không giải quyết được gốc rễ**: Cho $A$ gọi $B$ gọi $C$ chỉ chuyển sự ô nhiễm từ Client sang phụ thuộc chéo giữa các Services.
2. **Thảm họa Trạng thái & Undo**: Phân rã theo quy trình chức năng làm cho công tác quản lý giao dịch (Transaction Management) và hoàn tác (Rollback) trở thành ác mộng.
3. **Cảnh giác với Runaway Complexity**: Độ phức tạp tích tụ theo kiểu lũy thừa phi tuyến tính. Hệ thống càng nhiều tính năng thì nguy cơ trở thành "Clique of Doom" càng cao nếu giữ cách phân rã theo chức năng.
