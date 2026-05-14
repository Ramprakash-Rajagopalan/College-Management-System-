# 🎓 College Management System - Comprehensive Edition

A comprehensive web-based application for managing all aspects of college operations including students, faculty, courses, departments, attendance, marks, timetables, and authentication with user roles.

## 📋 Features

### Core Features
- ✅ **Authentication & User Roles** - Admin, Faculty, and Student accounts with login system
- ✅ **Student Management** - Add, view, edit, and manage student records
- ✅ **Faculty Management** - Manage faculty members and their details
- ✅ **Department Management** - Organize and manage academic departments
- ✅ **Course Management** - Create and manage courses with faculty assignments
- ✅ **Attendance Tracking** - Record and track student attendance per course
- ✅ **Marks & Results** - Manage exam marks with automatic grade calculation
- ✅ **Timetable Management** - Create and view class timetables by day
- ✅ **Dashboard** - Comprehensive overview with statistics
- ✅ **Responsive Design** - Works on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RESTful JSON API with multiple endpoints

## 📁 Project Structure

```
College Management System/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── config.py                 # Database configuration
│   ├── requirements.txt           # Python dependencies
│   ├── database/
│   │   └── schema.sql            # Complete database schema
│   ├── models/
│   │   └── student_model.py      # All data models (User, Student, Faculty, etc.)
│   └── routes/
│       ├── student_routes.py     # Legacy routes
│       └── api_routes.py         # Comprehensive API blueprints
├── static/
│   └── css/
│       ├── style.css             # Main styling
│       └── js/
│           └── app.js            # Frontend JavaScript
├── templates/
│   ├── login.html                # Authentication page
│   ├── dashboard.html            # Main dashboard
│   ├── students.html             # Student management
│   ├── faculty.html              # Faculty management
│   ├── departments.html          # Department management
│   ├── courses.html              # Course management
│   ├── attendance.html           # Attendance tracking
│   ├── marks.html                # Marks & results
│   ├── timetable.html            # Class timetable
│   └── (legacy pages)
└── readme.md                      # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- MySQL Server
- pip (Python package manager)

### Step 1: Navigate to Project
```bash
cd "College Management System/New file"
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Mac/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### Step 4: Setup Database
1. Open MySQL terminal or MySQL Workbench
2. Create the database and tables:
```sql
SOURCE backend/database/schema.sql;
```

### Step 5: Configure Database
Edit `backend/config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',        # Your MySQL username
    'password': '282004',  # Your MySQL password
    'database': 'college_management'
}
```

### Step 6: Run Application
```bash
cd backend
python app.py
```

The application will be available at: **http://localhost:5000**

## 🔐 Authentication

### Demo Accounts
- **Admin**: username: `admin`, password: `admin123`
- **Faculty**: username: `dr_smith`, password: `faculty123`
- **Student**: username: `john_student`, password: `student123`

Access the login page: http://localhost:5000/login-page

## 📊 Database Schema

### Users Table
- id, username, email, password, role (admin/faculty/student)

### Students Table
- id, user_id, name, email, phone, department, year, enrollment_date

### Faculty Table
- id, user_id, name, email, phone, department, designation, qualification

### Departments Table
- id, name, code, head_id

### Courses Table
- id, code, name, department_id, faculty_id, credits, semester, capacity

### Enrollments Table
- id, student_id, course_id, enrollment_date, status

### Attendance Table
- id, student_id, course_id, attendance_date, status (present/absent/leave)

### Marks Table
- id, student_id, course_id, exam_type, marks_obtained, total_marks, percentage, grade

### Timetable Table
- id, course_id, day_of_week, start_time, end_time, room_number, faculty_id

## 📡 API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Students
- `GET /api/students` - Get all students
- `POST /api/students` - Create student
- `GET /api/students/<id>` - Get student details

### Faculty
- `GET /api/faculty` - Get all faculty
- `POST /api/faculty` - Create faculty member

### Departments
- `GET /api/departments` - Get all departments
- `POST /api/departments` - Create department

### Courses
- `GET /api/courses` - Get all courses
- `POST /api/courses` - Create course

### Attendance
- `GET /api/attendance` - Get attendance records
- `POST /api/attendance` - Mark attendance

### Marks
- `GET /api/marks` - Get marks records
- `POST /api/marks` - Record marks

### Timetable
- `GET /api/timetable` - Get timetable
- `POST /api/timetable` - Create timetable entry

## 🖥️ Web Pages

| Page | URL | Description |
|------|-----|-------------|
| Login | `/login-page` | User authentication |
| Dashboard | `/dashboard` | Main overview & statistics |
| Students | `/students` | Manage student records |
| Faculty | `/faculty` | Manage faculty members |
| Departments | `/departments` | Manage departments |
| Courses | `/courses` | Manage courses |
| Attendance | `/attendance` | Track attendance |
| Marks | `/marks` | Manage exam results |
| Timetable | `/timetable` | View class schedule |

## 🎨 Features Breakdown

### 1. Authentication System
- User login with role-based access
- Secure password hashing (SHA-256)
- Session management

### 2. Student Management
- Add new students
- View all student records
- Edit student information
- Delete student records
- Track student by department and year

### 3. Faculty Management
- Maintain faculty member records
- Track qualifications and designations
- Assign faculty to courses

### 4. Department Organization
- Create and manage departments
- Assign department heads
- Organize courses by department

### 5. Course Management
- Create courses with codes
- Assign faculty to courses
- Set capacity and credits
- Organize by semester

### 6. Attendance System
- Mark daily attendance
- Track by student and course
- Mark as present, absent, or leave

### 7. Marks & Results
- Record exam marks
- Automatic percentage calculation
- Automatic grade assignment (A+, A, B, C, D, F)
- Track multiple exam types

### 8. Timetable
- Create class schedules
- View by day of week
- Display room numbers and timings
- Show assigned faculty

## 🐛 Troubleshooting

### Database Connection Error
```
Error: Database connection error
```
**Solution**: Check MySQL credentials in `backend/config.py`

### Module Not Found
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Reinstall dependencies
```bash
pip install -r backend/requirements.txt
```

### Port Already in Use
```
Address already in use
```
**Solution**: Change port in app.py
```python
app.run(debug=True, port=5001)
```

### Template Not Found
```
TemplateNotFound: dashboard.html
```
**Solution**: Ensure templates folder is in correct location

## 🔒 Security Notes

- Passwords are hashed using SHA-256
- Use environment variables for production
- Implement JWT tokens for production use
- Add CSRF protection for production
- Use HTTPS in production
- Implement role-based access control properly

## 📈 Sample Data

The database comes pre-populated with:
- 1 Admin user
- 1 Faculty member (Dr. Smith)
- 2 Student users
- 4 Departments
- 3 Courses
- Sample attendance records
- Sample marks records
- Sample timetable entries

## 🚀 Deployment

For production deployment:
1. Use a production WSGI server (Gunicorn)
2. Set `debug=False` in app.py
3. Use environment variables for credentials
4. Implement proper logging
5. Add request validation and sanitization
6. Use database connection pooling

## 📚 API Examples

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

### Get All Students
```bash
curl http://localhost:5000/api/students
```

### Add Attendance
```bash
curl -X POST http://localhost:5000/api/attendance \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 1,
    "course_id": 1,
    "attendance_date": "2024-09-05",
    "status": "present"
  }'
```

### Record Marks
```bash
curl -X POST http://localhost:5000/api/marks \
  -H "Content-Type: application/json" \
  -d '{
    "student_id": 1,
    "course_id": 1,
    "exam_type": "Final",
    "marks_obtained": 85,
    "total_marks": 100
  }'
```

## 📄 License

This project is provided for educational purposes.

## 👨‍💻 Contributors

Created as a comprehensive college management system.

## 🤝 Support

For issues or questions, please check the troubleshooting section or review the code comments.

---

**Last Updated**: May 2026
**Version**: 2.0.0 - Comprehensive Edition
**Status**: ✅ Fully Functional with All Features

