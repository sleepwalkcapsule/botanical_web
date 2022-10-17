from cgitb import html, text
from unittest import result
from bs4 import BeautifulSoup
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
    html = get_html("https://harvesttotable.com/#")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_manuals = soup.find('ul', class_="mega-sub-menu").findAll('li')
        print(all_manuals)
        result_manuals = []
        for manuals in all_manuals:
            title = manuals.find('a').text
            # print(title)
            url = manuals.find('a')['href']
            # published = manuals.find('time').text
            result_manuals.append({
                "title": title,
                "url": url
            })
            # print(title)
            # print(url)
            # print(published)
        return result_manuals
    return False

# if __name__ == "__main__":
    # if html:
        # with open("botanical.org.html", "w", encoding="utf8") as f:
        #     f.write(html)
        # manuals = get_manuals(html)
        # print(manuals)