num=int(input())
a=num//100
b=(num//10)%10
c=num%10
x1=max(a, b, c)
x2=min(a, b, c)
x0=(a+b+c)-(x1+x2)
if (x1-x2)==x0:
    print("Число интересное")
else:
    print("Число неинтересное")