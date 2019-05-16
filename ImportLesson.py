import datetime

year, month, day = tuple(int(i) for i in input().split())
date1 = datetime.date(year, month, day)
delta = datetime.timedelta(int(input()))
date2 = date1 + delta
print(date2.year, date2.month, date2.day)
