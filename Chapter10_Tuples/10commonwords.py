#Note Chapter 10 TOP 10 Common words
import string
inp = input("Please enter the filename: ")
if len(inp) < 1:
    inp = 'mbox.txt'
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
    quit()
count = dict()
for line in fhand:
    line = line.lower()
    line = line.translate(str.maketrans("","",string.punctuation))
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1
rank = list(count.items())
rank = sorted(rank,reverse = True)
length = len(rank)
if length < 10:
    for (key,value) in rank:
        print(key,value)
else:
    counter = 0
    for (key,value) in rank:
        print(key,value)
        counter += 1
        if counter >= 10:
            break
