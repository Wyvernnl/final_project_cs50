from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..db import get_db_connection

training_bp = Blueprint('training', __name__)

@training_bp.route('/register/training', methods=['GET', 'POST'])
def register_training():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM students')
        students = cursor.fetchall()
        cursor.execute('SELECT id, name FROM exercises')
        exercises = cursor.fetchall()

    students = [dict(id=row['id'], name=row['name']) for row in students]
    exercises = [dict(id=row['id'], name=row['name']) for row in exercises]

    if request.method == 'POST':
        student_id = request.form['student']

        if not student_id:
            flash('Selecione um aluno.')
            return redirect(url_for('training.register_training'))

        with get_db_connection() as conn:
            cursor = conn.cursor()
            for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                exercises = request.form.getlist(f'{day}Exercise')
                repetitions = request.form.getlist(f'{day}Repetitions')
                sets = request.form.getlist(f'{day}Sets')
                for exercise, repetition, set_ in zip(exercises, repetitions, sets):
                    if exercise == 'rest':
                        repetition = None
                        set_ = None
                    cursor.execute('''
                        INSERT INTO training (student_id, day, exercise_id, repetitions, sets)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (student_id, day, exercise, repetition, set_))
            conn.commit()
        flash('Treino cadastrado com sucesso!')
        return redirect(url_for('training.register_training'))

    return render_template('forms/register_training.html', students=students, exercises=exercises)