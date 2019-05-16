# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern=r"cat.*?cat.*?"
    if re.search(pattern,line):
        print(line)