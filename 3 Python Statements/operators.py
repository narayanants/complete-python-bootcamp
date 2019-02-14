from random import shuffle
from random import randint
'''
Useful Operators
=================

    * range(0,11,2)
    * enumerate()
    * zip
    * min
    * max
    * randint
    * input

'''
for num in range(0, 11, 2):
    print(num)


print(list(range(0, 11, 2)))

index_count = 0
for letter in 'ABCDE':
    print('At index {} the letter is {}'.format(index_count, letter))

word = "ABCDE"
for index, letter in enumerate(word):
    print(index)
    print(letter)

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3):
    print(item)


print(2 in [2, 3, 4])


mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(min(mylist))
print(max(mylist))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
shuffle(mylist)
print(mylist)

print(randint(0, 100))


letter_input = input('Enter a number')
