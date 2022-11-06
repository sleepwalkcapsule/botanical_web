from datetime import datetime

# from cgitb import html, text
# from itertools import count
# from turtle import title
# from unittest import result
from bs4 import BeautifulSoup
from webapp.db import db
from webapp.manuals.models import Manuals
import requests

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Error")
        return False

def get_manuals():
    html = get_html("https://en.wikipedia.org/wiki/Outline_of_botany")
    if html:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            all_manuals = soup.findAll('li')
            result_manuals = []
            base_url = "https://en.wikipedia.org"
            for manuals in all_manuals:
                item = manuals.find('a')
                title = item.text
                relative_url = item['href']
                url = f'{base_url}{relative_url}'
                published = manuals.find('li', class_='footer-info-lastmod').text
                try:
                    published = datetime.strptime(published, '%Y-%m-%d')
                except ValueError:
                    published = datetime.now()
                save_manuals(title, url, published)
                print(published)
        except AttributeError:
            print(AttributeError)
        
def save_manuals(title, url, published):
    manuals_exists = Manuals.query.filter(Manuals.url == url).count()
    print(manuals_exists)
    if not manuals_exists:
        manuals_manuals = Manuals(title=title, url=url, published=published)
        db.session.add(manuals_manuals)
        db.session.commit()
