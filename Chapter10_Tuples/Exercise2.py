#Exercise 2 Chapter 10 Page 135
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
    words = line.split()
    length = len(words)
    if line.startswith("From") and length > 5:
        words = words[5].split(':')
        count[words[0]] = count.get(words[0],0) + 1
for (key,value) in list(count.items()):
    print("Hour:",key,"Times:",value)
