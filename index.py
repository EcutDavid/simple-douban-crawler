from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

DOUBAN_SHANGHAI_URL = 'https://shanghai.douban.com/'

try:
    with urlopen(DOUBAN_SHANGHAI_URL) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(e)

if html != None:
    pageObj = BeautifulSoup(html, 'html.parser')
    for div in pageObj.findAll('div'):
        print(div.get_text())
