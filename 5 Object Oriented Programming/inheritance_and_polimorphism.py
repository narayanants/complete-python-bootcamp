# Inheritance and Polimorphism


class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an Animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created!')

    def bark(self):
        print('WOF!!')

    def eat(self):
        print('I am eat and I am eating')


dogs = Dog()
print(dogs.eat())
print(dogs.who_am_i())


# Polymorphism

class Pig():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof !'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow !'


niko = Pig('niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())


# Polymorphism using Felix

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


class Animals():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass must implement this abstract method")


myanimal = Animals('freed')
myanimal.speak()
