# Two iteration varibales
# We can have multiple itertion variables in a for loop
name = {'first name':'Changhao','middle name':None,'last name':'Wang'}
keys = list(name.keys())
values = list(name.values())
items = list(name.items())
print("Keys of the dict:",keys)
print("Values of the dict:",values)
print("Items of the dict:",items)
for key,value in items:  # Two Itertion Values
    print('Keys and Values of the dict:',key)
