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
    eventContainer = pageObj.find('div', {'id': 'db-events-guess'})
    for item in eventContainer.findAll('div', {'class': 'title'}):
        print('Event name:', item.contents[1].get('title'))
        print('      ----:', item.contents[1].get('href'))
