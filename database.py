import sqlite3

def create_database():
    conn = sqlite3.connect('application.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS genders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender VARCHAR(20) NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goal VARCHAR(100) NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS training_levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level VARCHAR(50) NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        salt VARCHAR(255) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        birth_date DATE NOT NULL CHECK(birth_date <= CURRENT_DATE),
        gender_id INTEGER NOT NULL,
        phone VARCHAR(15),
        email VARCHAR(100) UNIQUE,
        height DECIMAL(5, 2),
        weight DECIMAL(5, 2),
        goal_id INTEGER NOT NULL,
        medical_history TEXT,
        training_preference TEXT,
        level_id INTEGER NOT NULL,
        schedule TEXT,
        notes TEXT,
        photo_url VARCHAR(255),
        evaluation_photo_url VARCHAR(255),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(gender_id) REFERENCES genders(id),
        FOREIGN KEY(goal_id) REFERENCES goals(id),
        FOREIGN KEY(level_id) REFERENCES training_levels(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        student_id INTEGER NOT NULL,
        weight REAL CHECK(weight > 0) NOT NULL,
        height REAL CHECK(height > 0) NOT NULL,
        body_fat REAL CHECK(body_fat >= 0) NOT NULL,
        muscle_mass REAL,
        chest REAL,
        waist REAL,
        hip REAL,
        right_arm REAL,
        left_arm REAL,
        right_thigh REAL,
        left_thigh REAL,
        calf REAL,
        resting_hr INTEGER,
        cooper_test REAL,
        flexibility REAL,
        blood_pressure TEXT NOT NULL,
        sleep_quality REAL,
        stress_level INTEGER,
        training_feedback TEXT,
        new_goals TEXT,
        goal TEXT,
        notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        muscle_group VARCHAR(100),
        exercise_type VARCHAR(100) CHECK(exercise_type IN ('Strength', 'Cardio', 'Flexibility')) NOT NULL,
        subcategory VARCHAR(100),
        equipment VARCHAR(100) CHECK(equipment IN ('Dumbbell', 'Barbell', 'Rope', 'Machine')) NOT NULL,
        difficulty_level VARCHAR(50) CHECK(difficulty_level IN ('Easy', 'Medium', 'Hard')) NOT NULL,
        execution TEXT,
        video_link VARCHAR(255),
        benefits TEXT,
        goal TEXT,
        contraindications TEXT,
        variations TEXT,
        adaptations TEXT,
        injury_risk TEXT,
        notes TEXT,
        tags TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        date DATE NOT NULL,
        weight DECIMAL(5, 2),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS training (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        day TEXT NOT NULL,
        exercise_id INTEGER NOT NULL,
        repetitions INTEGER CHECK(repetitions > 0) NOT NULL,
        sets INTEGER CHECK(sets > 0) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
