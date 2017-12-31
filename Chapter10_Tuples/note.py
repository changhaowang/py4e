# Note Chapter 10 Tuples Page 125
# Tuples are immutable
a = tuple(["a","b"])
print(a)
b = tuple((1,2))
print(b)
print(a+b)
####Comparison Operators
### Tuple assignment
m = ('Changhao','Wang')
First_name, Last_name = m
print(First_name)
print(Last_name)
# Remember when you use dictionary to do this, the order is unexpected
# Use tuple to swap
a = 1
b = 2
print("origin, a=",a,'b=',b)
a,b = b,a
print("After swaping, a=",a,'b=',b)
mail = 'Changhaowang@berkeley.edu'
mail = mail.split('@')
username,domain = mail
print('username:',username,'domain:',domain)
#Dictionary and tuple
d = {'A':10,'A-':5,'F':20}
t = list(d.items())
t_new = list()
print(t)
for key,value in t:
    t_new.append((value,key))
t_new.sort(reverse=True)
print(t_new)
#Use tuple as keys of dictionaries
