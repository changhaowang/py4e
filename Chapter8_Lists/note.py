# Chapter 8 Lists Page 97
a = ['Changhao','Wang','scores',[100,200],'points','.']
# method: append & extend
a.append('Yeah!') #Note, the method returns None. it is different with str
a.extend(['He','is','so','clever','!'])
# method : sort (arranges the elements of the list from low to high)
b= ['He','is','clever','!']
b.sort()
print(b)
# method : delete (pop) retrus the element we removed.
c = ['a',1,'c']
x = c.pop(0)
print('After remove:',c)
print('What we removed is:',x)
# method : del
c = ['a',1,'c']
del c[0]
print(c)
# method : remove attention: it can only remove one element
c = ['a',1,'c',1]
c.remove(1)
print(c)
# convert string to List
d = 'Changhao'
e = list(d)
print(e)
f = 'Changhao Wang'
g = f.split()
print(g)
# string method : split()
s = 'spam-spam-spam'
s_new = s.split('-')
print(s_new)
# convert lists to string
t = ['pining','for','the','fjords']
delimiter = ' '
t_str = delimiter.join(t)
print(t_str)
