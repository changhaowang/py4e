# List modify
#It's important to remember which methods modify the list or create a new one
def delete_head(t):
    del t[0]
def pop_head(t):
    t.pop(0)
def add_append(t1,t2):
    t1.append(t2)
def add(t1,t2):
    return t1 + t2
def delete_head_alternative(t):
    return t[1:]
letters = ['a',1,'b',2,'c',3]
delete_head(letters)
print(letters)
pop_head(letters)
print(letters)
letters_new = ['Another',1]
add_append(letters,letters_new)
print(letters)
letters_new_1 = add(letters,letters_new)
print('Another',letters_new_1)
letters_delete = delete_head_alternative(letters)
print('Delete head',letters_delete)
