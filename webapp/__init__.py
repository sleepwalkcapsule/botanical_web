import re
from webapp.db import db
from flask import Flask #, render_template, flash, redirect, url_for
from flask_login import LoginManager #, current_user, login_required
from webapp.admin.views import blueprint as admin_blueprint
from webapp.manuals.views import blueprint as manuals_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(manuals_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
