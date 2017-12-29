# Exercise 1 Chapter 8 Page 107
def chop(t):
    del t[-1]
    del t[0]
def middle(t):
    length = len(t)
    return t[1:length-1]
inp = ['Changhao','is','smart','!',1]
inp_new = middle(inp)
chop(inp)
print('chop:',inp)
print('middle:',inp_new)
