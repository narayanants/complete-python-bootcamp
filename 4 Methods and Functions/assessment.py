# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd


def sphere(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(sphere(100, 20))

# Write a function takes a two-word string and returns True if both words begin with same letter


def circle(s):
    someword = s.split()
    print(someword[0][0])
    print(someword[1][0])
    return someword[0][0] == someword[1][0]


print(circle('Pettai Parak'))

# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶


def hexagon(a, b):
    if a+b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False


print(hexagon(10, 10))


def circle1(a, b):
    return (a+b) == 20 or a == 20 or b == 20


print(circle1(10, 20))


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def capital(n):
    if len(n) > 3:
        return n[:3].capitalize() + n[3:].capitalize()
    else:
        print('Name is too short')


print(capital('Narayanan'))


# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(s):
    return ' '.join(s.split()[::-1])


print(master_yoda('I am home'))


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def hello(n):
    return((abs(100 - n) <= 10)) or ((abs(200 - n) <= 10))


print(hello(99))


# LEVEL 2 Problems

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def has_33(n):
    for i in range(0, len(n) - 1):
        if n[i:i+2] == [3, 3]:
            return True
    return False


print(has_33([1, 3, 5, 6, 3, 5, 67, 3, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def rocket(s):
    result = ''
    for char in s:
        result += char * 3
    return result


print(rocket('Mass maranam tough tharanum adhuku avan dhan porandhu varanam'))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    if a+b+c == 21:
        return a+b+c
    elif a+b+c <= 31 and 11 in (a, b, c):
        return a+b+c - 10
    else:
        return 'BUST'


print(blackjack(10, 11, 10))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([1, 3, 5]))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(n):
    code = [0, 0, 7, 'x']
    for num in n:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3, x, 2):  # test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(100))
