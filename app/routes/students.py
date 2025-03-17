from flask import Blueprint, render_template, request, flash, abort, redirect, url_for
from ..db import get_db_connection

students_bp = Blueprint('students', __name__)

def execute_query(query, params=()):
    with get_db_connection() as conn:
        result = conn.execute(query, params)
        rows = result.fetchall()
    return rows

def execute_insert(query, params=()):
    with get_db_connection() as conn:
        conn.execute(query, params)
        conn.commit()

@students_bp.route('/index', methods=['GET'])
def index():
    search_query = request.args.get('search')
    if search_query:
        students = execute_query('''
            SELECT students.id, students.name, genders.gender AS gender, students.phone, 
                   (SELECT MAX(date) FROM assessments WHERE assessments.student_id = students.id) AS data_ultima_avaliacao,
                   (SELECT COUNT(*) FROM training WHERE training.student_id = students.id) AS treinos_cadastrados
            FROM students
            JOIN genders ON students.gender_id = genders.id
            WHERE students.name LIKE ?
        ''', ('%' + search_query + '%',))
    else:
        students = execute_query('''
            SELECT students.id, students.name, genders.gender AS gender, students.phone, 
                   (SELECT MAX(date) FROM assessments WHERE assessments.student_id = students.id) AS data_ultima_avaliacao,
                   (SELECT COUNT(*) FROM training WHERE training.student_id = students.id) AS treinos_cadastrados
            FROM students
            JOIN genders ON students.gender_id = genders.id
        ''')
    
    return render_template('index.html', students=students, search_query=search_query)

@students_bp.route('/register', methods=['GET', 'POST'])
def Student_registration():
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        gender_id = request.form['gender']
        phone = request.form['phone']
        email = request.form['email']
        height = request.form['height']
        weight = request.form['weight']
        goal_id = request.form['objective']
        medical_history = request.form['medical_history']
        training_preference = request.form['training_preference']
        level_id = request.form['nivel']
        schedule = request.form['time']
        notes = request.form['notes']
        photo_url = request.form.get('photo_url', None)
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                photo_url = f'static/uploads/{photo.filename}'
                photo.save(photo_url)
            else:
                photo_url = None
        else:
            photo_url = None
                    
        existing_student = execute_query('SELECT id FROM students WHERE email = ?', (email,))
        if existing_student:
            flash('Email already registered!', 'error')
        else:
            execute_insert('''
                INSERT INTO students (name, birth_date, gender_id, phone, email, height, weight, goal_id, medical_history, training_preference, level_id, schedule, notes, photo_url )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, birth_date, gender_id, phone, email, height, weight, goal_id, medical_history, training_preference, level_id, schedule, notes, photo_url))
            flash('Student registered successfully!')

    genders = execute_query('SELECT id, gender FROM genders')
    goals = execute_query('SELECT id, goal FROM goals')
    level = execute_query('SELECT id, level FROM training_levels')
    
    return render_template('forms/register_student.html', gender=genders, goal=goals, level=level)

@students_bp.route('/profile/<int:student_id>')
def profile(student_id):
    student = execute_query('''
        SELECT students.*, genders.gender, goals.goal
        FROM students
        JOIN genders ON students.gender_id = genders.id
        JOIN goals ON students.goal_id = goals.id
        WHERE students.id = ?
    ''', (student_id,))
    if not student:
        abort(404)
    
    training = execute_query('''
        SELECT exercises.name, training.day, training.repetitions, training.sets
        FROM training
        JOIN exercises ON training.exercise_id = exercises.id
        WHERE training.student_id = ?
    ''', (student_id,))
    
    evaluations = execute_query('''
        SELECT date, weight, height, goal, notes
        FROM assessments
        WHERE student_id = ?
    ''', (student_id,))
    
    return render_template('dashboard/student_profile.html', student=student, training=training, evaluations=evaluations)