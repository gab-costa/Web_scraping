

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
lista = []
for tag in tags:
    lista.append(tag)

lista_2 = []
for x in range(0, len(lista)):
    z = str(lista[x])
    lista_2.append(re.findall(r'[0-9]+' , z))


soma = 0
for j in lista_2:
    soma+=int(j[0])
    print(j[0])

print(f'the sum is: {soma}')