from flask import Blueprint, request, jsonify, session
import pymysql
from config import DB_CONFIG
from models.student_model import User, Student, Faculty, Department, Course, Attendance, Mark, Timetable
import hashlib

# Create blueprints for different modules
auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
student_bp = Blueprint('students', __name__, url_prefix='/api/students')
faculty_bp = Blueprint('faculty', __name__, url_prefix='/api/faculty')
dept_bp = Blueprint('departments', __name__, url_prefix='/api/departments')
course_bp = Blueprint('courses', __name__, url_prefix='/api/courses')
attendance_bp = Blueprint('attendance', __name__, url_prefix='/api/attendance')
marks_bp = Blueprint('marks', __name__, url_prefix='/api/marks')
timetable_bp = Blueprint('timetable', __name__, url_prefix='/api/timetable')

def get_db_connection():
    """Create database connection"""
    try:
        return pymysql.connect(**DB_CONFIG)
    except pymysql.Error as e:
        raise Exception(f"Database connection error: {e}")

# ==================== AUTHENTICATION ====================

@auth_bp.route('/login', methods=['POST'])
def login():
    """User login"""
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT id, username, email, role FROM users WHERE username = %s AND password = %s", 
                      (username, hashed_password))
        
        user = cursor.fetchone()
        cursor.close()
        db.close()
        
        if not user:
            return jsonify({"error": "Invalid credentials"}), 401
        
        session['user_id'] = user[0]
        session['username'] = user[1]
        session['role'] = user[3]
        
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "role": user[3]
            }
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """User logout"""
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

# ==================== STUDENTS ====================

@student_bp.route('', methods=['GET'])
def get_all_students():
    """Get all students"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT s.id, s.user_id, s.name, s.email, s.phone, s.department, s.year
            FROM students s
        """)
        
        students = cursor.fetchall()
        cursor.close()
        db.close()
        
        student_list = [
            {
                "id": s[0],
                "user_id": s[1],
                "name": s[2],
                "email": s[3],
                "phone": s[4],
                "department": s[5],
                "year": s[6]
            }
            for s in students
        ]
        
        return jsonify(student_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_bp.route('', methods=['POST'])
def create_student():
    """Create new student"""
    try:
        data = request.json
        required_fields = ['user_id', 'name', 'email', 'department', 'year']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO students(user_id, name, email, phone, department, year)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (
            data['user_id'], data['name'], data['email'],
            data.get('phone'), data['department'], data['year']
        ))
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Student created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student by ID"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT s.id, s.user_id, s.name, s.email, s.phone, s.department, s.year
            FROM students s WHERE s.id = %s
        """, (student_id,))
        
        student = cursor.fetchone()
        cursor.close()
        db.close()
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        return jsonify({
            "id": student[0],
            "user_id": student[1],
            "name": student[2],
            "email": student[3],
            "phone": student[4],
            "department": student[5],
            "year": student[6]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== FACULTY ====================

@faculty_bp.route('', methods=['GET'])
def get_all_faculty():
    """Get all faculty members"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT f.id, f.user_id, f.name, f.email, f.phone, f.department, f.designation, f.qualification
            FROM faculty f
        """)
        
        faculty_list = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": f[0],
                "user_id": f[1],
                "name": f[2],
                "email": f[3],
                "phone": f[4],
                "department": f[5],
                "designation": f[6],
                "qualification": f[7]
            }
            for f in faculty_list
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@faculty_bp.route('', methods=['POST'])
def create_faculty():
    """Create new faculty"""
    try:
        data = request.json
        required_fields = ['user_id', 'name', 'email', 'department']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO faculty(user_id, name, email, phone, department, designation, qualification)
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (
            data['user_id'], data['name'], data['email'],
            data.get('phone'), data['department'],
            data.get('designation'), data.get('qualification')
        ))
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Faculty created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== DEPARTMENTS ====================

@dept_bp.route('', methods=['GET'])
def get_all_departments():
    """Get all departments"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT id, name, code, head_id FROM departments
        """)
        
        depts = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": d[0],
                "name": d[1],
                "code": d[2],
                "head_id": d[3]
            }
            for d in depts
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@dept_bp.route('', methods=['POST'])
def create_department():
    """Create new department"""
    try:
        data = request.json
        
        if not data or not data.get('name') or not data.get('code'):
            return jsonify({"error": "Name and code required"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        cursor.execute("""
            INSERT INTO departments(name, code, head_id)
            VALUES(%s, %s, %s)
        """, (data['name'], data['code'], data.get('head_id')))
        
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Department created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== COURSES ====================

@course_bp.route('', methods=['GET'])
def get_all_courses():
    """Get all courses"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT id, code, name, department_id, faculty_id, credits, semester, capacity
            FROM courses
        """)
        
        courses = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": c[0],
                "code": c[1],
                "name": c[2],
                "department_id": c[3],
                "faculty_id": c[4],
                "credits": c[5],
                "semester": c[6],
                "capacity": c[7]
            }
            for c in courses
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== ATTENDANCE ====================

@attendance_bp.route('', methods=['GET'])
def get_attendance():
    """Get attendance records"""
    try:
        student_id = request.args.get('student_id')
        course_id = request.args.get('course_id')
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = "SELECT id, student_id, course_id, attendance_date, status FROM attendance WHERE 1=1"
        params = []
        
        if student_id:
            query += " AND student_id = %s"
            params.append(student_id)
        if course_id:
            query += " AND course_id = %s"
            params.append(course_id)
        
        cursor.execute(query, params)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": r[0],
                "student_id": r[1],
                "course_id": r[2],
                "attendance_date": str(r[3]),
                "status": r[4]
            }
            for r in records
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@attendance_bp.route('', methods=['POST'])
def create_attendance():
    """Create attendance record"""
    try:
        data = request.json
        required_fields = ['student_id', 'course_id', 'attendance_date', 'status']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        cursor.execute("""
            INSERT INTO attendance(student_id, course_id, attendance_date, status)
            VALUES(%s, %s, %s, %s)
        """, (data['student_id'], data['course_id'], data['attendance_date'], data['status']))
        
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Attendance recorded successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== MARKS ====================

@marks_bp.route('', methods=['GET'])
def get_marks():
    """Get marks/results"""
    try:
        student_id = request.args.get('student_id')
        course_id = request.args.get('course_id')
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = """
            SELECT id, student_id, course_id, exam_type, marks_obtained, 
                   total_marks, percentage, grade FROM marks WHERE 1=1
        """
        params = []
        
        if student_id:
            query += " AND student_id = %s"
            params.append(student_id)
        if course_id:
            query += " AND course_id = %s"
            params.append(course_id)
        
        cursor.execute(query, params)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": r[0],
                "student_id": r[1],
                "course_id": r[2],
                "exam_type": r[3],
                "marks_obtained": float(r[4]),
                "total_marks": float(r[5]),
                "percentage": float(r[6]),
                "grade": r[7]
            }
            for r in records
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@marks_bp.route('', methods=['POST'])
def create_marks():
    """Create marks/results"""
    try:
        data = request.json
        required_fields = ['student_id', 'course_id', 'exam_type', 'marks_obtained', 'total_marks']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        # Calculate percentage and grade
        percentage = (float(data['marks_obtained']) / float(data['total_marks']) * 100)
        
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'
        
        cursor.execute("""
            INSERT INTO marks(student_id, course_id, exam_type, marks_obtained, total_marks, percentage, grade)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
        """, (
            data['student_id'], data['course_id'], data['exam_type'],
            data['marks_obtained'], data['total_marks'], percentage, grade
        ))
        
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Marks recorded successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ==================== TIMETABLE ====================

@timetable_bp.route('', methods=['GET'])
def get_timetable():
    """Get timetable"""
    try:
        course_id = request.args.get('course_id')
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = "SELECT id, course_id, day_of_week, start_time, end_time, room_number, faculty_id FROM timetable WHERE 1=1"
        params = []
        
        if course_id:
            query += " AND course_id = %s"
            params.append(course_id)
        
        query += " ORDER BY day_of_week, start_time"
        
        cursor.execute(query, params)
        records = cursor.fetchall()
        cursor.close()
        db.close()
        
        return jsonify([
            {
                "id": r[0],
                "course_id": r[1],
                "day_of_week": r[2],
                "start_time": str(r[3]),
                "end_time": str(r[4]),
                "room_number": r[5],
                "faculty_id": r[6]
            }
            for r in records
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@timetable_bp.route('', methods=['POST'])
def create_timetable():
    """Create timetable entry"""
    try:
        data = request.json
        required_fields = ['course_id', 'day_of_week', 'start_time', 'end_time', 'room_number', 'faculty_id']
        
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        cursor.execute("""
            INSERT INTO timetable(course_id, day_of_week, start_time, end_time, room_number, faculty_id)
            VALUES(%s, %s, %s, %s, %s, %s)
        """, (
            data['course_id'], data['day_of_week'], data['start_time'],
            data['end_time'], data['room_number'], data['faculty_id']
        ))
        
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Timetable entry created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
