family_name = ["Shahithyan", "Darshan", "Priya", "Vijayaraj"]
print(type(family_name))  # <class 'list'>
print(family_name)
print(family_name[2])  # Accessing third elemen
print(len(family_name))  # Length of the list

family_age = [ 14,10,37,40]
print(type(family_age))  # <class 'list'>
print(family_age)

# printing family name
for name in family_name:
    print(name)

# printing family age
for age in family_age:
    print(age)

i = 1
while i <= 6:
    print(i)
    i += 1  # Incrementing i by 1

if i == 6:
    print("i is equal to 6")
else:
    print("i is not equal to 6")

j = 7
 
if i > j:
     print("i is greater than j")
elif i == j:
    print("i is equal to j")
else:
    print("i is not greater than j")