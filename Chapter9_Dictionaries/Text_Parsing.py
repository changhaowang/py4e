# Advanced text parsing Page 121
import string
inp = input("Please enter the filename:")
if inp == '':
    inp = 'romeo_punctuation.txt'
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
count = dict()
for line in fhand:
    line = line.lower()
    Tran = line.maketrans('','',string.punctuation) # the use of maketrans() & translate
    line = line.translate(Tran)
    line = line.split()
    for word in line:
        count[word] = count.get(word,0) + 1
print(count)
