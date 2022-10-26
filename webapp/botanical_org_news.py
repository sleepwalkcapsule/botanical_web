# from datetime import datetime

from cgitb import html, text
# from turtle import title
from unittest import result
from bs4 import BeautifulSoup
from webapp.model import db, Manuals
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
            # print(all_manuals)
            base_url = "https://en.wikipedia.org"
            for manuals in all_manuals:
                # title = manuals.find('a')
                item = manuals.find('a')
                title = item.text
                relative_url = item['href']
                url = f'{base_url}{relative_url}'
                result_manuals.append({
                    "title": title,
                    "url": url
                })
            return result_manuals
                # save_manuals(item, relative_url, url)
        except AttributeError:
            print(AttributeError)
            return result_manuals
    return False

def save_manuals(title, url):
    manuals_manuals = Manuals(title=title, url=url)
    db.session.add(manuals_manuals)
    db.session.commit()

    save_manuals(title, url)