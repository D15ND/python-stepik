import math
from math import *
a, b, c=float(input()), float(input()), float(input())
a!=0
# (a*(x**2)+b*x+c)==0
D=(b**2)-(4*a*c)
if D>0:
    x1=((-b+((D)**0.5))/(2*a))  #x1=((-b+sqrt(D))/(2*a))
    x2=((-b-((D)**0.5))/(2*a))  #x2=((-b-sqrt(D))/(2*a))
    print(min(x1, x2))
    print(max(x1, x2))
elif D==0:
    x1=(-b/(2*a))
    print(x1)
else:
    print("Нет корней")