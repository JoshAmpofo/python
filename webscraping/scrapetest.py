#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://pythonscraping.com/pages/page1.html')
except HTTPError as err:
    print(err)
except URLError as err:
    print("Server could not be found!")
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
