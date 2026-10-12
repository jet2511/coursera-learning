-- ==============================================================================
-- DigiHealth Modernization Initiative
-- Part 2 - Task 1: MySQL OLTP Database DDL & DML Scripts
-- Target RDBMS: MySQL 8.0+
-- Database: digihealth_oltp
-- ==============================================================================

-- 1. DATABASE CREATION
CREATE DATABASE IF NOT EXISTS digihealth_oltp
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE digihealth_oltp;

-- Drop existing tables in reverse foreign-key dependency order
DROP TABLE IF EXISTS billing;
DROP TABLE IF EXISTS medical_records;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS patients;

-- ==============================================================================
-- 2. DDL DEFINITIONS (CREATE TABLE STATEMENTS - 3NF COMPLIANT)
-- ==============================================================================

-- 2.1. Departments Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(150) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2.2. Doctors Table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_doctors_department FOREIGN KEY (department_id)
        REFERENCES departments (department_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- 2.3. Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2.4. Appointments Table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-Show') DEFAULT 'Scheduled',
    reason_for_visit VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_appointments_patient FOREIGN KEY (patient_id)
        REFERENCES patients (patient_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_appointments_doctor FOREIGN KEY (doctor_id)
        REFERENCES doctors (doctor_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- 2.5. Medical Records Table
CREATE TABLE medical_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis TEXT NOT NULL,
    prescription TEXT,
    treatment_notes TEXT,
    record_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_records_patient FOREIGN KEY (patient_id)
        REFERENCES patients (patient_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_records_doctor FOREIGN KEY (doctor_id)
        REFERENCES doctors (doctor_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- 2.6. Billing Table
CREATE TABLE billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_id INT NOT NULL UNIQUE,
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    payment_status ENUM('Pending', 'Paid', 'Refunded') DEFAULT 'Pending',
    payment_method ENUM('Cash', 'Credit Card', 'Insurance', 'Bank Transfer') NOT NULL,
    billing_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_billing_patient FOREIGN KEY (patient_id)
        REFERENCES patients (patient_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT fk_billing_appointment FOREIGN KEY (appointment_id)
        REFERENCES appointments (appointment_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ==============================================================================
-- 3. DML INSERT SCRIPTS (SAMPLE DATA SEEDING)
-- ==============================================================================

-- 3.1. Insert Departments
INSERT INTO departments (department_name, location) VALUES
('Cardiology', 'Building A, Floor 2'),
('Neurology', 'Building B, Floor 3'),
('Pediatrics', 'Building A, Floor 1'),
('Orthopedics', 'Building C, Floor 2'),
('General Medicine', 'Building A, Floor 1');

-- 3.2. Insert Doctors
INSERT INTO doctors (first_name, last_name, specialization, contact_number, email, department_id) VALUES
('Robert', 'Smith', 'Cardiologist', '555-0101', 'dr.smith@digihealth.org', 1),
('Alice', 'Johnson', 'Neurologist', '555-0102', 'dr.johnson@digihealth.org', 2),
('David', 'Lee', 'Pediatrician', '555-0103', 'dr.lee@digihealth.org', 3),
('Sarah', 'Brown', 'Orthopedic Surgeon', '555-0104', 'dr.brown@digihealth.org', 4),
('Michael', 'Taylor', 'General Physician', '555-0105', 'dr.taylor@digihealth.org', 5);

-- 3.3. Insert Patients
INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_number, email, address) VALUES
('John', 'Doe', '1985-04-12', 'Male', '555-1001', 'john.doe@email.com', '123 Elm St, Springfield'),
('Emily', 'Clark', '1992-08-25', 'Female', '555-1002', 'emily.c@email.com', '456 Oak Ave, Springfield'),
('James', 'Wilson', '1978-11-03', 'Male', '555-1003', 'jwilson@email.com', '789 Pine Rd, Capital City'),
('Sophia', 'Martinez', '2015-06-19', 'Female', '555-1004', 'smartinez@email.com', '321 Maple Dr, Shelbyville'),
('William', 'Anderson', '1960-01-30', 'Male', '555-1005', 'wanderson@email.com', '654 Birch Ln, Springfield');

-- 3.4. Insert Appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status, reason_for_visit) VALUES
(1, 1, '2026-09-10', '09:00:00', 'Completed', 'Routine cardiac checkup'),
(2, 2, '2026-09-11', '10:30:00', 'Completed', 'Chronic migraine consultation'),
(3, 4, '2026-09-12', '14:00:00', 'Completed', 'Knee joint pain after workout'),
(4, 3, '2026-09-15', '11:00:00', 'Completed', 'Annual pediatric vaccination & checkup'),
(5, 5, '2026-09-18', '08:30:00', 'Completed', 'Blood pressure monitoring');

-- 3.5. Insert Medical Records
INSERT INTO medical_records (patient_id, doctor_id, diagnosis, prescription, treatment_notes, record_date) VALUES
(1, 1, 'Mild Hypertension', 'Amlodipine 5mg daily', 'Recommended low sodium diet and 30min cardio exercise.', '2026-09-10 09:45:00'),
(2, 2, 'Tension Headache', 'Sumatriptan 50mg as needed', 'Advised stress reduction techniques and regular sleep schedule.', '2026-09-11 11:15:00'),
(3, 4, 'Patellar Tendinitis', 'Ibuprofen 400mg, Physiotherapy', 'Rest for 2 weeks, avoid heavy squats.', '2026-09-12 14:50:00'),
(4, 3, 'Healthy Pediatric Examination', 'Multivitamins pediatric drops', 'Growth percentiles normal (75th percentile).', '2026-09-15 11:40:00'),
(5, 5, 'Stage 1 Hypertension', 'Lisinopril 10mg daily', 'Follow up in 4 weeks with home BP log.', '2026-09-18 09:15:00');

-- 3.6. Insert Billing
INSERT INTO billing (patient_id, appointment_id, total_amount, payment_status, payment_method, billing_date) VALUES
(1, 1, 250.00, 'Paid', 'Credit Card', '2026-09-10 10:00:00'),
(2, 2, 180.00, 'Paid', 'Insurance', '2026-09-11 11:30:00'),
(3, 3, 320.00, 'Paid', 'Credit Card', '2026-09-12 15:10:00'),
(4, 4, 150.00, 'Paid', 'Cash', '2026-09-15 12:00:00'),
(5, 5, 200.00, 'Paid', 'Insurance', '2026-09-18 09:30:00');
