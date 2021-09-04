import math
from decimal import Decimal
a,b,c = map(int,input().split())
x = a**5 - 2*math.sqrt(abs(b)) + a*b*c
y= Decimal(x).quantize(Decimal('1.00'))
print(y)
