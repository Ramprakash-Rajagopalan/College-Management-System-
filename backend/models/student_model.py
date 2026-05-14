import hashlib

class User:
    """User model for authentication"""
    
    def __init__(self, username, email, password, role, user_id=None):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = self.hash_password(password) if password else None
        self.role = role
    
    @staticmethod
    def hash_password(password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role
        }


class Student:
    """Student model"""
    
    def __init__(self, user_id, name, email, department, year, phone=None, student_id=None):
        self.id = student_id
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.year = year
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'year': self.year
        }


class Faculty:
    """Faculty model"""
    
    def __init__(self, user_id, name, email, department, phone=None, designation=None, qualification=None, faculty_id=None):
        self.id = faculty_id
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.designation = designation
        self.qualification = qualification
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'designation': self.designation,
            'qualification': self.qualification
        }


class Department:
    """Department model"""
    
    def __init__(self, name, code, head_id=None, dept_id=None):
        self.id = dept_id
        self.name = name
        self.code = code
        self.head_id = head_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'head_id': self.head_id
        }


class Course:
    """Course model"""
    
    def __init__(self, code, name, department_id, faculty_id, credits=None, semester=None, capacity=None, course_id=None):
        self.id = course_id
        self.code = code
        self.name = name
        self.department_id = department_id
        self.faculty_id = faculty_id
        self.credits = credits
        self.semester = semester
        self.capacity = capacity
    
    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'department_id': self.department_id,
            'faculty_id': self.faculty_id,
            'credits': self.credits,
            'semester': self.semester,
            'capacity': self.capacity
        }


class Attendance:
    """Attendance model"""
    
    def __init__(self, student_id, course_id, attendance_date, status, attendance_id=None):
        self.id = attendance_id
        self.student_id = student_id
        self.course_id = course_id
        self.attendance_date = attendance_date
        self.status = status
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'attendance_date': self.attendance_date,
            'status': self.status
        }


class Mark:
    """Marks/Results model"""
    
    def __init__(self, student_id, course_id, exam_type, marks_obtained, total_marks, grade=None, mark_id=None):
        self.id = mark_id
        self.student_id = student_id
        self.course_id = course_id
        self.exam_type = exam_type
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks
        self.percentage = (marks_obtained / total_marks * 100) if total_marks else 0
        self.grade = grade or self.calculate_grade()
    
    def calculate_grade(self):
        """Calculate grade based on percentage"""
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 50:
            return 'D'
        else:
            return 'F'
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'exam_type': self.exam_type,
            'marks_obtained': self.marks_obtained,
            'total_marks': self.total_marks,
            'percentage': round(self.percentage, 2),
            'grade': self.grade
        }


class Timetable:
    """Timetable model"""
    
    def __init__(self, course_id, day_of_week, start_time, end_time, room_number, faculty_id, timetable_id=None):
        self.id = timetable_id
        self.course_id = course_id
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.room_number = room_number
        self.faculty_id = faculty_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'day_of_week': self.day_of_week,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
            'room_number': self.room_number,
            'faculty_id': self.faculty_id
        }
