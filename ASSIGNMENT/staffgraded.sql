CREATE DATABASE Assignment1;

USE Assignment1;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DepartmentID INT,
    InstructorID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    CourseID INT,
    Grade DECIMAL(4,2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- 2. Insert Data into Tables

INSERT INTO Departments (Name) VALUES 
('Computer Science'), ('Mathematics'), ('Physics'), ('Biology'), ('Chemistry'), ('English'), ('History'), ('Economics'), ('Psychology'), ('Engineering');

INSERT INTO Instructors (Name, DepartmentID) VALUES
('Dr. Smith', 1), ('Dr. Johnson', 2), ('Dr. Brown', 3), ('Dr. Wilson', 1), ('Dr. Adams', 4), ('Dr. Lee', 5), ('Dr. Martin', 6), ('Dr. White', 7), ('Dr. Harris', 8), ('Dr. Clark', 9);

INSERT INTO Students (Name, DateOfBirth, DepartmentID) VALUES
('Alice', '2002-05-15', 1), ('Bob', '2001-08-21', 2), ('Charlie', '2003-11-30', 3), ('David', '2002-02-10', 4), ('Emma', '2001-06-25', 5), ('Frank', '2000-09-12', 6), ('Grace', '2003-03-18', 7), ('Henry', '2002-07-08', 8), ('Ivy', '2001-04-29', 9), ('Jack', '2000-12-15', 10);

INSERT INTO Courses (Name, DepartmentID, InstructorID) VALUES
('Database Systems', 1, 1), ('Calculus', 2, 2), ('Quantum Mechanics', 3, 3), ('Genetics', 4, 5), ('Organic Chemistry', 5, 6), ('Shakespeare Studies', 6, 7), ('World History', 7, 8), ('Macroeconomics', 8, 9), ('Cognitive Psychology', 9, 10), ('Thermodynamics', 10, 1);

INSERT INTO Enrollments (StudentID, CourseID, Grade) VALUES
(1, 1, 85.5), (2, 2, 90.0), (3, 3, 88.0), (4, 4, 92.0), (5, 5, 89.5), (6, 6, 87.0), (7, 7, 91.0), (8, 8, 86.5), (9, 9, 93.0), (10, 10, 88.5),
(1, 2, 79.0), (2, 3, 82.5), (3, 4, 85.0), (4, 5, 78.5), (5, 6, 80.0), (6, 7, 83.5), (7, 8, 89.0), (8, 9, 92.5), (9, 10, 86.0), (10, 1, 90.0);

-- 3. SQL Queries

-- a) Update student data
UPDATE Students SET Name = 'Alice Johnson' WHERE StudentID = 1;

-- b) Fetch instructor details for a specific course
SELECT I.* FROM Instructors I
JOIN Courses C ON I.InstructorID = C.InstructorID
WHERE C.Name = 'Database Systems';

-- c) Total number of students across all courses in each department (including departments with zero students)
SELECT D.Name AS Department, COUNT(E.StudentID) AS TotalStudents
FROM Departments D
LEFT JOIN Courses C ON D.DepartmentID = C.DepartmentID
LEFT JOIN Enrollments E ON C.CourseID = E.CourseID
GROUP BY D.Name;

-- d) Identify instructors teaching more than 2 courses
SELECT I.Name, COUNT(C.CourseID) AS CoursesTaught
FROM Instructors I
JOIN Courses C ON I.InstructorID = C.InstructorID
GROUP BY I.Name
HAVING COUNT(C.CourseID) > 2;

-- e) Calculate the average grade per course
SELECT C.Name AS Course, AVG(E.Grade) AS AverageGrade
FROM Courses C
JOIN Enrollments E ON C.CourseID = E.CourseID
GROUP BY C.Name;

-- f) Procedure to find enrollment count in all courses
DELIMITER //
CREATE PROCEDURE GetEnrollmentCounts()
BEGIN
    SELECT C.Name AS Course, COUNT(E.StudentID) AS EnrollmentCount
    FROM Courses C
    LEFT JOIN Enrollments E ON C.CourseID = E.CourseID
    GROUP BY C.Name;
END //
DELIMITER;
