import requests
from bs4 import BeautifulSoup
import sys


toadparams = {'search_words': 'abyssmegalo', 'searchmode': 'basic'}
page = requests.get("https://www.trollandtoad.com/products/search.php", params=toadparams)
parsed = BeautifulSoup(page.content, 'html.parser')
prices = parsed.find_all(class_='price_text')

for x in prices:
    print ("ye", x.get_text())
print("ye", prices[0].get_text())