# Exercise 4 Chapter 8 Page 106
fhand = open('romeo.txt')
fl = []
for line in fhand:
    word = line.split()
    length = len(word)
    for i in range(0,length):
        if word[i] not in fl:
            fl.append(word[i])
fl.sort()
print(fl)
