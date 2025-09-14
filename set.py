numbers_set={1,2,3,4,5}
print(numbers_set)  # <class 'set'>\

letter_set = {'a', 'b', 'c', 'd'}

for x in numbers_set:
    print(x)

print(1 in numbers_set)
print(10 in numbers_set)

numbers_set.add(6)
print(len(numbers_set))
print(numbers_set)

numbers_set.remove(3)
print(numbers_set)

x = numbers_set.pop()
print(x)
print(numbers_set)

numbers_set.clear()
print(numbers_set)

set_n_l = numbers_set.union(letter_set)
print(set_n_l)