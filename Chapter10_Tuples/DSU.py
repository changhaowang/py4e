# DSU Chapter 10 Tuples Page 127
# Sort the words from the longest to shortest
inp = input("Please enter some words: ")
if len(inp)<1:
    inp = 'but soft what light in yonder window breaks'
words = inp.split()
t = list()
for word in words:
    t.append((len(word),word))
try:
    t.sort(reverse = True)
except:
    print('Please enter the word in type str!')
    quit()
res = list()
for length,word in t:
    res.append(word)
print(res)
