import requests
import re

def icango(page_from,page_to,num_jump=2):
    regex = r'<a href="(.*?)">'
    r = requests.get(page_from)
    if r.status_code==200:
        urls=re.findall(regex, str(r.content))
        if num_jump==1 and page_to in str(r.content):
            return True
        for url in urls:
            if num_jump>0 and icango(url, page_to, num_jump-1):
                return True
    return False

A=input()
B=input()
receive=icango(A,B)
print("Yes" if receive else "No")