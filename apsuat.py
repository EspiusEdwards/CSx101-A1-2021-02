from decimal import*
getcontext().prec = 6
a = float(input())
b= a*(0.453592/2.54**2)
print(Decimal(b).normalize())
