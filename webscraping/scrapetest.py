#!/usr/bin/python3

# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# from bs4 import BeautifulSoup

# try:
#     html = urlopen('https://pythonscraping.com/pages/page1.html')
# except HTTPError as err:
#     print(err)
# except URLError as err:
#     print("Server could not be found!")
# else:
#     bs = BeautifulSoup(html.read(), 'html.parser')
#     print(bs.h1)

########################################################
# Handling Attribute Errors 
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup 

def getTitle(url):
    try:
        html = urlopen(url)  # read url
    except HTTPError as err:  # if url cannot be found
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1  # retriee tag
    except AttributeError as err:  #  if tag doesn't exist
        return None 
    return title
# get target URL
title = getTitle('https://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
