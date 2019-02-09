# Dictionary

# Unordered mapping for storing objects
# Use K:V pair to store objects
# K:V helps in grabbing the objects without knowing the index location
# Dictonary uses {} and colons to signify the keys and their associated values

# When to use a List and Dictionary
# Dictionary : Objects retrieved by Key Name
# List : Objects retrieved by location
# Ordered sequence can be indexed and sliced.



my_dict = {'name':'Narayanan'}
print(my_dict['name']) # Narayanan

prices_lookup = {"apples":2.99,"Chocolates":5.10,"Oranges":10.10}
print(prices_lookup['apples']) # 2.99

d = {'k1':123,'k2':[12,44,12.12],'k3':{'insertKey':100}}
print(d['k2']) # [12, 44, 12.12]
print(d['k2'][2]) #12.12
print(d['k3']['insertKey']) #100

d = {'k1':['a','b','c']}
print(d['k1'][2].upper()) # C

d= {'k1':100,'k2':200}
d['k3'] = 300
print(d) #{'k1': 100, 'k2': 200, 'k3': 300}


print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
print(d.values()) # dict_values([100, 200, 300])
print(d.items()) # dict_items([('k1', 100), ('k2', 200), ('k3', 300)])