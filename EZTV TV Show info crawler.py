import requests
from bs4 import BeautifulSoup

def get_info(info_url):
    code = requests.get(info_url)
    plain_text = code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('td', {'class':'section_post_header'}):
        print(link.string)

def trade_spider():
    url = 'https://eztv.ag/search/?q1=&q2=929&search=Search'
    code = requests.get(url)
    plain_text = code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('a', {'class':'epinfo'}):
        href = "https://eztv.ag" + link.get('href')
        get_info(href)

trade_spider()