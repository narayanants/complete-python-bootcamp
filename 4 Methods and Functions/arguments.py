def myfunc(a, b):
    return sum((a, b) * 0.05)


print(myfunc(40, 60))


# kwargs

def somefunc1(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


somefunc(fruit="Strawberry")

# Second Function using args and kwargs


def newfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


newfunc(10, 20, 30, 40, fruit="orange", pet="dog", food="Bacon")


def myfunc1(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(
            f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc1('eggs', 'Bacon', fruit='cherries', juice='orange')
