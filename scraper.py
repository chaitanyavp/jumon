import requests
from bs4 import BeautifulSoup
import sys


toadparams = {'search_words': sys.argv[1], 'searchmode': 'basic'}
page = requests.get("https://www.trollandtoad.com/products/search.php", params=toadparams)
parsed = BeautifulSoup(page.content, 'html.parser')
prices = parsed.find_all(class_='search_result_text')

for x in prices[:20]:
	text = x.get_text()
	if text[-13:] == "SELL US YOURS":
		print("ye", text[:-13])
	else:
		print("ne", text)
