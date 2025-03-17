from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import get_db_connection

exercises_bp = Blueprint('exercises', __name__, url_prefix='/exercises')

@exercises_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['exercise-name']
        muscle_group = request.form['muscle-group']
        exercise_type = request.form['exercise-type']
        subcategory = request.form['subcategory']
        equipment = request.form['equipment']
        difficulty_level = request.form['difficulty-level']
        execution = request.form['execution']
        video_link = request.form['video-link']
        benefits = request.form['benefits']
        goal = request.form['goal']
        contraindications = request.form['contraindications']
        variations = request.form['variations']
        adaptations = request.form['adaptations']
        injury_risk = request.form['injury-risk']
        notes = request.form['notes']
        tags = request.form['tags']

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO exercises (name, muscle_group, exercise_type, subcategory, equipment, difficulty_level, execution, video_link, benefits, goal, contraindications, variations, adaptations, injury_risk, notes, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, muscle_group, exercise_type, subcategory, equipment, difficulty_level, execution, video_link, benefits, goal, contraindications, variations, adaptations, injury_risk, notes, tags))
            conn.commit()

        flash('Exercise registered successfully!')
        return redirect(url_for('exercises.exercise_list'))

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT muscle_group FROM exercises')
        muscle_groups = cursor.fetchall()
        cursor.execute('SELECT DISTINCT equipment FROM exercises')
        equipments = cursor.fetchall()
        cursor.execute('SELECT DISTINCT difficulty_level FROM exercises')
        difficulty_levels = cursor.fetchall()

    return render_template('forms/register_exercise.html', muscle_groups=muscle_groups, equipments=equipments, difficulty_levels=difficulty_levels)

@exercises_bp.route('/list')
def exercise_list():
    search_query = request.args.get('search')
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if search_query:
        cursor.execute('''
            SELECT * FROM exercises
            WHERE name LIKE ?
        ''', ('%' + search_query + '%',))
    else:
        cursor.execute('SELECT * FROM exercises')
    
    exercises = cursor.fetchall()
    conn.close()
    return render_template('dashboard/exercises.html', exercises=exercises, search_query=search_query)