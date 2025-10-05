days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for x in days:
  print(x)

for x in "Thu":
    print(x)

for x in days:
  print(x)
  if x == "Fri":
    break
  
for x in days:
  if x == "Wed":
    break
  print(x)

for x in days:
    if x == "Sat":
        continue
    print(x)

for x in range(7):
  print(x)

for x in range(2, 7):
  print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
   print(x)
else:
   print("Finally finished!")