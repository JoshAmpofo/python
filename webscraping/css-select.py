# This crawler will select some data based on the CSS style color
from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), 'html.parser')

# nameList = bs.find_all('span', {'class': 'green'})
# for name in nameList:
    # print(name.get_text())
    
# return all header tags in document
# name_tag = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# for tag in name_tag:
    # print(tag.get_text())
    
# return specific attributes in document
# name_css = bs.find_all('span', {'class': {'green', 'red'}})
# for style in name_css:
    # print(style.get_text())
    
# using the text argument to find specific number of times a string in doc has tags
nameList = bs.find_all(text='the prince')
print(len(nameList))