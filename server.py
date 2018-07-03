import requests
from bs4 import BeautifulSoup
import sys
import scraper
from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__, template_folder='jumon-app/src')

@app.route("/index.html")
def output():
	return render_template('index.html', name='Joe')
	
@app.route('/receiver', methods = ['POST'])
def worker():
	
	name = request.args.get('name')
	print(request.args.get('name'), file=sys.stderr)
	ebay_scrap = scraper.scrape_ebay(name)
	data = scraper.scrape(name)[0]
	str2 = ""
	
	for x in data:
		str2 += x + '\n'
	
	return str2
	
if __name__ == "__main__":
	app.run("127.0.0.1", "8080")
