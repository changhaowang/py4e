# Chapter 9 Dictionaries Page 115
name = dict()
print('Empty dictionary:',name)
name['First name'] = 'Changhao'
name['Last name'] = 'Wang'
name['middle name'] = ''
print('Dictionary:',name)
name_new = {'First name':'Aiping','middle name':'','Last name':'Qu'}
print('New Dictionary:',name_new)
length = len(name)
print('Length of the Dictionary:',length)
# Method:value Convert the dictionary to list
name_list = list(name.values())
print('Convert the dictionary to list:',name_list)
# Method: get() Syntax: get('something',default = None)
print('Use of get():',name.get('middle name')) # Output is ''
print('Use of get() with default value:',name.get('name')) # Output is None
print('Use of get with the second value changed:',name.get('name','There is no this value'))
# remove the key:
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print('The dict of the names list:',counts)
### Two iteration variables!!!!!!!!!!!!!
# See it in TwoIterationVariables.py!!!!
