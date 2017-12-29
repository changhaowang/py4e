# Exercise 2 Page 95
fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('Cannot open the file:',fname)
    quit()
count = 0
total = 0
for line in fhand:
    if line.find("X-DSPAM-Confidence:") != -1:
        count += 1
        start = line.find(":")
        total += float(line[start+1:])
        print(line[start+1:])
print("finished!")
print('Average:',total/count)
