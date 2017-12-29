# Exericise 2 Chapter 9 Page 124
inp = input("Please enter the file:")
default = 'mbox.txt'
if inp == '':
    inp = default
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
    quit()
count = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    length = len(words)
    if line.startswith("From") and length > 2:
        count[words[2]] = count.get(words[2],0) + 1
print(count)
