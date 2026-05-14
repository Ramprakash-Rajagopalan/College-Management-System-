CREATE DATABASE IF NOT EXISTS college_management;
USE college_management;

-- Users table for authentication
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'faculty', 'student') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    department VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    enrollment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Faculty table
CREATE TABLE IF NOT EXISTS faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    department VARCHAR(50) NOT NULL,
    designation VARCHAR(50),
    qualification VARCHAR(100),
    joining_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Departments table
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    head_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (head_id) REFERENCES faculty(id)
);

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    faculty_id INT NOT NULL,
    credits INT,
    semester INT,
    capacity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

-- Course Enrollment table
CREATE TABLE IF NOT EXISTS enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE,
    status ENUM('active', 'completed', 'dropped') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    UNIQUE KEY unique_enrollment (student_id, course_id)
);

-- Attendance table
CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('present', 'absent', 'leave') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Marks/Results table
CREATE TABLE IF NOT EXISTS marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    exam_type VARCHAR(50),
    marks_obtained DECIMAL(5,2),
    total_marks DECIMAL(5,2),
    percentage DECIMAL(5,2),
    grade VARCHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Timetable table
CREATE TABLE IF NOT EXISTS timetable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_number VARCHAR(20),
    faculty_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

-- Sample Data
-- Users (passwords are SHA256 hashed)
INSERT INTO users (username, email, password, role) VALUES
('admin', 'admin@college.edu', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'admin'),
('dr_smith', 'dr.smith@college.edu', '27041f5856c7387a997252694afb048d1aa939228ffcdbd6285b979b8da20e7a', 'faculty'),
('john_student', 'john.doe@college.edu', '703b0a3d6ad75b649a28adde7d83c6251da457549263bc7ff45ec709b0a8448b', 'student'),
('jane_student', 'jane.smith@college.edu', '703b0a3d6ad75b649a28adde7d83c6251da457549263bc7ff45ec709b0a8448b', 'student');

-- Departments
INSERT INTO departments (name, code) VALUES
('Computer Science', 'CS'),
('Business Administration', 'BA'),
('Mechanical Engineering', 'ME'),
('Electrical Engineering', 'EE');

-- Faculty
INSERT INTO faculty (user_id, name, email, phone, department, designation, qualification) VALUES
(2, 'Dr. Smith', 'dr.smith@college.edu', '9876543210', 'Computer Science', 'Professor', 'PhD');

-- Students
INSERT INTO students (user_id, name, email, phone, department, year, enrollment_date) VALUES
(3, 'John Doe', 'john.doe@college.edu', '9123456789', 'Computer Science', 1, '2024-08-15'),
(4, 'Jane Smith', 'jane.smith@college.edu', '9987654321', 'Business Administration', 2, '2023-08-20');

-- Courses
INSERT INTO courses (code, name, department_id, faculty_id, credits, semester, capacity) VALUES
('CS101', 'Introduction to Programming', 1, 1, 3, 1, 60),
('CS102', 'Data Structures', 1, 1, 3, 2, 60),
('BA101', 'Business Fundamentals', 2, 1, 3, 1, 50);

-- Enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, status) VALUES
(1, 1, '2024-08-15', 'active'),
(2, 3, '2023-08-20', 'active');

-- Attendance
INSERT INTO attendance (student_id, course_id, attendance_date, status) VALUES
(1, 1, '2024-09-01', 'present'),
(1, 1, '2024-09-02', 'present'),
(1, 1, '2024-09-03', 'absent');

-- Marks
INSERT INTO marks (student_id, course_id, exam_type, marks_obtained, total_marks, percentage, grade) VALUES
(1, 1, 'Mid-term', 35, 50, 70, 'B'),
(1, 1, 'Final', 75, 100, 75, 'B');

-- Timetable
INSERT INTO timetable (course_id, day_of_week, start_time, end_time, room_number, faculty_id) VALUES
(1, 'Monday', '09:00:00', '10:30:00', 'A101', 1),
(1, 'Wednesday', '09:00:00', '10:30:00', 'A101', 1),
(1, 'Friday', '09:00:00', '10:30:00', 'A101', 1);
