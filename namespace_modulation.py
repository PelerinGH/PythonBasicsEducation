dic = {'global': {'vars': []}}


def create(ns, parent):
    dic[ns] = {'parent': parent, 'vars': []}


def add(ns, var):
    if ns in dic:
        dic[ns]['vars'] += [var]


def get(ns, var):
    if var in dic[ns]['vars']:
        print(ns)
    elif ns == "global":
        print("None")
    else:
        get(dic[ns]['parent'], var)


for i in range(int(input())):
    cmd, ns, arg = input().split()
    if cmd == "add":
        add(ns, arg)
    elif cmd == 'create':
        create(ns, arg)
    elif cmd == 'get':
        get(ns, arg)
