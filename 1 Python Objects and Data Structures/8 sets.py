# Sets

# Sets are unordered collection of unique elements
# Meaning there can be only be one representative of the same object


myset = set()
print(myset) #set()

myset.add(1)
print(myset) #{1}

myset.add(2)
print(myset) #{1, 2}

myset.add(2)
print(myset) #{1, 2}

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,]
print(set(mylist)) # {1, 2, 3, 4, 5}