# Exercise 3 Chapter 9 Page 124
inp = input("Please enter the filename:")
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
    if line.startswith("From") and length > 1:
        count[words[1]] = count.get(words[1],0) + 1
# order the dict
# Now I cannot find any efficient methods to do that(build-in function?)
