# Page 102 count & average
# build-in functions
num = list() # num =[]
while True:
    inp = input('Please enter a number:')
    if inp == 'done':
        print('Done!')
        break
    try:
        inp = float(inp)
    except:
        print('Please enter numeric number!')
        quit()
    num.append(inp)
count = len(num)
total = sum(num)
print('Count:',count)
print('Sum:',total)
print('Average:',total/count)
