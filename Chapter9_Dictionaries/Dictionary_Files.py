# Dictionary & Files Page 118
inp = input("Please enter the file name:")
if inp == '':
    inp = 'romeo.txt'
try:
    fhand = open(inp)
except:
    print('Cannot open the file:',inp)
    quit()
word_dict = dict()
for line in fhand:
    line = line.split()
    for word in line:
        word_dict[word] = word_dict.get(word,0) + 1
print('1',word_dict)
for key in word_dict:
    print('2',key,word_dict[key])
word_list = list(word_dict.keys())
word_list.sort()
for word in word_list:
    print('3:',word,word_dict[word])
