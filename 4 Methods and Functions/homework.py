# Volume of sphere given the radius


def vol(rad):
    return (4/3) * (3.14) * (rad ** 3)


print(vol(4))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(num, low, high):
    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range')


print(range_check(35, 10, 100))


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


def uplow(s):
    d = {'upper': 0, 'lower': 0}
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


print(uplow('My Name is BILLA'))


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(unique([1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, ]))


# Write a Python function to multiply all the numbers in a list.

def mul(num):
    total = 1
    for x in num:
        total *= x
    return total


print(mul([1, 2, 3, -4]))


# Write a Python function that checks whether a passed string is palindrome or not.

def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print(palindrome('nurses run'))
