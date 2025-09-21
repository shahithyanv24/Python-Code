car = {
    "brand": "BMW",
    "model": "M4",
    "year": 2021
}

print(car) 
print(type(car))
print(car["brand"])
print(len(car))

x = car["model"]
print(x)

y = car.keys()
print(y)

z = car.values()
print(z)

car["color"] = "black"
print(car)

car["model"] = "X5"
print(car)

b = car.items()
print(b)

if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")

car.pop("color")
print(car)

for x in car:
    print(x)

for x in car:
    print(car[x])

for x in car.values():
    print(x)

for x in car.keys():
    print(x)

for x, y in car.items():
    print(x, y)

car = car.copy()
print(car)