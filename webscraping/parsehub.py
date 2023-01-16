#!/usr/bin/python3

# import libraries
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# define url opener function
def getHeader(url):
    try:
        head_url = urlopen(url)
    except HTTPError as err:
        return err
    try:
        bs = BeautifulSoup(head_url.read(), 'html.parser')
        head_url = bs.body.h1
    except AttributeError as err:
        return None
    return head_url

head_url = getHeader('https://www.parsehub.com/blog/beginners-guide-to-web-scraping')
if head_url == None:
    print('Title not found!')
else:
    print(head_url)
