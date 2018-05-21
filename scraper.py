import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR0.TRC0.H0.Xallure+of+darkness.TRS0&_nkw=allure+of+darkness&_sacat=0")
parsed = BeautifulSoup(page.content, 'html.parser')
soup_str = parsed.prettify()

print("ye", list(parsed.children)[0])