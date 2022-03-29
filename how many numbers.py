def arti(i1, i2):
    return i1 + i2

def eksi(i1, i2):
    return i1 - i2

def invoke(func, value1, value2):
    return func(value1, value2)

print(invoke(arti, 2, 4))