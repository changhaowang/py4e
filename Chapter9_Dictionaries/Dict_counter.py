# Dictionary as a set of counter
inp = input('Enter what you want:')
#length = len(inp)
inp_dict = dict()
# First way:
for word in inp:
    if word not in inp_dict:
        inp_dict[word] = 1
    else:
        inp_dict[word] += 1
print('Output of the first method:',inp_dict)
# Alternative way by using get()
inp_dict_new = dict()
for word in inp:
    inp_dict_new[word] = inp_dict_new.get(word,0) + 1
print("Output of the get() method",inp_dict_new)
print('Is the two Outputs are the same?',inp_dict == inp_dict_new)
