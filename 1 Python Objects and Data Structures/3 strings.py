# Strings are ordered sequences of characters with single or double quotes
# Strings can be slices and indexed
# Indexing grabs a single character from the string
# uses [] with the index
# Reverse indexing also possible in Python
# Slicing allows you to grab a subsection of multiple characters
# Strings are immutable


name = 'Narayanan'
last_letters = name[1:]
print(last_letters) #arayanan

total_name = 'N' + last_letters
print(total_name)

letter = 'z'; # zzzzzzzzzz
print(letter * 10)

letters = '2' + '3'
print(letters) # 23

x = 'Hello world'
print(x.upper()) # HELLO WORLD
print(x.lower()) # hello world

x = 'This is a string'
print(x.split('i')) # ['Th', 's ', 's a str', 'ng']