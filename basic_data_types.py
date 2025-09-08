def add_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def subtract_numbers(num1, num2):
    return num1 - num2

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"
    
def remainder_numbers(num1, num2):
    return num1 % num2

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

c=10
e=5
f=4

sum2 = add_numbers(d, s)
product2 = multiply_numbers(d, s)
print("The product of", d, "and", s, "is", product2)
print("The product of", product2, "and", product, "is", multiply_numbers(product2, product))
print("The sum of", d, "and", s, "is", sum2)

difference = subtract_numbers(s, d)
print("The difference of", s, "and", d, "is", difference)

quotient = divide_numbers(c, e)
print("The quotient of", c, "and", e, "is", quotient)

rem=remainder_numbers(c, f)
print("The remainder of", c, "and", f, "is", rem)

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

name = "Shahithyan"
print(name.capitalize())  # Capitalizing the first letter
print(name.upper())  # Converting to uppercase
print(name.lower())  # Converting to lowercase
print(name.replace("yan", "darshan"))  # Replacing 'S' with 's
print(name.split("t"))  # Splitting the string at 'a'
print(name[0])  # Accessing the first character
print(len(name))  # Length of the string
print(name[1:5])  # Slicing the string from index 1 to 4
print(name[-1])  # Accessing the last character
print(name[-4:-1])  # Slicing the string from index -4 to -
print(name + " Darshan")  # Concatenating strings

if "Vijayaraj" in name:
    print("Vijayaraj is in the name")
else:
    print("Vijayaraj is not in the name")

name = name + " Vijayaraj"
print(name)
if "Vijayaraj" in name:
    print("Vijayaraj is in the name")
else:
    print("Vijayaraj is not in the name")
