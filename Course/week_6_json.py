import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = 'http://py4e-data.dr-chuck.net/comments_1206871.json'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)
count = 0
for x in range(0,len(info['comments'])):
    somador = int(info['comments'][x]['count'])
    count+=somador
print(count)
