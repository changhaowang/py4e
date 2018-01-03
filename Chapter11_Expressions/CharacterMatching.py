# Character matching of Chaper 11 Regular Expression Page 137
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if re.search("From",line):
        print('Method 1:',line)
    if re.search("^From",line):  # Only from the begining
        print("Method 2:",line)
    if re.search("^F...m",line):  # Do not match From particularly
        print("Method 3:",line)
    if re.search("^F.+@",line):
        print("Method 4:",line)
    if re.search("^F.*@",line):   #*: zeor to any number note it will match the last @ sign
        print("Method 5:",line)
