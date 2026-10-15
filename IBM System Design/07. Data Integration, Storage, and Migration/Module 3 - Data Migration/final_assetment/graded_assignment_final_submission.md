# Coursera Graded Assignment: Final Project Submission
## Consolidating Customer Data Across Legacy Systems for RetailCorp

> **Course:** IBM System Design — 07. Data Integration, Storage, and Migration  
> **Module:** Module 3 - Data Migration  
> **Activity:** Graded Assignment: Final Project Submission (20 Points)

---

### Task 1: Data Integration Pattern Selection (3 points)

#### Prompt:
> Which pattern do you think is most appropriate for RetailCorp? (1 point)  
> Provide two reasons that support your choice. (2 points)

#### Answer:
```text
The most appropriate pattern for RetailCorp is Extract-Transform-Load (ETL).

First, RetailCorp collects customer data from five heterogeneous legacy source systems (CRM, POS, E-commerce, Loyalty, and Marketing) that have varying schemas, inconsistent data formatting, and duplicate records. The traditional ETL pattern ensures that all records are thoroughly cleansed, standardized, deduplicated, and unified through Master Data Management (MDM) before they are loaded into the target central repository, preventing dirty data from polluting the data warehouse.

Second, using an ETL pattern with a temporary staging area isolates intensive data transformation workloads from the central data warehouse and production transactional databases. This staging and pre-cleansing approach protects system performance and minimizes operational disruption across RetailCorp's 200+ retail stores during active business hours.
```

---

### Task 2: Stages of the ETL Process at RetailCorp (3 points)

#### Prompt:
> Briefly explain an activity that needs to be completed at each stage of the ETL process: Extract, Transform, Load.  
> Provide a brief explanation of each activity as it applies to RetailCorp. (3 points)

#### Answer:
```text
1. Extract: RetailCorp must extract customer, sales, and interaction data from its five legacy source systems (such as daily sales logs from on-premise POS systems across 200+ stores, online purchase logs from the E-commerce platform, and contact histories from the CRM) using specialized extractors, database connectors, and streaming ingestion into a temporary staging area without disrupting store operations.

2. Transform: In the Data Transformation Layer, RetailCorp cleanses, deduplicates, and standardizes disparate customer records. This activity includes resolving schema mismatches (e.g., standardizing phone numbers, postal addresses, and timestamps), applying business rules, and performing identity resolution via Master Data Management (MDM) to merge fragmented profiles into a single unified customer view (Golden Record).

3. Load: The finalized, enriched, and validated customer records are ingested from staging into the target Cloud Data Warehouse (and raw semi-structured logs into the Data Lake). This step includes writing partitioned data, building query indexing structures, and verifying referential integrity to enable fast reporting and analytics for business intelligence and marketing teams.
```

---

### Task 3: Connectors & Integration Mechanism (4 points)

#### Prompt:
> Using the pipeline diagram, identify two places RetailCorp needs to use a connector. (2 points)  
> Provide a reason that supports each of your choices. (2 points)

#### Answer:
```text
1. Place 1: Between the Legacy Source Systems (e.g., POS terminals and CRM) and the Data Ingestion Layer (Extractors / ETL Tool).
Reason: RetailCorp operates physical POS terminals across 200+ stores alongside a relational CRM database. A Database Connector (such as JDBC/ODBC) or an API Connector is required to securely query, authenticate, and extract raw transactional logs and customer profiles directly from diverse underlying database engines without schema conflicts.

2. Place 2: Between the Ingestion/Transformation Layer and the Central Data Warehouse (Target Storage).
Reason: The centralized repository resides on a modern cloud data platform (such as Snowflake, Google BigQuery, or Amazon Redshift). A dedicated Cloud Connector or Native Warehouse Connector is necessary to establish encrypted network connections and bulk-load transformed, standardized customer datasets efficiently using optimized cloud storage and ingestion APIs.
```

---

### Task 4: Cloud Storage Options for the Data Lake (1 point)

#### Prompt:
> Choose a type of cloud storage and explain why you think that type of storage would be useful to RetailCorp’s data lake strategy. (1 point)

#### Answer:
```text
I choose Object Storage (such as Amazon S3, Google Cloud Storage, or Azure Blob Storage) for RetailCorp’s data lake strategy. 

Object storage provides massive, cost-effective scalability and high durability for storing vast volumes of unstructured and semi-structured raw data (such as raw JSON clickstream events from e-commerce, raw marketing logs, and uncurated POS transactions). Furthermore, object storage decouples storage from compute, allowing RetailCorp to store raw historical customer data indefinitely for auditing, machine learning, and future reprocessing at a fraction of the cost of high-performance database storage.
```

---

### Task 5: Backup Fundamentals (2 points)

#### Prompt:
> Choose a backup technique you think would be useful for RetailCorp’s data. (1 point)  
> Explain why you think that the backup technique would be useful for RetailCorp’s data. (1 point)

#### Answer:
```text
I recommend a Hybrid Full and Incremental Cloud Backup technique (or Cloud-based Incremental Backup).

RetailCorp handles continuous sales transactions across more than 200 physical locations and an online store. Performing a full backup every day would consume excessive network bandwidth, cloud storage costs, and computing overhead. By executing a scheduled weekly full backup supplemented by daily or hourly incremental backups, the company only captures data that has changed since the previous backup. This significantly shortens the backup window, optimizes storage utilization, minimizes network impact, and maintains a strict Recovery Point Objective (RPO) for rapid disaster recovery.
```

---

### Task 6: Migration Approach: Big Bang vs. Trickle (2 points)

#### Prompt:
> Which approach do you think would be best for the organization? (1 point)  
> Provide a reason that supports your choice. (1 point)

#### Answer:
```text
The Trickle Migration approach (Phased Migration / Parallel Running) is the best choice for RetailCorp.

RetailCorp operates 200+ physical stores and an active 24/7 e-commerce platform. A Big Bang migration carries an unacceptable business risk; if cutover failure or data corruption occurs during a single weekend window, physical store checkouts and online transactions would be halted, resulting in catastrophic revenue and reputational loss. A Trickle migration enables the team to migrate sub-systems incrementally (such as migrating loyalty and marketing data first before migrating live POS transactions), running systems in parallel and validating data integrity thoroughly with zero disruption to daily sales.
```

---

### Task 7: Data Migration Steps Mapped to the Pipeline Diagram (5 points)

#### Prompt:
> Select two of these steps and compare them to the pipeline diagram:  
> Planning and assessment, Data extraction, Data transformation, Data loading, Validation and testing.  
> 1. Name the two steps you chose. (1 point)  
> 2. Describe which parts of the diagram are associated with those steps. (2 points)  
> 3. Explain why you believe those steps apply to those parts of the pipeline diagram. (2 points)

#### Answer:
```text
1. Selected Steps: Data Extraction and Data Transformation.

2. Associated Parts in the Pipeline Diagram:
- Data Extraction is directly associated with the Source Systems (Legacy Systems), the Data Ingestion Layer (specifically the Extractors, ETL Tool Extraction stage, and Streaming Data components), and the Staging Area.
- Data Transformation is directly associated with the Data Transformation Layer (including Data Quality Services, Data Mapping and Transformation, Business Logic Implementation, and Master Data Management - MDM).

3. Explanation of Alignment:
- Data Extraction applies to the Ingestion Layer and Staging because its primary objective is reading and extracting data from the 5 legacy databases (POS, CRM, E-commerce, Loyalty, Marketing) and securely delivering raw copies into the temporary staging area without altering the source systems.
- Data Transformation applies to the Transformation Layer because it takes the staged raw data and applies cleansing, deduplication, schema alignment, and business logic. Specifically, the MDM component resolves disparate identities into a single customer golden record, fulfilling the core requirements of the migration transformation stage before loading into the target data warehouse.
```
