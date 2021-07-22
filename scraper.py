import requests
from bs4 import BeautifulSoup
import string

url = "https://www.nature.com/nature/articles"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

title_news = []


for i in soup.find_all('article'):
    span = i.find('span', {"class": "c-meta__type"}).text
    if span == 'News':
        title = i.find('a', {'data-track-label': "link"}).text
        name = title.strip().translate(str.maketrans(" ", "_", string.punctuation)) + ".txt"
        title_news.append(name)
        print(title_news)
        article_url = f"https://www.nature.com{i.a.get('href')}"
        print(article_url)
        r2 = requests.get(article_url)
        soup2 = BeautifulSoup(r2.content, 'html.parser')
        article_body = soup2.find('div', {'class': 'c-article-body'}).text.strip()
        body = article_body.replace("\n", "")
        print(body)
        file = open(name, 'w', encoding='UTF-8')
        file.write(body)
        print('File written')
        file.close()












