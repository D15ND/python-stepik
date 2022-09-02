from xml.etree.ElementTree import XML


a, b, c=int(input()), int(input()), int(input())
x=b+c
if a<b+c and b<a+c and c<a+b:
    print("YES")
else:
    print("NO")
