# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
#
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
#
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.


dic = {}
used=set()

def inher(c1,c2):
    if c1 == c2:
        return True
    elif dic[c2]==None:
        return False
    else:
        for z in dic[c2]:
            if inher(c1,z):
                return True

def needless(c):
    for i in used:
        if inher(i,c):
            print(c)
            break
    used.add(c)
for i in range(int(input())):
    s=input().split(" : ")
    dic[s[0]]=s[1].split() if len(s)>1 else None
for i in range(int(input())):
    ex = input()
    needless(ex)