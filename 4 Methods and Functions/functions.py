'''
Function in Python:
====================

Create blocks of code that can be easily executed many times

'''


def name_of_function(name):
    '''
    Docstring explaning the function
    '''
    print('Hello' + name)


def somefunction(name):
    print('Hello', name)


def addfunc(n1, n2):
    return n1 + n2


def name_function():
    print('Hello world')


def print_my_name(name="Gokul"):
    return 'My name is ' + name


result = print_my_name()
print(result)


def add(n1, n2):
    return n1+n2


result = add(20, 30)
print(result)


# PIG LATIN:
def pig_latin(word):
    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = first_letter + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
