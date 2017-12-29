#Note Chapter 5 Iteration
######################
##infinite loop1
#n = 0
#while True:
#    n += 1
#    print(n)
#print("Done")
##infinite loop2： use of 'break'
#while True:
#    line = input('Enter something: ')
#    if line == 'done':
#        break
#    print(line)
#print("Finished")
##infinite loop3: use of "continue"
#n=0
#while True:
#    line = input('>')
#    if line[0] == '#':
#        continue
#        print('#')
#    n += 1
#    print('Iteration',n)
#    if line == 'done' or line == 'Done':
#        break
#print("Finished")
# for loop1: the use of 'for' and 'in'
university = ['MIT','Stanford','UC Berkeley']
print(university)
for choice in university:
    print("Changhao will choose",choice)
print("finished!")
# for loop2 : maximum
largest = None
smallest = None
print("Largest Before:",largest)
print("Smallest Before:",smallest)
for iterval in [1,4,51,1, 213,3241]:
    if largest == None or iterval > largest:
        largest = iterval
    if smallest == None or iterval < smallest:
        smallest = iterval
    print("Loop:",iterval,largest)
    print("Loop:",iterval,smallest)
print("Largest:",largest)
print("Smallest:",smallest)
