from flask import Flask, redirect, session, url_for
from .db import init_db
from .routes import register_routes

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_mapping(
        SECRET_KEY='supersecretkey',
        DATABASE='application.db'
    )

    app.jinja_env.filters['int'] = int

    with app.app_context():
        init_db(app)

    register_routes(app)

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('students.index'))
        return redirect(url_for('auth.login'))

    return app