-- ==============================================================================
-- DigiHealth Modernization Initiative
-- Part 2 - Task 2A: PostgreSQL OLAP Data Warehouse DDL & DML Scripts
-- Target RDBMS: PostgreSQL 12+
-- Database: digihealth_dw
-- Schema Model: Star Schema (Dimensional Modeling)
-- ==============================================================================

-- 1. SCHEMA CREATION
CREATE SCHEMA IF NOT EXISTS clinical_dw;
SET search_path TO clinical_dw, public;

-- Drop existing tables in reverse dependency order (Fact first, then Dimensions)
DROP TABLE IF EXISTS fact_appointments CASCADE;
DROP TABLE IF EXISTS dim_service CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;
DROP TABLE IF EXISTS dim_doctor CASCADE;
DROP TABLE IF EXISTS dim_patient CASCADE;

-- ==============================================================================
-- 2. DIMENSION TABLES DDL (CREATE STATEMENTS)
-- ==============================================================================

-- 2.1. Patient Dimension (Dim Patient)
CREATE TABLE dim_patient (
    patient_key SERIAL PRIMARY KEY,              -- Surrogate Key
    patient_id INT NOT NULL,                     -- Natural / Business Key
    full_name VARCHAR(120) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    birth_year INT NOT NULL,
    age_group VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    effective_start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- 2.2. Doctor Dimension (Dim Doctor)
CREATE TABLE dim_doctor (
    doctor_key SERIAL PRIMARY KEY,               -- Surrogate Key
    doctor_id INT NOT NULL,                      -- Natural / Business Key
    doctor_name VARCHAR(120) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    clinic_location VARCHAR(150) NOT NULL,
    effective_start_date DATE NOT NULL DEFAULT CURRENT_DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE
);

-- 2.3. Date Dimension (Dim Date)
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,                    -- Format: YYYYMMDD
    full_date DATE NOT NULL UNIQUE,
    day_number INT NOT NULL,
    day_name VARCHAR(20) NOT NULL,
    month_number INT NOT NULL,
    month_name VARCHAR(20) NOT NULL,
    quarter INT NOT NULL,
    year INT NOT NULL,
    is_weekend BOOLEAN NOT NULL
);

-- 2.4. Service Dimension (Dim Service)
CREATE TABLE dim_service (
    service_key SERIAL PRIMARY KEY,              -- Surrogate Key
    service_code VARCHAR(50) NOT NULL UNIQUE,
    service_name VARCHAR(150) NOT NULL,
    service_category VARCHAR(100) NOT NULL,
    standard_cost NUMERIC(10, 2) NOT NULL
);

-- ==============================================================================
-- 3. FACT TABLE DDL (CREATE STATEMENT)
-- ==============================================================================

CREATE TABLE fact_appointments (
    appointment_fact_id BIGSERIAL PRIMARY KEY,
    -- Foreign Keys to Dimensions
    patient_key INT NOT NULL,
    doctor_key INT NOT NULL,
    date_key INT NOT NULL,
    service_key INT NOT NULL,
    
    -- Degenerate Dimensions / Operational Keys
    appointment_id INT NOT NULL,
    
    -- Numerical Facts / Metrics
    consultation_fee NUMERIC(10, 2) NOT NULL,
    total_billed_amount NUMERIC(10, 2) NOT NULL,
    visit_duration_minutes INT DEFAULT 30,
    appointment_count INT DEFAULT 1,
    is_completed INT DEFAULT 1,
    
    -- Foreign Key Constraints
    CONSTRAINT fk_fact_patient FOREIGN KEY (patient_key)
        REFERENCES dim_patient (patient_key) ON DELETE RESTRICT,
    CONSTRAINT fk_fact_doctor FOREIGN KEY (doctor_key)
        REFERENCES dim_doctor (doctor_key) ON DELETE RESTRICT,
    CONSTRAINT fk_fact_date FOREIGN KEY (date_key)
        REFERENCES dim_date (date_key) ON DELETE RESTRICT,
    CONSTRAINT fk_fact_service FOREIGN KEY (service_key)
        REFERENCES dim_service (service_key) ON DELETE RESTRICT
);

-- Optimization Indexes for Dimensional Star Query Joins
CREATE INDEX idx_fact_patient_key ON fact_appointments(patient_key);
CREATE INDEX idx_fact_doctor_key ON fact_appointments(doctor_key);
CREATE INDEX idx_fact_date_key ON fact_appointments(date_key);
CREATE INDEX idx_fact_service_key ON fact_appointments(service_key);

-- ==============================================================================
-- 4. DML INSERT SCRIPTS (ANALYTICAL SAMPLE DATA SEEDING)
-- ==============================================================================

-- 4.1. Populate Dim Patient
INSERT INTO dim_patient (patient_id, full_name, gender, birth_year, age_group, city) VALUES
(1, 'John Doe', 'Male', 1985, '36-50', 'Springfield'),
(2, 'Emily Clark', 'Female', 1992, '26-35', 'Springfield'),
(3, 'James Wilson', 'Male', 1978, '36-50', 'Capital City'),
(4, 'Sophia Martinez', 'Female', 2015, '0-18', 'Shelbyville'),
(5, 'William Anderson', 'Male', 1960, '60+', 'Springfield');

-- 4.2. Populate Dim Doctor
INSERT INTO dim_doctor (doctor_id, doctor_name, specialization, department_name, clinic_location) VALUES
(1, 'Dr. Robert Smith', 'Cardiologist', 'Cardiology', 'Building A, Floor 2'),
(2, 'Dr. Alice Johnson', 'Neurologist', 'Neurology', 'Building B, Floor 3'),
(3, 'Dr. David Lee', 'Pediatrician', 'Pediatrics', 'Building A, Floor 1'),
(4, 'Dr. Sarah Brown', 'Orthopedic Surgeon', 'Orthopedics', 'Building C, Floor 2'),
(5, 'Dr. Michael Taylor', 'General Physician', 'General Medicine', 'Building A, Floor 1');

-- 4.3. Populate Dim Date
INSERT INTO dim_date (date_key, full_date, day_number, day_name, month_number, month_name, quarter, year, is_weekend) VALUES
(20260910, '2026-09-10', 10, 'Thursday', 9, 'September', 3, 2026, FALSE),
(20260911, '2026-09-11', 11, 'Friday', 9, 'September', 3, 2026, FALSE),
(20260912, '2026-09-12', 12, 'Saturday', 9, 'September', 3, 2026, TRUE),
(20260915, '2026-09-15', 15, 'Tuesday', 9, 'September', 3, 2026, FALSE),
(20260918, '2026-09-18', 18, 'Friday', 9, 'September', 3, 2026, FALSE);

-- 4.4. Populate Dim Service
INSERT INTO dim_service (service_code, service_name, service_category, standard_cost) VALUES
('SRV-CARD-01', 'Cardiac Consultation & ECG', 'Cardiology', 250.00),
('SRV-NEUR-01', 'Neurological Evaluation', 'Neurology', 180.00),
('SRV-ORTH-01', 'Orthopedic Consultation & Joint Exam', 'Orthopedics', 320.00),
('SRV-PED-01', 'Pediatric Routine Checkup & Vaccine', 'Pediatrics', 150.00),
('SRV-GEN-01', 'General Health Assessment', 'General Medicine', 200.00);

-- 4.5. Populate Fact Appointments
INSERT INTO fact_appointments (patient_key, doctor_key, date_key, service_key, appointment_id, consultation_fee, total_billed_amount, visit_duration_minutes, appointment_count, is_completed) VALUES
(1, 1, 20260910, 1, 1, 250.00, 250.00, 45, 1, 1),
(2, 2, 20260911, 2, 2, 180.00, 180.00, 40, 1, 1),
(3, 4, 20260912, 3, 3, 320.00, 320.00, 50, 1, 1),
(4, 3, 20260915, 4, 4, 150.00, 150.00, 30, 1, 1),
(5, 5, 20260918, 5, 5, 200.00, 200.00, 35, 1, 1);
