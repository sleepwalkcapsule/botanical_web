from datetime import datetime
# from turtle import title
from bs4 import BeautifulSoup

from webapp.manuals.parsers.utils import get_html, save_manuals

# def get_habr_snippets():
#     html = get_html("https://habr.com/ru/search/?q=%D1%80%D0%B0%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D1%8F&target_type=posts&order=relevance")
#     if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         all_manuals = soup.findAll('ul', class_='content-list_posts').findAll('li', class_='content-list__item_post')
#         # result_manuals = []
#         for manuals in all_manuals:
#             title = manuals.find('a', class_='tm-article-snippet__title-link').text
#             url = manuals.find('a', class_='post__title_link')['href']
#             published = manuals.find('span', class_='tm-article-snippet__datetime-published').text
#             print(title, url, published)
#             # save_manuals(title, url)
            # """
            # try:
            #     published = datetime.strptime(published, '%Y-%m-%d')
            # except ValueError:
            #     published = datetime.now()
            # save_manuals(title, url, published)
            # """

def get_wiki_snippets():
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
                published = manuals.find('span', class_='anonymous-show').text
                try:
                    published = datetime.strptime(published, '%Y-%m-%d')
                except ValueError:
                    published = datetime.now()
                save_manuals(title, url, published)
                print(title, url, published)
        except AttributeError:
            print(AttributeError)
            """
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_manuals(title, url, published)
            """