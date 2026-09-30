CREATE DATABASE DigiHealth_DB;
USE DigiHealth_DB;

CREATE TABLE Dim_Patient (
    Patient_Key INT AUTO_INCREMENT PRIMARY KEY,
    Patient_ID INT,
    Patient_Name VARCHAR(100),
    Gender VARCHAR(20),
    City VARCHAR(100)
);
INSERT INTO Dim_Patient
(Patient_ID, Patient_Name, Gender, City)
VALUES
(1,'Divya M','Female','Chennai'),
(2,'Priya S','Female','Bangalore');

CREATE TABLE Dim_Doctor (
    Doctor_Key INT AUTO_INCREMENT PRIMARY KEY,
    Doctor_ID INT,
    Doctor_Name VARCHAR(100),
    Specialization VARCHAR(100)
);
INSERT INTO Dim_Doctor
(Doctor_ID, Doctor_Name, Specialization)
VALUES
(1,'Sundar C','Cardiology'),
(2,'Prashant S','Dermatology');

CREATE TABLE Dim_Date (
    Date_Key INT AUTO_INCREMENT PRIMARY KEY,
    Full_Date DATE,
    Month_Name VARCHAR(20),
    Quarter_No INT,
    Year_No INT
);
INSERT INTO Dim_Date
(Full_Date, Month_Name, Quarter_No, Year_No)
VALUES
('2026-07-15','September',3,2026),
('2026-07-20','September',3,2026),
('2026-07-25','September',3,2026);

CREATE TABLE Dim_Payment (
    Payment_Key INT AUTO_INCREMENT PRIMARY KEY,
    Payment_Method VARCHAR(20),
    Payment_Status VARCHAR(20)
);
INSERT INTO Dim_Payment
(Payment_Method, Payment_Status)
VALUES
('Card','Paid'),
('UPI','Paid');

CREATE TABLE Fact_Appointment (
    Fact_ID INT AUTO_INCREMENT PRIMARY KEY,

    Patient_Key INT,
    Doctor_Key INT,
    Date_Key INT,
    Payment_Key INT,

    Treatment_Cost DECIMAL(10,2),
    Tax_Amount DECIMAL(10,2),
    Total_Amount DECIMAL(10,2),
    Appointment_Count INT DEFAULT 1,

    FOREIGN KEY (Patient_Key)
        REFERENCES Dim_Patient(Patient_Key),

    FOREIGN KEY (Doctor_Key)
        REFERENCES Dim_Doctor(Doctor_Key),

    FOREIGN KEY (Date_Key)
        REFERENCES Dim_Date(Date_Key),

    FOREIGN KEY (Payment_Key)
        REFERENCES Dim_Payment(Payment_Key)
);
INSERT INTO Fact_Appointment
(
Patient_Key,
Doctor_Key,
Date_Key,
Payment_Key,
Treatment_Cost,
Tax_Amount,
Total_Amount,
Appointment_Count
)
VALUES

(1,1,1,1,12000.00,300.00,12300.00,1),

(2,2,3,2,8000.00,200.00,8200.00,1);


