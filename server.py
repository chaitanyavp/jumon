import requests
from bs4 import BeautifulSoup
import sys
import scraper
from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route("/index.html")
def output():
	return render_template('index.html', name='Joe')
	
@app.route('/receiver', methods = ['POST'])
def worker():
	toadparams = {'search_words': 'abyssmegalo', 'searchmode': 'basic'}
	page = requests.get("https://www.trollandtoad.com/products/search.php", params=toadparams)
	parsed = BeautifulSoup(page.content, 'html.parser')
	prices = parsed.find_all(class_='search_result_row_wrapper')

	arr = []
	str = ""

	for x in prices:
		name = x.find(class_='search_result_text').find_all('h2')[0].get_text()
		price = x.find(class_='price_text').get_text()
		object = {'name': name, 'price': price}
		str += name + " " + price + "\n"
	
	
	str2 = ""
	data = scraper.scrape("abyssmegalo")[0]
	
	for x in data:
		str2 += x + '\n'
	
	return str2
	
if __name__ == "__main__":
	app.run("127.0.0.1", "8080")
