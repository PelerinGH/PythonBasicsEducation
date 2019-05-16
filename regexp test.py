import re

exp = r"\b[aeiouAEIOU]\w+"
s = "AV is largest Analytics community of India"
result = re.findall(exp, s)
print(result)
