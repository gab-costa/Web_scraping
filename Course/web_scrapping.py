import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('enter witj a url')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')



tags = soup('div')
for tag in tags:
    print(tag.get('class', None))

