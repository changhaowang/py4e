inp_hour=float(input('Enter the hour:'))
inp_rate=float(input('Enter the rate per hour:'))
if inp_hour > 40:
    inp_rate_new=1.5*inp_rate
    grosspay = inp_rate_new*(inp_hour-40)+40*inp_rate
else:
    grosspay=inp_hour*inp_rate
print('Grosspay is',grosspay)
