#Exercise 2 Chapter 11 Page 149
import re
fhand = open("mbox.txt")
num_list = list()
for line in fhand:
    if re.search("^New Revision:",line):
        num = re.findall(": ([0-9]+)",line)
        num_list.append(float(num[0]))
total = sum(num_list)
count = len(num_list)
average = total/count
print("Average:",average)
