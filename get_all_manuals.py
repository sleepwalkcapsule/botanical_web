from webapp import create_app
from webapp.botanical_org_news import get_manuals

app = create_app()
with app.app_context():
    get_manuals()
