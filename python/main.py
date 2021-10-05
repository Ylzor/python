import requests
from bs4 import BeautifulSoup
url = "http://C:/Users/CDA05.AFPA/python/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)