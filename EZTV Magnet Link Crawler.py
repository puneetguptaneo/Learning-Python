import requests
from bs4 import BeautifulSoup

def trade_spider():
    url = 'https://eztv.ag/search/?q1=&q2=929&search=Search'
    code = requests.get(url)
    plain_text = code.text
    soup = BeautifulSoup(plain_text, "lxml")
    fw = open('Jimmy Fallon Url.txt', "w")
    for link in soup.findAll('a', {'class':'magnet'}):
        href = link.get('href')
        fw.write(href + "\n")
    fw.close()
        

trade_spider()

