# read the file
fhand = open('mbox.txt') #
inp = fhand.read()
count_open = 0
fhand = open('mbox.txt')
for line in fhand:
    count_open += 1
length = len(inp)
count = 0
for letter in inp:
    if letter == '\n':
        count += 1
print(count,count_open)
#print(inp)
