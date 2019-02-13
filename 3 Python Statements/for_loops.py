'''
For Loops:
==========

    

'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number {num}')


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for num in mylist:
    list_sum = num + list_sum
print(list_sum)


mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in mylist:
    print(a)


d = {'k1': 1, 'k2': 2, 'k3': 3}
for k, v in d.items():
    print(k)
