#use of "pass"
x=5
if (x>=5) :
    pass
else :
    print(x)
#####################
#function
def Changhao():
    print('He is clever')
a=Changhao()
print(a) #a = none
######################
#variables and return
def Changhao(a):
    return a
a=Changhao(3)
print(a)
#####################
def addtwo(a,b):
    added = a + b
    return added
print(addtwo('abc','asd'))
