# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


class Line(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.c1
        x2, y2 = self.c2
        return (y2-y1)/(x2-x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


# Problem 2: Fill in the class

class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * self.pi * (self.radius) ** 2

    def surface_area(self):
        top = self.pi * (self.radius) ** 2
        return (2*top) + (2*3.14*self.radius*self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


# Challenge Problem:

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dept_amt):
        self.balance += dept_amt
        print('Added {} to the balance'.format(dept_amt))

    def withdrawl(self, wd_amt):

        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawl accepted')
        else:
            print('Sorry not enough funds!!')

    def __str__(self):
        return "Owner is {} \n  Balance is {}".format(self.owner, self.balance)


a = Account('Sam', 500)
print(a.owner)
print(a.balance)
print(a.deposit(100))
print(a.withdrawl(600))
print(a.withdrawl(100))
