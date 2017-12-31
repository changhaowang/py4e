#Count words Chapter 10 Page 131
import string
inp = input("Please enter the filename: ")
if len(inp) < 1:
    inp = 'romeo-full.txt'
try:
    fhand = open(inp)
except:
    print("Cannot open the file:",inp)
    quit()
count_dict = dict()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        count_dict[word] = count_dict.get(word,0) + 1
count_list = list()
for (key,value) in list(count_dict.items()):
    count_list.append((value,key))
count_list.sort(reverse = True)
print('The most common word is',count_list[0][1],"It appears",count_list[0][0],'times')
