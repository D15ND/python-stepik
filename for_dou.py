total=0
a, b=int(input()), int(input())
for i in range(a, b+1): #nado b+1
    if ((a**3)%10==4 or (a**3)%10==9) or ((b**3)%10==4 or (b**3)%10==9):
        total=total+a+b
print(total)