#Exercise 1 & Exercise 2 Page 71
total = 0
count = 0
largest = None
smallest = None
while True:
    inp_num = input("Enter a number: ")
    if inp_num == 'done':
        break
    else:
        try:
            inp_num = float(inp_num)
            count +=1
            total +=inp_num
            if largest == None or inp_num > largest:  # Exercise 2
                largest = inp_num
            if smallest == None or inp_num < smallest: # Exercise 2
                smallest = inp_num
        except:
            print("Invalid input")
print(total,count,total/count )
print(largest,smallest)
