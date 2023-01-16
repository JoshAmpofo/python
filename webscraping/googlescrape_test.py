# import libraries
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# define url scraper function
def getUrl(url):
    try:
        html = urlopen(url)  # open url
    except HTTPError as err:
        return err
    try:  # parse url tag to BeautifulSoup
        bs = BeautifulSoup(html.read(), 'html.parser')
        Url = bs.body.h1  # target tag
    except AttributeError as err:  # handle if tag calls a None tag
        return None
    return Url
    
Url = getUrl('https://www.google.com')
if Url == None:
    print("Url not found")
else:
    print(Url)