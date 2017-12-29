# Exercise 1 Page 95
fname = input('Enter the file name: ')
try:
    fhand = open(fname,'r')
except:
    print('Cannot open the file:',fname)
    quit()
for line in fhand:
    line = line.upper()
    print(line)
