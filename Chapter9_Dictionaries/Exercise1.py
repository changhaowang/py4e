# Exercise 1 Chapter 9 Page 116
fhand = open('words.txt')
word = fhand.read()
list_string = word.split()
length = len(list_string)
word_dic = dict()
for i in range(length):
    word_dic[list_string[i]] = None
while True:
    inp = input('Enter a string to check it whether is in the txt file: ')
    if inp == 'done':
        break
    print(inp in word_dic)
