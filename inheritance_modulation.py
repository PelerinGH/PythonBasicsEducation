dic = {}
def inher(c1,c2):
    if c1 == c2:
        return True
    elif dic[c2]==None:
        return False
    else:
        for z in dic[c2]:
            if inher(c1,z):
                return True
for i in range(int(input())):
    s=input().split(" : ")
    dic[s[0]]=s[1].split() if len(s)>1 else None
print(dic)
for i in range(int(input())):
    c1,c2 = input().split()
    print("Yes" if inher(c1, c2)  else "No")