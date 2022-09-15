a1,b1=map(int, input().split())
a2,b2=map(int, input().split())
a3,b3=map(int, input().split())

if a1==a2:
    a4=a3
elif a1==a3:
    a4=a2
else:
    a4=a1

if b1==b2:
    b4=b3
elif b1==b3:
    b4=b2
else:
    b4=b1

print(a4,b4)