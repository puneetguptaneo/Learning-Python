import requests
from bs4 import BeautifulSoup

def NEO_scraper():
	url = "https://eztv.ag/search/silicon-valley"
	r = requests.get(url)
	plain_text = r.text
	soup = BeautifulSoup(plain_text, 'lxml')
	fw = open("Sample.txt", "w")

	for link in soup.find_all('a', {'class' : 'magnet'}):
		title = link.get('title')
		if '720p' in title:
			href = link.get('href')
			fw.write(href + '\n')	
		
	fw.close()

NEO_scraper()