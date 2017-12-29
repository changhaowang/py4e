inp_hour=(input('Enter the hour:'))
inp_rate=(input('Enter the rate per hour:'))
try:
    inp_hour=float(inp_hour)
    inp_rate=float(inp_rate)
    if inp_hour > 40:
        inp_rate_new=1.5*inp_rate
        grosspay = inp_rate_new*(inp_hour-40)+40*inp_rate
        print('Grosspay is',grosspay)
    else:
        grosspay=inp_hour*inp_rate
        print('Grosspay is',grosspay)
except:
    print('Error, please enter numeric input!')
