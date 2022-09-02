m, n=int(input()), int(input())
for i in range(m, n+1):
    if i%10==9 or (i%3+i%5==0) or i%17==0:
        print(i)