# use of split Page 104
fhand = open('/home/wang/Desktop/py4e/Chapter7_Files/mbox-short.txt')
for line in fhand:
    line = line.rstrip('\n')
    if not line.startswith('From'):
        continue
    word = line.split()
    try:
        print(word[2])
    except:
        print(word)
