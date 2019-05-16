import csv
tc15={}#types of crimes
with open("crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Date"][6:10] == "2015":
            t = row["Primary Type"]
            if t in tc15:
                tc15[t] += 1
            else:
                tc15[t] = 1
#print(tc15)
maxcrimes = max(tc15, key=tc15.get)
print(maxcrimes)