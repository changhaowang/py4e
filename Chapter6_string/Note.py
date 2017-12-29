# Note Chapter 6
## Exercise1 for Traversal while loop Page 75
#inp = input('Enter a string: ')
#length = len(inp)
#index = -length
#while index < 0:
#    print(inp[index])
#    index +=1
#print("finished")
# Exercise2 for counter Page 76
#import numpy as np
def count(word,string):
    length = len(string)
    #counter = np.zero(i,1)
    counter = 0
    for letter in word:
        if letter == string:
            counter +=1
    return counter
word = input('Enter some words: ')
string = input('Specifc strings you want to count: ')
counter = count(word,string)
print(counter)
#Exercise 4 Page 79
word = 'banana'
num_a = word.count('a')
print(num_a)
# Parsing strings Page 80
data = 'From stephen.marquard@ uct.ac.za Sat Jan  5 09:14:16 2008'
start = data.find('@') + 2
end = data.find('S',start) - 1 # attention: in Python, [m,n] is from m to n-1!!!!!! 
main = data[start:end]
print(main)
