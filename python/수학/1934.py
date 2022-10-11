'''t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    result=1
    
    c=a*b
    if a==1 or b==1:
        print(c)
    else:
        for j in range(2,c):
            if c%j==0:
                result=result*j
                c=c//j
                if j>c:
                    break

        print(result)
'''
#위의 코드도 맞는 코드이다. 하지만 백준의 시간초과로 다른 풀이를 해보려고 한다.
#1번 접근법 두수의 최대 공약수를 구하고, 두수를 곱한 값을 최대 공약수로 나눔

#최소공배수(lcm), 최대공약수(gcd)
import sys
t=int(input())
for i in range(t):
    a,b=map(int, sys.stdin.readline().split())
    A,B=a,b
    while b!=0:
        a=a%b
        a,b=b,a
    gcd=a
    lcm=A*B//a
    print(lcm)
