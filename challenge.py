import urllib.request, urllib.parse, urllib.error
import re

from bs4 import BeautifulSoup

import ssl
#ignoring ssl certificate errors





url = 'http://py4e-data.dr-chuck.net/known_by_Kareem.html'

cont = True


while cont<=7:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    lista = []
    for tag in tags:
        lista.append(tag.get('href', None))
    link = lista[17]

    cont+=1
    #print(link)
    url = link


# finding the name in the last link

name = re.findall(r'by_(\S+).html',link)
print(f'last name in sequence: {name[0]}')


