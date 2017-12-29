# Exercise 6 Page 61
def computepay( hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 *rate
    else:
        pay = hours * rate
    return hours, rate, pay

inp_hours = input("Enter hours:\n")
inp_rate = input("Enter rate:\n")
try:
    inp_hours = float(inp_hours)
    inp_rate = float(inp_rate)
    (hours, rate, pay) = computepay(inp_hours, inp_rate)
    print("Pay is:",pay)
except:
    print("Error, please input numeric value!")
