import requests
from bs4 import BeautifulSoup
url = "https://github.com/Ylzor/python/blob/main/python/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
