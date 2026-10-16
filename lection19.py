import requests
from bs4 import BeautifulSoup

def lection19():
    """
    web scraping (bs4)
    """
    articles_list = []
    r = requests.get("https://habr.com/ru/all")
    soup = BeautifulSoup(r.content, "html5lib")
    # print(soup.prettify())
    # article-snippet-title-link
    articles = soup.find_all("article", attrs = {"class":"tm-articles-list__item"})
    for article in articles:
        title = article.find("h2").find("span")
        #print(title.text)
        articles_list.append(title.text)

    for a in sorted(articles_list):
        print(a)

