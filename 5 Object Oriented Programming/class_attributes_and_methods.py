# Class Attributes and Methods


class Sample():

    # Class Object Attributes

    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('WOF! My name is {}'.format(self.name))


mydog = Sample('lab', 'Raj')

print(mydog)


# Circle Class
class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


mycircle = Circle(30)
print(mycircle.get_circumference())
print(mycircle.area)
