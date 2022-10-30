from flask import Blueprint, render_template #current_app,

from webapp.manuals.models import Manuals

blueprint = Blueprint('manuals', __name__)

@blueprint.route('/')
def index():
    title = "My botanical project"
    manuals_list = Manuals.query.all()
    return render_template('manuals/index.html', page_title=title, manuals_list=manuals_list)