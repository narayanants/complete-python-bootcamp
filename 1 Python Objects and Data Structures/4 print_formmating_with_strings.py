# String Interpolation
print('This is a string {}'.format('INSERTED')) # This is a string INSERTED
print('The {} {} {}'.format('Fox','Trox','POX')) #The Fox Trox POX
print('The {0} {0} {0}'.format('Fox','Trox','POX')) # The Fox Fox Fox
print('The {q} {b} {f}'.format(f="FOX",b="Brown",q="quick")) #The quick Brown FOX


result = 100 /777
print('The Result was {r:1.3f}'.format(r=result)) # The Result was 0.129

results = 404.132839
print('The Result was {r:1.4f}'.format(r=results)) # The Result was 404.1328

# fstrings

name = 'Narayanan'
print(f'Hello My Name is {name}') # Hello My Name is Narayanan

name = 'Narayanan'
age = 25
print(f'{name} is {age} years old') # Narayanan is 25 years old

