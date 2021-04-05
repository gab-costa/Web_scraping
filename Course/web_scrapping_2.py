import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

import ssl
#ignoring ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('enter with a url')
html1 = urllib.request.urlopen(url, context=ctx)
html2= html1.read()

print(html1)
#soup = BeautifulSoup(html2, 'html.parser')



#tags = soup('div')
#for tag in tags:
 #   print(tag.get('class', None))

