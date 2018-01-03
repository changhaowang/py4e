#S_E Chapter 11 Page 142
import re
inp = input("Please enter the filename: ")
if len(inp) < 1:
    inp = "mbox.txt"
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
    quit()
for line in fhand:
    line = line.strip()
    if re.search("^X-\S+: [0-9.]+",line):
        print(line)
    word = re.findall("X-\S+: ([0-9.]+)",line)
    if len(word) > 0:
        print(word)
    hour = re.findall("([0-9]+):[0-9]+:[0-9]+",line)
    if len(hour) > 0:
        print("Hour:",hour)
