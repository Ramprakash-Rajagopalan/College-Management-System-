# College Management System

A comprehensive web-based college management system built with Flask and MySQL. This system provides an integrated platform for managing students, faculty, departments, courses, attendance, marks, and timetables.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [User Roles](#user-roles)
- [Features Overview](#features-overview)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- **User Authentication**: Secure login system with role-based access control
- **Student Management**: Add, edit, delete, and view student information
- **Faculty Management**: Manage faculty details and assignments
- **Department Management**: Organize and manage departments
- **Course Management**: Create and manage courses
- **Attendance Tracking**: Monitor student attendance
- **Marks Management**: Record and manage student marks/grades
- **Timetable Management**: Create and manage class schedules

### Role-Based Dashboards
- **Admin Dashboard**: Full system control and management
- **Student Dashboard**: View personal information, attendance, marks, and timetable
- **Faculty Dashboard**: View assigned courses, students, and manage marks

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MySQL
- **Authentication**: Session-based with SHA-256 password hashing

### Frontend
- **HTML5**: Page structure and templates
- **CSS3**: Styling (custom stylesheets)
- **JavaScript**: Client-side functionality

## 📁 Project Structure

```
College Management System/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Database configuration
│   ├── requirements.txt        # Python dependencies
│   ├── database/
│   │   └── schema.sql         # Database schema
│   ├── models/
│   │   └── student_model.py   # Data models
│   └── routes/
│       ├── api_routes.py      # API endpoints
│       └── student_routes.py  # Student-specific routes
├── templates/                  # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── admin_dashboard.html
│   ├── student_dashboard.html
│   ├── faculty_dashboard.html
│   ├── students.html
│   ├── faculty.html
│   ├── departments.html
│   ├── courses.html
│   ├── attendance.html
│   ├── marks.html
│   ├── timetable.html
│   └── add_student.html
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheet
│   └── js/
│       └── app.js             # Frontend JavaScript
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## 📋 Prerequisites

- Python 3.7 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/college-management-system.git
cd college-management-system
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup

### 1. Create Database

Open MySQL command line or MySQL Workbench and run:

```bash
mysql -u root -p
```

### 2. Execute Schema

```bash
# From the backend directory
mysql -u root -p college_management < database/schema.sql
```

Or manually copy and paste the content of `backend/database/schema.sql` into your MySQL client.

### 3. Verify Database Creation

```sql
USE college_management;
SHOW TABLES;
```

You should see the following tables:
- users
- students
- faculty
- departments
- courses
- attendance
- marks
- timetable

## ▶️ Running the Application

### 1. Navigate to Backend Directory

```bash
cd backend
```

### 2. Run Flask Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 3. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

##  User Roles

### 1. Admin
- Full system access
- Manage all students, faculty, and courses
- View all reports
- Configure system settings

### 2. Faculty
- View assigned courses
- Mark attendance for their courses
- Record and manage marks
- View faculty-specific dashboard

### 3. Student
- View personal information
- Check attendance records
- View marks and grades
- Access timetable and course information

## 🎯 Features Overview

### Student Management
- Add new students with enrollment details
- View student list with filtering options
- Edit student information
- Track student enrollment status
- Assign students to departments and years

### Faculty Management
- Manage faculty profiles
- Track faculty qualifications and experience
- Assign courses to faculty
- View faculty workload

### Department Management
- Create and manage departments
- Set department heads
- View department statistics

### Course Management
- Create new courses
- Assign courses to departments
- Manage course credits and prerequisites
- Track course enrollment

### Attendance System
- Mark daily attendance
- Generate attendance reports
- Track attendance trends

### Marks System
- Record student marks
- Manage multiple assessments
- Generate grade reports
- Calculate GPA

### Timetable Management
- Create class schedules
- Manage room assignments
- Publish timetables to students

## 📚 Database Schema

The system uses a relational database with the following main entities:

- **Users**: Authentication and authorization
- **Students**: Student information and enrollment
- **Faculty**: Faculty details and qualifications
- **Departments**: Department information
- **Courses**: Course details and structure
- **Attendance**: Attendance records
- **Marks**: Student assessment records
- **Timetable**: Class schedule information

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Security Notes

- ⚠️ **Important**: This is a development version. For production use:
  - Change the secret key in `app.py`
  - Update database credentials
  - Use environment variables for sensitive data
  - Enable HTTPS
  - Implement additional security measures
  - Use password hashing with salt
  - Add input validation and sanitization

## 🐛 Known Issues

- None currently reported

## 📞 Support

For support, email your-email@example.com or open an issue on GitHub.

## 👨‍💻 Author

[Your Name]
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your-email@example.com

---

**Last Updated**: May 2026

