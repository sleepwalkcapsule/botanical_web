import requests

from webapp.db import db 
from webapp.manuals.models import Manuals

def get_html(url):
    headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Error")
        return False

def save_manuals(title, url, published):
    manuals_exists = Manuals.query.filter(Manuals.url == url).count()
    print(manuals_exists)
    if not manuals_exists:
        manuals_manuals = Manuals(title=title, url=url, published=published)
        db.session.add(manuals_manuals)
        db.session.commit()