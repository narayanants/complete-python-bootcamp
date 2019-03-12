# NESTED STATEMENTS

x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# LEGB RULE

name = 'My Name is Narayanan'


def greet():
    name = 'Sammy'

    def hello():
        print('Hello' + name)
    hello()


# Another function
z = 50


def func():
    global x
    print(f'X is {x}')

    x = 'New Value'
    print(f'I just locally changed global X to {x}')


print(x)
func()
