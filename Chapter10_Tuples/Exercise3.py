#Exercise 3 Chapter 10 Page 136
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
    line = line.strip()
    line = line.lower()
    line = line.translate(str.maketrans("","",string.punctuation+' 1234567890'+'\n\t'))
    words = list(line)
    for word in words:
        count[word] = count.get(word,0) + 1
count_list = list(count.items())
count_list.sort()
for (key,value) in count_list:
    print(key,value)
