# LAB DELIVERABLES: Capacity Planning Worksheet
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Core Digital Transformation for Retail Banking  
**Vai trò:** Systems and Solutions Architect  
**Mục tiêu:** Tính toán và lập bảng hoạch định năng lực hạ tầng Cloud (Compute, Storage, Network) đảm bảo chịu tải cao điểm, dự phòng N+1 và tối ưu chi phí.  

---

# TASK 1: ESTIMATE COMPUTING NEEDS (TÍNH TOÁN NĂNG LỰC TÍNH TOÁN)

### 1. Dữ liệu kịch bản (Input Parameters)
- **Peak Concurrent Users (Số người dùng đồng thời đỉnh):** $500$ users
- **Tài nguyên tiêu thụ cho mỗi session:**
  - RAM tiêu thụ/session: $\sim 250\text{ MB} = 0.25\text{ GB}$
  - vCPU tiêu thụ/session: $\sim 0.25\text{ vCPU}$
- **Hệ số dự phòng an toàn (Resiliency Buffer):** $+30\%$ ($1.3$) dành cho failover, đột biến tải và bảo trì.

---

### 2. Các bước tính toán chi tiết (Formulas & Results)

#### A. Tổng dung lượng RAM cần thiết:
$$\text{Base RAM} = 500 \times 250\text{ MB} = 125,000\text{ MB} = 125\text{ GB}$$
$$\text{Total RAM (with 30\% Buffer)} = 125\text{ GB} \times 1.3 = \mathbf{162.5\text{ GB}}$$

#### B. Tổng số vCPU cần thiết:
$$\text{Base vCPU} = 500 \times 0.25\text{ vCPU} = 125\text{ vCPU}$$
$$\text{Total vCPU (with 30\% Buffer)} = 125 \times 1.3 = \mathbf{162.5\text{ vCPU}}$$

---

### 3. Quy đổi sang Pods & Ánh xạ loại máy chủ Cloud (Instance Sizing)

Giả sử định cỡ chuẩn của 1 Container Pod cho Banking Microservice là: **$2\text{ vCPU}$** và **$4\text{ GB RAM}$**:
- Số lượng Pods cần thiết: $\lceil 162.5 / 2 \rceil = \mathbf{82\text{ Pods}}$ (phân bổ đều cho các cụm microservices: Auth, Loan, Onboarding, Transaction).

#### Đề xuất Cloud Instance Type (AWS / IBM Cloud):
Để chạy cụm Kubernetes/Red Hat OpenShift chứa các Pods trên với tính sẵn sàng cao (**High Availability qua 3 Availability Zones - AZs**):
- **Lựa chọn instance:** Nhóm **Compute/General Purpose**:
  - **AWS:** `m6i.4xlarge` (16 vCPU, 64 GB RAM) hoặc `c6i.4xlarge` (16 vCPU, 32 GB RAM).
  - **IBM Cloud:** `bx2-16x64` (16 vCPU, 64 GB RAM).
- **Số lượng Worker Nodes triển khai:**
  - Cần tối thiểu: $\lceil 162.5\text{ vCPU} / 16\text{ vCPU} \rceil \approx 11\text{ nodes}$ (đã bao gồm buffer 30%).
  - **Khuyến nghị HA Multi-AZ:** Triển khai **$12\text{ Worker Nodes}$** (`m6i.4xlarge` hoặc `bx2-16x64`) phân bổ đều **4 nodes/Zone trên 3 AZs**, cung cấp tổng năng lực:
    - **Tổng vCPU khả dụng:** $12 \times 16 = \mathbf{192\text{ vCPU}}$ (dư dả so với $162.5$).
    - **Tổng RAM khả dụng:** $12 \times 64\text{ GB} = \mathbf{768\text{ GB}}$ (dư dả để cache dữ liệu và mở rộng).

---

# TASK 2: CALCULATE STORAGE REQUIREMENTS (TÍNH TOÁN DUNG LƯỢNG LƯU TRỮ)

### 1. Dữ liệu kịch bản (Input Parameters)
- **Số lượng giao dịch mỗi tháng:** $5,000,000$ transactions/tháng.
- **Kích thước trung bình mỗi bản ghi giao dịch:** $\sim 2\text{ KB}$ (bao gồm payload, metadata và audit trail).
- **Thời gian lưu trữ Online (Hot Active Retention):** $13\text{ tháng}$.
- **Hệ số chi phí đánh chỉ mục (Indexing Overhead):** $+20\%$ ($1.2$).
- **Lưu trữ lưu trữ lịch sử (Cold Archive):** Đẩy dữ liệu cũ hơn 13 tháng vào Object Storage theo chu kỳ hàng năm ($12\text{ tháng}$).

---

### 2. Các bước tính toán chi tiết (Formulas & Results)

#### A. Dung lượng dữ liệu thô phát sinh hàng tháng:
$$\text{Monthly Base Volume} = 5,000,000 \times 2\text{ KB} = 10,000,000\text{ KB} = 10,000\text{ MB} = \mathbf{10\text{ GB / tháng}}$$

#### B. Dung lượng lưu trữ hoạt động (Active Hot Storage - 13 tháng kèm 20% Index Overhead):
$$\text{Base Active Volume} = 10\text{ GB/tháng} \times 13\text{ tháng} = 130\text{ GB}$$
$$\text{Total Active Storage} = 130\text{ GB} \times 1.2 = \mathbf{156\text{ GB}}$$

#### C. Dung lượng lưu trữ lịch sử hàng năm (Yearly Cold Archive Storage):
$$\text{Annual Archive Size} = 10\text{ GB/tháng} \times 12\text{ tháng} = \mathbf{120\text{ GB / năm}}$$
*(Sau 5 năm tuân thủ quy chế kiểm toán ngân hàng: $120\text{ GB} \times 5 = 600\text{ GB}$)*.

---

### 3. Đề xuất phân tầng lưu trữ (Tiered Storage Architecture)
- **Active Tier (Hot Storage):**
  - **Công nghệ:** SSD-backed Block Storage (AWS EBS `gp3`/`io2` hoặc IBM Cloud Block Storage NVMe).
  - **Dung lượng cấp phát:** Tối thiểu **$250\text{ GB}$** (provisioning thêm 60% cho database snapshot và transaction log WAL).
  - **Mục đích:** Đảm bảo độ trễ truy vấn cực thấp (< 2ms) cho các nghiệp vụ kiểm tra số dư và giao dịch thẻ thời gian thực.
- **Archive Tier (Cold Storage):**
  - **Công nghệ:** Cloud Object Storage với chính sách Lifecycle Rules (AWS S3 Glacier Instant Retrieval / IBM Cloud Object Storage Cold Vault).
  - **Mục đích:** Lưu trữ lâu dài dữ liệu lịch sử giao dịch và nhật ký kiểm toán bất biến (WORM compliance - 7 năm) với chi phí thấp nhất.

---

# TASK 3: ESTIMATE NETWORK BANDWIDTH (TÍNH TOÁN BĂNG THÔNG MẠNG)

### 1. Dữ liệu kịch bản (Input Parameters)
- **Peak Throughput (Giao dịch đỉnh):** $2,000\text{ transactions/giây (TPS)}$.
- **Average Payload Size (Kích thước gói tin trung bình):** $1.5\text{ KB}$.
- **Hệ số dự phòng mạng (Redundancy & Re-transmission Overhead):** $+25\%$ ($1.25$).

---

### 2. Các bước tính toán chi tiết (Formulas & Results)

#### A. Thông lượng dữ liệu thô (Raw Throughput):
$$\text{Raw Throughput (KB/s)} = 2,000\text{ TPS} \times 1.5\text{ KB} = 3,000\text{ KB/s} = 3\text{ MB/s}$$

#### B. Chuyển đổi sang Megabits per second (Mbps) và cộng thêm 25% Overhead:
$$\text{Raw Bandwidth (Mbps)} = \frac{2,000 \times 1.5 \times 1,024 \times 8}{1,000,000} \approx 24.576\text{ Mbps}$$
*(Hoặc tính nhanh theo chuẩn hệ thập phân: $3\text{ MB/s} \times 8\text{ bits} = 24\text{ Mbps}$)*

Áp dụng công thức chuẩn đề bài đưa ra:
$$\text{Throughput (Mbps)} = \frac{2,000 \times 1.5 \times 8}{1,000,000} \times 10^3 \times 1.25 = 24\text{ Mbps} \times 1.25 = \mathbf{30\text{ Mbps}}$$

---

### 3. Phân bổ đa vùng (Multi-AZ Distribution) & Chính sách Autoscaling
- **Phân bổ mạng đa vùng (Multi-AZ Bandwidth Distribution):**
  - Hệ thống được triển khai trên 3 Availability Zones (AZ1, AZ2, AZ3).
  - Băng thông đỉnh mỗi vùng: $30\text{ Mbps} / 3 = 10\text{ Mbps/Zone}$.
  - **Dung lượng dự phòng tối thiểu mỗi vùng:** Thiết lập đường truyền cam kết tối thiểu **$50\text{ Mbps} - 100\text{ Mbps}$/Zone** (có khả năng burst lên $1\text{ Gbps}$) để chịu được kịch bản sập hoàn toàn 1 AZ mà 2 AZ còn lại vẫn chịu tải 100%.
- **Chính sách tự động co giãn (Autoscaling & Alert Policies):**
  - **Storage Threshold Trigger:** Kích hoạt cảnh báo và tự động mở rộng dung lượng ổ đĩa (Storage Auto-expand) khi dung lượng sử dụng **vượt quá $80\%$ liên tục trong 5 phút**.
  - **Compute Scaling Rule:** Kích hoạt Horizontal Pod Autoscaler (HPA) tăng số Pods khi mức sử dụng CPU/RAM trung bình vượt quá $70\%$.
  - **Network Bandwidth Trigger:** Cảnh báo nghẽn mạng khi Throughput chạm ngưỡng $80\%$ giới hạn của Direct Link / Transit Gateway.

---

# TASK 4: CAPACITY PLANNING VALIDATION CHECKLIST

| Hạng mục đối soát (Validation Item) | Kết quả kiểm tra | Minh chứng kiến trúc & Đánh giá |
| :--- | :---: | :--- |
| **1. Compute plan includes buffer for HA** | **ĐẠT** | Bổ sung $30\%$ buffer an toàn, quy đổi ra $162.5\text{ vCPU}$ và $162.5\text{ GB RAM}$, đáp ứng failover khi có node gặp sự cố. |
| **2. Container types cloud-specific & properly sized** | **ĐẠT** | Định cỡ Pod chuẩn ($2\text{ vCPU} / 4\text{ GB}$) và ánh xạ sang Worker Nodes chuẩn Cloud (`m6i.4xlarge` / `bx2-16x64`) phân bổ trên 3 AZs. |
| **3. Storage plan covers indexing, retention & archiving** | **ĐẠT** | Tính đủ $13\text{ tháng}$ online ($156\text{ GB}$ bao gồm $20\%$ index overhead) và phân tầng sang Cold Object Storage ($120\text{ GB/năm}$). |
| **4. Bandwidth plan includes scaling rules & redundancy** | **ĐẠT** | Tính toán băng thông đỉnh $30\text{ Mbps}$ (bao gồm $25\%$ redundancy overhead), phân bổ đa vùng và quy tắc co giãn tự động tại ngưỡng $>80\%$ trong 5 phút. |
| **5. Fault tolerance and cost controls alignment** | **ĐẠT** | Cấu hình dự phòng $N+1$, mô hình Multi-AZ đảm bảo SLA 99.99% và tối ưu chi phí qua mô hình lưu trữ phân tầng (Tiered Storage). |
