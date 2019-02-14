'''
    Elif and Else-if statements in Python
    ======================================

    Control Flow:
    -------------

    if (some_condition):
        #execute_some_code
    elif some_other_condition:
        #do_something_different
    else:
        #do_something
'''

name = "Narayanan"
if name == "Gokul":
    print('Hello Gokul')
elif name == "Deepak":
    print("Hello Deepak")
else:
    print('Hello Gokul')


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
sum = 0
for val in numbers:
    sum = sum + val
print("The sum is", sum)
