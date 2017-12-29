# Exercise 5 Chapter 8 Page 112
inp = input('Enter a file name:')
try:
    fhand = open(inp)
except:
    print('Cannot open this file:',inp)
    quit()
count = 0
for line in fhand:
    word = line.split()
    length = len(word)
    if line.startswith('From') and length > 1:
        print(word[1])
        count += 1
print('''There were''',count,'''lines in the file with "From" as the first word''')
