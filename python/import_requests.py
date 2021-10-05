import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
titres_bs = soup.find_all("a", class_="gem-c-document-list__item-title")
descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
list = []
articles = {}
articleName = ""
articleDesc = ""
for i in range(len(titres_bs)):
    articleName = titres_bs[i].string
    articleDesc = descriptions_bs[i].string
    articles[articleName] = articleDesc
    list.append(articleName + " : " + articleDesc)
    #list.append(f"{articleName} : {articleDesc}")
for i in range(len(list)):
    print(f"{i+1}/ {list[i]}")