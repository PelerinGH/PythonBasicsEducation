# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern=r"\b\w*?cat\w*?\b"
    if re.search(pattern,line):
        print(line)