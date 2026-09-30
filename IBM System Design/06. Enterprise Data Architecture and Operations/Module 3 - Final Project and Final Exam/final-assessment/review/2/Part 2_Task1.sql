CREATE DATABASE DigiHealth;
USE DigiHealth;

CREATE TABLE Patient (
    Patient_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Date_Of_Birth DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Phone_Number VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Address VARCHAR(255)
);
INSERT INTO Patient
(First_Name, Last_Name, Date_Of_Birth, Gender, Phone_Number, Email, Address)
VALUES
('Divya', 'M', '1980-05-15', 'Female', '9876543210',
 'divya@gmail.com', 'Chennai'),

('Priya', 'S', '2000-08-20', 'Female', '9988776655',
 'priya@gmail.com', 'Bangalore');

CREATE TABLE Doctor (
    Doctor_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    License_Number VARCHAR(50) UNIQUE NOT NULL
);
INSERT INTO Doctor
(First_Name, Last_Name, Specialization, Phone_Number, Email, License_Number)
VALUES
('Sundar', 'M', 'Cardiology', '9001122334',
 'sundar.cardio@hospital.com', 'DOC1001'),

('Prashant', 'S', 'Dermatology', '9112233445',
 'prashant.derma@hospital.com', 'DOC1002');

CREATE TABLE Patient_Doctor (
    Patient_Doctor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Doctor_ID INT NOT NULL,
    Start_Date DATE,
    End_Date DATE,

    CONSTRAINT fk_pd_patient
        FOREIGN KEY (Patient_ID)
        REFERENCES Patient(Patient_ID)
        ON DELETE CASCADE,

    CONSTRAINT fk_pd_doctor
        FOREIGN KEY (Doctor_ID)
        REFERENCES Doctor(Doctor_ID)
        ON DELETE CASCADE
);
INSERT INTO Patient_Doctor
(Patient_ID, Doctor_ID, Start_Date)
VALUES
(1, 1, '2026-01-01'),
(1, 2, '2026-02-01'),
(2, 2, '2026-03-01');

CREATE TABLE Appointment (
    Appointment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Doctor_ID INT NOT NULL,
    Appointment_Date DATETIME NOT NULL,
    Appointment_Status ENUM('Scheduled','Completed','Cancelled')
        DEFAULT 'Scheduled',
    Reason_For_Visit VARCHAR(255),

    CONSTRAINT fk_appointment_patient
        FOREIGN KEY (Patient_ID)
        REFERENCES Patient(Patient_ID),

    CONSTRAINT fk_appointment_doctor
        FOREIGN KEY (Doctor_ID)
        REFERENCES Doctor(Doctor_ID)
);
INSERT INTO Appointment
(Patient_ID, Doctor_ID, Appointment_Date,
 Appointment_Status, Reason_For_Visit)
VALUES
(1, 1, '2026-07-15 10:00:00',
 'Completed', 'Heart Checkup'),

(1, 2, '2026-07-20 14:00:00',
 'Scheduled', 'Skin Allergy'),

(2, 2, '2026-07-25 11:00:00',
 'Completed', 'Routine Consultation');

CREATE TABLE Medical_Record (
    Record_ID INT AUTO_INCREMENT PRIMARY KEY,
    Patient_ID INT UNIQUE NOT NULL,
    Diagnosis TEXT,
    Prescription TEXT,
    Allergies TEXT,
    Medical_History TEXT,
    Last_Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_medical_patient
        FOREIGN KEY (Patient_ID)
        REFERENCES Patient(Patient_ID)
);
INSERT INTO Medical_Record
(Patient_ID, Diagnosis, Prescription,
 Allergies, Medical_History)
VALUES
(1,
 'Hypertension',
 'Amlodipine 5mg',
 'Penicillin',
 'High BP since 2022'),

(2,
 'Skin Allergy',
 'Antihistamines',
 'None',
 'No chronic illness');

CREATE TABLE Billing (
    Bill_ID INT AUTO_INCREMENT PRIMARY KEY,
    Appointment_ID INT UNIQUE NOT NULL,
    Treatment_Cost DECIMAL(10,2) NOT NULL,
    Tax_Amount DECIMAL(10,2) DEFAULT 0.00,
    Total_Amount DECIMAL(10,2) NOT NULL,
    Payment_Method ENUM('Cash','Card','UPI','Online'),
    Payment_Status ENUM('Paid','Pending','Failed')
        DEFAULT 'Pending',

    CONSTRAINT fk_billing_appointment
        FOREIGN KEY (Appointment_ID)
        REFERENCES Appointment(Appointment_ID)
);
INSERT INTO Billing
(Appointment_ID, Treatment_Cost,
 Tax_Amount, Total_Amount,
 Payment_Method, Payment_Status)
VALUES
(1, 12000.00, 300.00, 12300.00,
 'Card', 'Paid'),

(3, 8000.00, 200.00, 8200.00,
 'UPI', 'Paid');
