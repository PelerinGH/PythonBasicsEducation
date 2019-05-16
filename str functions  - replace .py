s = input()
a = input()
b = input()
i = 0
while True:
    print(s)
    if a in s:
        print(s)
        s = s.replace(a, b)
        i += 1
    else:
        print(i)
        break
    if i > 1000:
        print("Impossible")
        break
