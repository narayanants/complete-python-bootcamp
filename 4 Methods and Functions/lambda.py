def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

list(map(square(my_nums)))


# MAP FUNCTION
def splicer(s):
    if len(s) % 2 == 0:
        return 'EVEN'
    else:
        return s[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))


# FILTER FUNCTION
def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(check_even, my_nums)))


# LAMBDA EXPRESSION
mynums = [1, 2, 3, 4, 5, 6, 7]

print(map(lambda num: num ** 2, my_nums))


# CHECK EVEN
mynums = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(lambda num: num % 2 == 0, mynums)))


# FILTER NAMES
names = ['Narayanan', 'Gopal', 'Krish']

print(list(map(lambda name: name[0], names)))
