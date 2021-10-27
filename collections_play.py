fruits = ['apple', 'pearl', 'banana', 'mongo']
fruits.reverse()
fruits.sort()
print(fruits)

my_list = [5] * 10
list_2 = [4, 10]
print(my_list + list_2)

# slice
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
list_copy = my_list.copy()
print(my_list[:-2])
print(list_copy)
print(list(my_list))

squares = [i * i for i in my_list]
print(squares)

my_set = set("This is the what we have")
set_2 = set("have a great day")
print(my_set.union(set_2))
print(my_set.intersection(set_2))


# enumerate
names = ['Bob', 'Jerry', 'Jim', 'Dave']
for index, name in enumerate(names):
    print(f'{index} --> {name}')

# zip: if the length is different, zip will stop at the shortest list
name = ['tim', 'joe', 'billy']
age = [21, 20, 19]
print(list(zip(name, age)))

for name, age in zip(name, age):
    print(f'{name}: {age}')

# unpacking
