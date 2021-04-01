#from decimal import *
#getcontext().prec = 4

km = input('How many kilometres? ')
if km.isnumeric():
    km = int(km)
    if km >= 0:
        miles = km * 0.6214
        print(miles)
        print(km, 'kilometres is', miles, 'miles')
