# List are ordered sequence that can hold a variety of objects
# They use [] and commas to separate objects in the list
# Lists support indexing and slicing 
# Lists can be nested and also have a variety of useful methods that can be called off of them

my_list = [1,2,3]
my_list  = ['Narayanan',100,10.24]
len(my_list)


my_list = ['One','Two','Three']
my_list[0] #One
my_list[1:] #'Two','Three'

another_list = ['Four','Five']
total_list = my_list + another_list
print(total_list) # ['One', 'Two', 'Three', 'Four', 'Five']
 
total_list.append('Six')
total_list.append('Seven')
print(total_list) # ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']

total_list.pop()
print(total_list) # ['One', 'Two', 'Three', 'Four', 'Five', 'Six']


new_list = ['a','e','i','o','u']
num_list = [1,2,3,5,6,7]

new_list.sort()
sorted_list = new_list
print(sorted_list) # ['a', 'e', 'i', 'o', 'u']

num_list.sort()
num_sort_list = num_list
print(num_sort_list) # [1, 2, 3, 5, 7, 34]