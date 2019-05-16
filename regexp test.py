import re

exp = r'<a .*?href=["\'](?:\w*?://)?(\w[\w.-]*)'
s = r'<li><a href="adworker.ru/">'
result = re.findall(exp, s)
print(result)
