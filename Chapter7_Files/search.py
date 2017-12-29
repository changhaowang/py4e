# Serach in the file
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    count = 0
# count the number of the lines which start with "From"
#for line in fhand:
#    line = line.strip('\n') #Strip the newline symbol
#    if not line.startswith('From'):
#        continue
#    print(line)
#print(fhand)
# count the number of the lines, which contains "@uct.ac.za"
#for line in fhand:
#    line = line.rstrip()
#    print(line)
#    if line.find('@uct.ac.za') == -1:
#        continue
#    print(line)
# enter the filename by myself and count the number of the lines which starts with "Subject"
    for line in fhand:
        if line.startswith('Subject:'):
            count += 1
    print("There are",count,"Subject lines in",fname)
except:
    print("The file",fname,"doesn't exixt!")
