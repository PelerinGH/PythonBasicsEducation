# Cчетчик с помощью замыканий Python
def a():
    c = 0
    def f():
        nonlocal c
        c+=1
        return c
    return f
x=a()
print(x())
print(x())
print(x())
print(x())
print(x())
print(x())
print(x())
print(x())
