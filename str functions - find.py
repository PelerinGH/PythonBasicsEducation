s = input()
t = input()
n = 0
start = 0
len_s = len(s)
while True:
    if n < len_s:
        x = s.find(t, start)
        if x != -1:
            n += 1
            start = x+1
        else:
            print(n)
            break
    else:
        print(n)
        break