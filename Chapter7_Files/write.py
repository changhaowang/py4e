# writing the file
fout = open('output.txt','w') # attentaiton: if the file exists, this command will clear out all the old data and start to fresh
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land\n"
fout.write(line2)
fout.close()
fhand = open('output.txt','r')
#for line in fhand:
#    print(line)
inp = fhand.read()
print(inp)
