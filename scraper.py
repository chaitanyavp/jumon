import requests
from bs4 import BeautifulSoup
import sys

def get_price(line):
	price = ""
	num = False
	for c in line:
		if c == '$':
			num = True
		elif c == ' ' and num:
			num = False
			break
		elif c == ' ':
			num = False
		elif num:
			price += c
	if price == '':
		return 9999999
	else:
		return float(price)


def price_sort(lines):
	if len(lines) > 1:
		half = int(len(lines)/2)
		first_half = price_sort(lines[:half])
		second_half = price_sort(lines[half:])
		i, j = 0, 0
		final_lines = []

		while i < len(first_half) and j < len(second_half):
			if get_price(first_half[i]) < get_price(second_half[j]):
				final_lines.append(first_half[i])
				i += 1
			else:
				final_lines.append(second_half[j])
				j += 1

		if i < len(first_half):
			final_lines += first_half[i:]
		elif j < len(second_half):
			final_lines += second_half[j:]

		return final_lines

	elif len(lines) == 1:
		return [lines[0]]
	else:
		return []


toadparams = {'search_words': sys.argv[1], 'search_category': '', 'search_order': 'price_asc'}
page = requests.get("https://www.trollandtoad.com/products/search.php", params=toadparams)
parsed = BeautifulSoup(page.content, 'html.parser')
prices = parsed.find_all(class_='search_result_text')

unsorted_lines = []
for x in prices:
	text = x.get_text()
	if text[-13:] == "SELL US YOURS":
		unsorted_lines.append(text[:-13])
	else:
		unsorted_lines.append(text)

# sorted_lines = price_sort(unsorted_lines)

return unsorted_lines[:20]: