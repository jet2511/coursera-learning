# Additional Resources & Documentation (Domain 1 - Design Secure Architectures)

Tổng hợp các liên kết tài liệu kỹ thuật chính thức (Official AWS Documentation & Whitepapers) phục vụ đào sâu kiến thức cho **Domain 1: Design Secure Architectures**.

---

## 1. Account Management & Identity Access Management (IAM)
- [Managing Your AWS Account](https://docs.aws.amazon.com/accounts/latest/reference/managing-accounts.html): Hướng dẫn quản trị tài khoản, bảo vệ Root User, phân quyền danh tính và thiết lập cấu hình bảo mật tài khoản.
- [What is AWS IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html): Tài liệu đặc tả dịch vụ IAM, cơ chế IAM Policies (Identity vs Resource Policies), IAM Roles, STS và Federation.
- [Security, Identity, and Compliance Overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-services.html): Whitepaper tổng quan về các dịch vụ bảo mật, danh tính và tuân thủ trên AWS.

---

## 2. VPC & Network Security
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html): Kiến trúc mạng riêng ảo, cấu hình Subnets (Public/Private), Route Tables, Internet Gateways & NAT Gateways.
- [Security in Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/security.html): Thiết kế bảo mật mạng chuyên sâu với Security Groups, Network ACLs, VPC Flow Logs và VPC Endpoints.

---

## 3. Data Encryption & Storage Security
- [Data Encryption in AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/data-encryption.html): Whitepaper chi tiết về nguyên lý mã hóa tĩnh (At-Rest), mã hóa động (In-Transit), AWS KMS và AWS CloudHSM.
- [Amazon S3 Cross-Region Replication (CRR)](http://aws.amazon.com/s3/features/replication/): Cơ chế tự động sao chép object bất đồng bộ qua các AWS Regions khác nhau phục vụ Disaster Recovery và giảm độ trễ truy cập.

---

## 4. Backup, Snapshots & Disaster Recovery Services
- [Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html): Tạo snapshot gia tăng (incremental), mã hóa bản sao snapshot và khôi phục EBS volumes.
- [Point-in-Time Recovery (PITR) for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html): Khôi phục dữ liệu NoSQL về bất kỳ giây nào trong 35 ngày qua mà không ảnh hưởng hiệu năng.
- [Backing up and Restoring an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html): Cơ chế sao lưu tự động (Automated Backups) và manual snapshots trên RDS.
- [Creating a DB Cluster Snapshot (Amazon Aurora)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html): Sao lưu cụm cơ sở dữ liệu phân tán Amazon Aurora.
- [Using AWS Backup to Back up and Restore Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html): Tích hợp quản trị sao lưu tập trung cho hệ thống tệp dùng chung EFS.
- [Amazon Redshift Snapshots and Backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html): Quản lý automated/manual snapshots cho kho dữ liệu Data Warehouse Redshift.
- [Overview of Backing up and Restoring Neptune DB Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview.html): Sao lưu và phục hồi cơ sở dữ liệu đồ thị Amazon Neptune.
- [Backing up and Restoring in Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore.html): Quản lý sao lưu cho DocumentDB (tương thích MongoDB).

---

## 5. Danh mục Dịch vụ Core liên quan (Official Portals)
- [AWS Backup](http://aws.amazon.com/backup)
- [Amazon Elastic Block Store (EBS)](http://aws.amazon.com/ebs/)
- [Amazon EC2](http://aws.amazon.com/ec2/)
- [Amazon Relational Database Service (RDS)](http://aws.amazon.com/rds/) & [Amazon Aurora](http://aws.amazon.com/rds/aurora/)
- [Amazon DynamoDB](http://aws.amazon.com/dynamodb/)
- [Amazon Elastic File System (EFS)](http://aws.amazon.com/efs/)
- [AWS Storage Gateway](http://aws.amazon.com/storagegateway/)
- [Amazon FSx for Windows File Server & Lustre](http://aws.amazon.com/fsx/windows/)

