import urllib.request, urllib.parse, urllib.error
import json

url=input("Enter a URL: ")
u = urllib.request.urlopen(url)
dat=u.read()
data = json.loads(dat)

total = 0
for tags in data['comments']:
    total += tags['count']
    print(total)
