from decimal import*
getcontext().prec = 6
a = float(input())
c=(a-32)*(5/9)
k= c +273.15
d= Decimal(c).normalize()
e= Decimal(k).normalize()
print(d, e)
