a, b, c=str(input()), str(input()), str(input())
a1=len(a)
b1=len(b)
c1=len(c)
m1=min(a1, b1, c1)
m2=max(a1, b1, c1)
if a1==m1:
    print(a)
elif b1==m1:
    print(b)
elif c1==m1:
    print(c)
if a1==m2:
    print(a)
elif b1==m2:
    print(b)
elif c1==m2:
    print(c)