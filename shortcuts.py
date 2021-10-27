import itertools

# unpacking:
tup = (1, 2, 3, 4)

value = "welcome"
a, b, c, d = tup
print(a, b, c, d)

a, b, c, d, e, f, h = value
print(a, b, c, d)

a, *b = value
print(a, b)

# using _ to skip value not intended to use
a, _ = (1, 2)
print(a)

# multiple assignment
width, height = 400, 500
print(width, height)

# swap in place
height, width = width, height
print(width, height)


# Comprehension
x = [i for i in range(10, 100) if i % 2 == 0]
print(x)

x = [[i for i in range(5)] for _ in range(5)]
print(x)

x = (i for i in "hello")
print(tuple(x))

sentence = "this is a good way to learn"
print(set(sentence))
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

# Object multiplication
x = "hello" * 5
print(x)

# Inline/Ternary Condition
x = 1 if 2 > 3 else 0
print(x)

# *arg and **kwargs


def func_1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func_2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 2, 3]
kwargs = {'arg1': 100, 'arg3': 1000, 'arg2': 50}
func_1(*args)
func_2(**kwargs)
print(*args)

# For Else & While Else
search = [1, 2, 3, 4, 5, 6]
target = 100
for element in search:
    if element == target:
        print('I found it')
        break
else:
    print('I did not find it')

# sort by key
lst = [[1, 2], [3, 4], [-1, 2], [4, -3], [5, 7]]
lst.sort(key=lambda e : e[0] + e[1])
print(lst)


num = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c', 'd']
chain_list = itertools.chain(num, lst2)
for v in chain_list:
    print(v, end='')

# big number with separator
print()
num1 = 10_000_000_000
num2 = 100_000_000
print(num1 + num2)
total = num1 + num2
print(f'{total:,}')