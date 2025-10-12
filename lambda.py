x = lambda a: a + 5
print(x(5))

y = lambda a, b: a * b
print(y(6, 7))

z = lambda a, b, c: a + b + c
print(z(5, 6, 7))

def mydouble(n):
    return lambda a: a * n

mydoubler = mydouble(2)

print(mydoubler(40))

def mytriple(n):
    return lambda a: a * n 

mytripler = mytriple(3)

print(mytripler(40))