# Exercise 1 Chapter 10 Page 135
inp = input("Please enter the filename: ")
if len(inp)<1:
    inp = 'mbox.txt'
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
    quit()
count_dict = dict()
for line in fhand:
    words = line.split()
    length = len(words)
    if line.startswith("From") and length > 1:
        count_dict[words[1]] = count_dict.get(words[1],0) + 1
#print(count_dict)
#Find the most commits
count_list = list()
for (key,value) in list(count_dict.items()):
    count_list.append((value,key))
count_list.sort(reverse = True)
print('The person has the most commits is',count_list[0][1],'who has',count_list[0][0],'commits')
