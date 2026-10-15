# Coursera Graded Assignment: Final Project Submission
## Consolidating Customer Data Across Legacy Systems for RetailCorp

---

### Task 1: Data Integration Pattern Selection (3 points)

#### Prompt:
> Which pattern do you think is most appropriate for RetailCorp? (1 point)  
> Provide two reasons that support your choice. (2 points)

#### Answer:
**Selected Pattern:** Extract-Transform-Load (ETL) combined with Change Data Capture (CDC). *(Or ETL)*

**Justification & Reasons:**
1. **Diverse Legacy Data Formats and High Data Cleansing Requirements:** RetailCorp gathers customer information from five disparate legacy systems (CRM, POS, E-commerce, Loyalty, and Marketing) that have varying schemas, duplicate profiles, and inconsistent formatting. The traditional ETL pattern ensures data is thoroughly cleansed, validated, deduplicated, and unified through Master Data Management (MDM) before being loaded into the central data warehouse, ensuring high-quality analytics.
2. **Minimizing Operational Disruption via Staging:** Running intensive transformations prior to loading protects the centralized data warehouse from performance degradation and avoids overburdening the legacy transactional systems. Utilizing an ETL pipeline with a staging area allows RetailCorp to standardize transactional records into a single customer view (Golden Record) without locking production databases during peak store operational hours.

---

### Task 2: Stages of the ETL Process at RetailCorp (3 points)

#### Prompt:
> Briefly explain an activity that needs to be completed at each stage of the ETL process: Extract, Transform, Load.  
> Provide a brief explanation of each activity as it applies to RetailCorp. (3 points)

#### Answer:
1. **Extract:**  
   *Activity for RetailCorp:* Pulling customer and transactional data from disparate legacy systems (such as daily sales logs from on-premise POS systems across 200+ stores, online purchase logs from the E-commerce platform, and contact histories from the CRM) using specialized database connectors, APIs, and scheduled batch extraction scripts into a temporary staging area without impacting daily transactional operations.
2. **Transform:**  
   *Activity for RetailCorp:* Cleaning, deduplicating, and standardizing disparate customer records in the Data Transformation and MDM Layer. This involves resolving discrepancies across records (e.g., standardizing phone numbers, addresses, and ISO date formats), implementing business logic, and executing identity resolution to merge duplicate profiles across POS and E-commerce into a single Master Customer Record.
3. **Load:**  
   *Activity for RetailCorp:* Ingesting the structured, validated, and enriched customer records from the staging area into the target Cloud Data Warehouse tables (and raw logs into the Data Lake). This step includes writing partitioned records, updating indexing structures, and verifying referential integrity so that downstream business intelligence and marketing tools can perform high-speed analytical queries.

---

### Task 3: Connectors & Integration Mechanism (4 points)

#### Prompt:
> Using the pipeline diagram, identify two places RetailCorp needs to use a connector. (2 points)  
> Provide a reason that supports each of your choices. (2 points)

#### Answer:
1. **Place 1: Between Legacy Source Systems (POS / CRM) and the Data Ingestion Layer (Extractors / ETL Tool)**  
   *Type of Connector:* **Database Connector / API Connector**  
   *Reason:* RetailCorp operates physical POS terminals across 200+ retail stores and an enterprise CRM database. Reliable database connectors (e.g., JDBC/ODBC) or REST API connectors are mandatory to securely interface with the underlying relational databases and third-party software interfaces, allowing extraction scripts to query sales transactions and customer profiles directly without schema conflicts.

2. **Place 2: Between the Ingestion / Transformation Layer and the Central Data Warehouse (Target Storage)**  
   *Type of Connector:* **Cloud Connector / Native Data Warehouse Connector**  
   *Reason:* The centralized repository resides on a modern cloud data platform (such as Snowflake, Google BigQuery, or Amazon Redshift). A dedicated high-throughput cloud connector is required to authenticate, establish encrypted connections, and bulk-load transformed, standardized customer datasets efficiently using native cloud storage staging and streaming ingest APIs.

---

### Task 4: Cloud Storage Options for the Data Lake (1 point)

#### Prompt:
> Choose a type of cloud storage and explain why you think that type of storage would be useful to RetailCorp’s data lake strategy. (1 point)

#### Answer:
**Selected Storage Type:** **Object Storage** (e.g., Amazon S3, Google Cloud Storage, or Azure Blob Storage).

**Explanation:**  
Object storage is the ideal solution for RetailCorp’s data lake because it provides virtually limitless scalability, high durability, and cost-effective pricing for storing vast amounts of raw, structured, and semi-structured data (such as raw JSON payloads from e-commerce sessions, web clickstreams, and marketing campaign logs). Furthermore, object storage decouples compute from storage, allowing RetailCorp to store historical data indefinitely for auditing, machine learning, and reprocessing without paying for expensive database compute capacity.

---

### Task 5: Backup Fundamentals (2 points)

#### Prompt:
> Choose a backup technique you think would be useful for RetailCorp’s data. (1 point)  
> Explain why you think that the backup technique would be useful for RetailCorp’s data. (1 point)

#### Answer:
**Selected Backup Technique:** **Hybrid Full and Incremental Backup** (or Cloud-based Incremental Backup).

**Explanation:**  
RetailCorp handles millions of sales transactions weekly across 200+ stores. Performing a full backup daily would consume excessive network bandwidth, storage costs, and computing resources. A strategy of scheduled weekly full backups complemented by daily/hourly incremental backups captures only newly modified or added customer transactions. This drastically reduces the backup window and network overhead while ensuring a low Recovery Point Objective (RPO) and rapid disaster recovery in case of system failure.

---

### Task 6: Migration Approach: Big Bang vs. Trickle (2 points)

#### Prompt:
> Which approach do you think would be best for the organization? (1 point)  
> Provide a reason that supports your choice. (1 point)

#### Answer:
**Selected Approach:** **Trickle Migration (Phased Migration / Parallel Running)**.

**Explanation:**  
RetailCorp is an active enterprise running 200+ physical stores and an ongoing 24/7 e-commerce platform. A Big Bang migration carries an unacceptable business risk; any data corruption, failed cutover, or unexpected downtime over a single weekend would directly shut down cash registers, stop online checkouts, and result in severe revenue and reputation loss. A Trickle migration allows RetailCorp to migrate subsystems incrementally (e.g., migrating loyalty and marketing data first before migrating live POS transactions), running systems in parallel and validating data accuracy thoroughly without interrupting daily customer sales.

---

### Task 7: Data Migration Steps Mapped to the Pipeline Diagram (5 points)

#### Prompt:
> Select two of these steps and compare them to the pipeline diagram:  
> Planning and assessment, Data extraction, Data transformation, Data loading, Validation and testing.  
> 1. Name the two steps you chose. (1 point)  
> 2. Describe which parts of the diagram are associated with those steps. (2 points)  
> 3. Explain why you believe those steps apply to those parts of the pipeline diagram. (2 points)

#### Answer:
1. **Selected Steps:**  
   - Step 1: **Data Extraction**  
   - Step 2: **Data Transformation**

2. **Associated Parts of the Pipeline Diagram:**  
   - **Data Extraction** is directly associated with the **Source Systems (Legacy Systems)**, the **Data Ingestion Layer** (specifically the *Extractors*, *ETL Tool Extraction stage*, and *Streaming Data components*), and the **Staging Area**.  
   - **Data Transformation** is directly associated with the **Data Transformation Layer** (including *Data Quality Services*, *Data Mapping and Transformation*, *Business Logic Implementation*, and *Master Data Management - MDM*).

3. **Explanation of Alignment:**  
   - *Why Data Extraction applies:* In the diagram, the Data Ingestion Layer utilizes extractors and streaming components to pull records out of the 5 legacy databases (POS, CRM, E-commerce, Loyalty, Marketing) and deliver them into the temporary staging area. This mirrors the formal Data Extraction phase of migration, which focuses on reading and retrieving raw source data without altering the production sources.  
   - *Why Data Transformation applies:* Once raw data reaches staging, the Data Transformation Layer applies data quality rules, cleanses duplicate entries, standardizes formats across different store systems, and uses MDM to unify customer entities into a single golden record. This directly executes the Data Transformation step of migration, ensuring that legacy schema discrepancies and data inconsistencies are resolved before final loading into the central data warehouse.
