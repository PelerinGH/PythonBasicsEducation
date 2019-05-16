import requests

r = requests.get('https://www.python.org')
print(type(r.status_code))