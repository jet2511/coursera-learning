# AWS Multi-Account Best Practices: Synergy Between Tag Policies and SCPs

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Multi-Account Best Practices (Tag Policies vs. Service Control Policies)  

---

## 1. Mối quan hệ tương hỗ: Tag Policies kết hợp SCPs

Một trong những câu hỏi kiến trúc kinh điển là: **"Làm sao để bắt buộc gắn thẻ (tagging) một cách tuyệt đối trên toàn bộ các tài khoản AWS?"**

Câu trả lời nằm ở sự phối hợp chặt chẽ giữa **Tag Policies** và **SCPs**:

| Tiêu chí | Tag Policies (Chuẩn hóa cú pháp & Chống sửa) | Service Control Policies - SCPs (Chặn tạo mới nếu thiếu thẻ) |
| :--- | :--- | :--- |
| **Vai trò chính** | Định nghĩa cú pháp thẻ chuẩn (tên thẻ, kiểu chữ hoa/thường, danh sách giá trị hợp lệ). | Thực thi nguyên tắc bắt buộc: *"No Tag, No Launch"*. |
| **Cơ chế kiểm soát** | Ngăn chặn người dùng **sửa hoặc gán sai tag** trên các tài nguyên **ĐANG CHẠY**. | Chặn ngay tại thời điểm gọi API (`RunInstances`, `CreateSecret`...) nếu request **thiếu tag bắt buộc**. |
| **Điểm hạn chế** | **KHÔNG** chặn được việc người dùng tạo mới tài nguyên không gắn thẻ. | Không kiểm tra sâu được cú pháp/giá trị hợp lệ phức tạp của thẻ (chỉ kiểm tra có/không có thẻ). |
| **Kết quả bảo vệ** | Đảm bảo tính nhất quán dữ liệu cho báo cáo chi phí và kiểm toán. | Triệt tiêu hoàn toàn tình trạng tài nguyên "mồ côi" không được gắn thẻ. |

---

## 2. Chi tiết cấu hình mẫu (Policy Examples)

### 2.1. AWS Organizations Tag Policy (Chuẩn hóa thẻ)
Chính sách này định nghĩa tag `Environment` với giá trị chuẩn là `Production` và áp dụng cho EC2 instances:

```json
{
  "tags": {
    "Environment": {
      "tag_key": {
        "@@assign": "Environment"
      },
      "tag_value": {
        "@@assign": [
          "Production"
        ]
      },
      "enforced_for": {
        "@@assign": [
          "ec2:instance"
        ]
      }
    }
  }
}
```
* **Ý nghĩa:** Chặn không cho user đổi hoặc gán sai giá trị tag trên các EC2 instance đã khởi chạy.

---

### 2.2. Service Control Policy - SCP (Bắt buộc phải có thẻ khi tạo mới)
Để ngăn chặn hoàn toàn việc người dùng bấm tạo máy ảo hoặc bí mật (secret) mà **quên gắn thẻ**, sử dụng mệnh đề `Deny` kết hợp điều kiện `Null: aws:RequestTag/<TagName> = "true"`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyCreateSecretWithNoProjectTag",
      "Effect": "Deny",
      "Action": "secretsmanager:CreateSecret",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:RequestTag/Project": "true"
        }
      }
    },
    {
      "Sid": "DenyRunInstanceWithNoProjectTag",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:volume/*"
      ],
      "Condition": {
        "Null": {
          "aws:RequestTag/Project": "true"
        }
      }
    },
    {
      "Sid": "DenyCreateSecretWithNoCostCenterTag",
      "Effect": "Deny",
      "Action": "secretsmanager:CreateSecret",
      "Resource": "*",
      "Condition": {
        "Null": {
          "aws:RequestTag/CostCenter": "true"
        }
      }
    },
    {
      "Sid": "DenyRunInstanceWithNoCostCenterTag",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:volume/*"
      ],
      "Condition": {
        "Null": {
          "aws:RequestTag/CostCenter": "true"
        }
      }
    }
  ]
}
```

---

## 3. Các tài liệu tham khảo cốt lõi (Core Whitepapers & References)

1. **Whitepaper:** [Organizing Your AWS Environments Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
   * Hướng dẫn thiết kế cấu trúc OU chi tiết: Security OU, Core OU, Workload OUs (Internal vs Public-facing).
2. **AWS Blog:** [Best Practices for AWS Organizations Service Control Policies in a Multi-Account Environment](https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/)
   * Mô hình phân tầng và các mẫu SCP guardrails thực chiến.
3. **AWS User Guide:** [Require a tag on specified created resources](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-tag-on-create)
   * Chi tiết kỹ thuật áp dụng điều kiện `aws:RequestTag` trong SCPs.
