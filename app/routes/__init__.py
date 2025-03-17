from .auth import auth_bp
from .students import students_bp
from .exercises import exercises_bp
from .assessments import assessments_bp
from .register_training import training_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(exercises_bp)
    app.register_blueprint(assessments_bp)
    app.register_blueprint(training_bp)