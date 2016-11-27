from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.google.com/').read()
except Exception as e:
    print(e)

if html != None:
    pageObj = BeautifulSoup(html, 'html.parser')
    print(len(pageObj.findAll('div')))
