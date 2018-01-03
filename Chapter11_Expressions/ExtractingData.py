#Extract data Chapter 11 Page 139
import re
s = 'A message from csevA@umich.edu to cwen@inpui.edu about meeting @2PM'
lst_greedy = re.findall("\S+@\S*",s) #?RETURNS THE SHORTEST ONE
print(type(lst_greedy))
print("Greedy",lst_greedy)
lst = re.findall("\S+@\S+?",s)
print("Non-greedy",lst)

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
    words = re.findall("[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]",line)
    length = len(words)
    if length > 0:
        print(words)
