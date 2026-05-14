from flask import Flask, request, jsonify, render_template, session, redirect
import pymysql
from config import DB_CONFIG
import os
from routes.api_routes import (
    auth_bp, student_bp, faculty_bp, dept_bp, 
    course_bp, attendance_bp, marks_bp, timetable_bp
)

# Set template and static folder paths
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = 'college_management_system_secret_key'

# Database connection
try:
    db = pymysql.connect(**DB_CONFIG)
except pymysql.Error as e:
    print(f"Database connection error: {e}")

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)
app.register_blueprint(faculty_bp)
app.register_blueprint(dept_bp)
app.register_blueprint(course_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(marks_bp)
app.register_blueprint(timetable_bp)


@app.route('/')
def home():
    return "College Management System - Comprehensive Edition Running Successfully"


# ==================== PAGE ROUTES ====================

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/login-page')
    
    user_role = session.get('role', 'student')
    
    # Route to appropriate dashboard based on role
    if user_role == 'admin':
        return render_template('admin_dashboard.html')
    elif user_role == 'faculty':
        return render_template('faculty_dashboard.html')
    else:  # student
        return render_template('student_dashboard.html')


@app.route('/login-page')
def login_page():
    return render_template('login.html')


@app.route('/students')
def students_page():
    return render_template('students.html')


@app.route('/faculty')
def faculty_page():
    return render_template('faculty.html')


@app.route('/departments')
def departments_page():
    return render_template('departments.html')


@app.route('/courses')
def courses_page():
    return render_template('courses.html')


@app.route('/attendance')
def attendance_page():
    return render_template('attendance.html')


@app.route('/marks')
def marks_page():
    return render_template('marks.html')


@app.route('/timetable')
def timetable_page():
    return render_template('timetable.html')


# Legacy routes (kept for backward compatibility)
@app.route('/home')
def homepage():
    return render_template('dashboard.html')


@app.route('/add-student-page')
def add_student_page():
    return render_template('add_student_modal.html')


@app.route('/students-page')
def students_list_page():
    return render_template('students.html')


if __name__ == '__main__':
    app.run(debug=True)