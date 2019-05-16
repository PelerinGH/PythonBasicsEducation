import requests
import re

link="http://pastebin.com/raw/7543p0ns"
regex =r'<a .*?href=["\'](?:\w*?://)?(\w[\w.-]*)'
r = requests.get(link)
urls=re.findall(regex, str(r.content))
urls=list(set(urls))
urls.sort()
for l in urls:
    print(l)