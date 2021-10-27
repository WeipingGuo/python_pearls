
import sys
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5, 6]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5, 6)", number=1000000))

fruits = ('apple', 'banana', 'pear', 'cherry', 'mongo')
print(fruits[-1])

i1, *i2, i3 = fruits
print(f'i2 = {i2}')

part_fruits = fruits[1:2]
print(part_fruits)

fruits_list = list(fruits)

print(f'tuple size: {sys.getsizeof(fruits)} bytes')
print(f'list size: {sys.getsizeof(fruits_list)} bytes')

print(fruits_list)

if 'apple' in fruits:
    print('we got what we want ')

print(fruits.count('apple'))
for fruit in fruits:
    print(fruit)


