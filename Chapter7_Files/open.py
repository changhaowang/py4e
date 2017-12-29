#open the file: mbox.txt
fhand = open('mbox.txt')
count = 0
for line in fhand: # Python open the file line by line
    count += 1
    if count == 1 or count == 2:
        print(line)
print("Line Count",count)
