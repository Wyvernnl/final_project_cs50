from flask import Blueprint, render_template, request, flash, url_for, redirect
from ..db import get_db_connection

assessments_bp = Blueprint('assessments', __name__, url_prefix='/assessments')

@assessments_bp.route('/')
def assessment():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM students')
        students = cursor.fetchall()
    return render_template('forms/assessment.html', students=students)

@assessments_bp.route('/submit', methods=['POST'])
def submit_evaluation():
    student_id = request.form.get('student')
    date = request.form.get('date')
    weight = request.form.get('weight')
    height = request.form.get('height')
    body_fat = request.form.get('body-fat')
    muscle_mass = request.form.get('muscle-mass')
    chest = request.form.get('chest')
    waist = request.form.get('waist')
    hip = request.form.get('hip')
    right_arm = request.form.get('right-arm')
    left_arm = request.form.get('left-arm')
    right_thigh = request.form.get('right-thigh')
    left_thigh = request.form.get('left-thigh')
    calf = request.form.get('calf')
    rest_hr = request.form.get('rest-hr')
    test_cooper = request.form.get('test-cooper')
    flexibility = request.form.get('flexibility')
    blood_pressure = request.form.get('blood-pressure')
    sleep_quality = request.form.get('sleep-quality')
    stress_level = request.form.get('stress-level')
    training_feedback = request.form.get('training-feedback')
    goal = request.form.get('goals')

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO assessments (
                student_id, date, weight, height, body_fat, muscle_mass, chest, waist, hip, 
                right_arm, left_arm, right_thigh, left_thigh, calf, resting_hr, cooper_test, 
                flexibility, blood_pressure, sleep_quality, stress_level, training_feedback, goal
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            student_id, date, weight, height, body_fat, muscle_mass, chest, waist, hip, 
            right_arm, left_arm, right_thigh, left_thigh, calf, rest_hr, test_cooper, 
            flexibility, blood_pressure, sleep_quality, stress_level, training_feedback, goal
        ))
        conn.commit()

    flash('Assessment submitted successfully!')
    return redirect(url_for('assessments.assessment'))