import re
exp = r'(^1(01*0)*1|0)+$'
s = r'0 0'
result = re.match(exp, s)
print(result)
