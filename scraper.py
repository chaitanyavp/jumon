import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
parsed = BeautifulSoup(page.content, 'html.parser')
soup_str = parsed.prettify()


print("ye", list(parsed.children))