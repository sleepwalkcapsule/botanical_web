import re
from webapp.botanical_org_news import get_manuals
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    #app.config.from_pyfile('config.py') Конфигурационный файл (юзать для скрытия API)

    @app.route('/')
    def index():
        title = "My botanical project"
        manuals_list = get_manuals()
        return render_template('index.html', page_title=title, manuals_list=manuals_list)

    return app