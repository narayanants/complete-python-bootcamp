'''
    IO with Text Files:
    ------------------

    r = read 
    w = write
    a = append

'''

with open('abcd.txt', 'w') as a:
    a.write('This is the First line \nThis is the second line \nThis is the third line')

with open('abcd.txt', 'r') as f:
    contents = f.read()
    print(contents)
