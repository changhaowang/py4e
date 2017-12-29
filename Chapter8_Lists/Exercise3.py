# Exercise 3 Chapter 8 Page 111
fhand = open('/home/wang/Desktop/py4e/Chapter7_Files/mbox-short.txt')
for line in fhand:
    word = line.split()
    if line.startswith('From') and len(word) > 2:
        print(word[2])
print('Finshed!') 
