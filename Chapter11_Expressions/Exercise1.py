# Exercise 1 Chapter 11 Page 149
import re
inp = input("Enter a regular expression: ")
if len(inp) < 1:
    inp = '^From:'
fhand = open("mbox.txt")
count = 0
for line in fhand:
    line = line.strip()
    words = re.findall(inp,line)
    if len(words) > 0:
        count += 1
print("mbox.txt had",count,"lines that matched",inp)
