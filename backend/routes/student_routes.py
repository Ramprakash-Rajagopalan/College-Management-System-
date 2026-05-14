from flask import Blueprint, request, jsonify
import pymysql
from config import DB_CONFIG

student_bp = Blueprint('students', __name__, url_prefix='/api')

def get_db_connection():
    """Create database connection"""
    try:
        return pymysql.connect(**DB_CONFIG)
    except pymysql.Error as e:
        raise Exception(f"Database connection error: {e}")

@student_bp.route('/students', methods=['GET'])
def get_all_students():
    """Get all students"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        db.close()

        student_list = []
        for student in students:
            student_list.append({
                "id": student[0],
                "name": student[1],
                "email": student[2],
                "department": student[3],
                "year": student[4]
            })
        
        return jsonify(student_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@student_bp.route('/students', methods=['POST'])
def create_student():
    """Create a new student"""
    try:
        data = request.json
        
        required_fields = ['name', 'email', 'department', 'year']
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO students(name, email, department, year)
        VALUES(%s,%s,%s,%s)
        """
        
        cursor.execute(query, (data['name'], data['email'], data['department'], data['year']))
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Student Added Successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get student by ID"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        cursor.close()
        db.close()
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        return jsonify({
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "department": student[3],
            "year": student[4]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update student by ID"""
    try:
        data = request.json
        
        db = get_db_connection()
        cursor = db.cursor()
        
        query = """
        UPDATE students 
        SET name=%s, email=%s, department=%s, year=%s
        WHERE id=%s
        """
        
        cursor.execute(query, (
            data.get('name'),
            data.get('email'),
            data.get('department'),
            data.get('year'),
            student_id
        ))
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Student Updated Successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete student by ID"""
    try:
        db = get_db_connection()
        cursor = db.cursor()
        
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Student Deleted Successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
