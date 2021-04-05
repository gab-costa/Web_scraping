import urllib.request, urllib.parse, urllib.error
import re
import xml.etree.ElementTree as ET
import ssl

from bs4 import BeautifulSoup

#ignoring ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = 'http://py4e-data.dr-chuck.net/comments_1206870.xml'
datas = urllib.request.urlopen(url, context=ctx).read()

#print(datas.decode())
reserved = datas.decode()

cont = 0
numbers = re.findall(r'<count>(\S+)<',reserved)

for x in numbers:
    cont+=int(x)

print(cont)
