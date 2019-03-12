# CLASS KEYWORD
# Blueprint of the future object


class Sample():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Dog():
    def __init__(self, breed):  # Constructor
        self.breed = breed


mydog = Dog(breed='lab')

print(mydog.breed)
