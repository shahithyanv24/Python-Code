def add_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

x = 7
print(type(x))  # <class 'int'>
print(x)

b = 18
sum = add_numbers(x, b)
product = multiply_numbers(x, b)
print("The product of", x, "and", b, "is", product)
print("The sum of", x, "and", b, "is", sum)

d = 6
s = 10

sum2 = add_numbers(d, s)
product2 = multiply_numbers(d, s)
print("The product of", d, "and", s, "is", product2)
print("The product of", product2, "and", product, "is", multiply_numbers(product2, product))
print("The sum of", d, "and", s, "is", sum2)

y = "Shahithyan"
print(type(y))  # <class 'str'>
print(y)

z = 3.14
print(type(z))  # <class 'float'>
print(z)

a = True
print(type(a))  # <class 'bool'>
print(a)

if a:
    print("Boolean value is True")
    print("This is executed because the condition is True")
else:
    print("Boolean value is False")
