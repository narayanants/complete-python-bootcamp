'''
Tuples
------

* Similar to lists
* They are immutable
* Once an element is assigned to a tuple it cannot be reassigned
* Tuples use parenthesis (1,2,3)
* Read only lists

'''


t = (1, 2, 3)
print(type(t))  # <class 'tuple'>
print(len(t))  # 3

print(t[0])  # 1
print(t[-1])  # 3

t = ('a', 'a', 'b')
print(t.count('a'))  # 2
print(t.index('a'))  # 0
print(t.index('b'))  # 2
