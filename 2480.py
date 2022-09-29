import sys
a,b,c=map(int, sys.stdin.readline().split())

if a==b==c:
    print(10000+1000*a)
elif a==b or b==c:
    print(1000+100*b)
elif a==c:
    print(1000+100*c)

else:
    print(max(a,b,c)*100)