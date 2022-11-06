from webapp import create_app
# from webapp.botanical_org_news import get_manuals
from webapp.manuals.parsers import habr_plant


app = create_app()
with app.app_context():
    # get_manuals()
    habr_plant.get_habr_snippets()
