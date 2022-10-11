import math
import sys

m,n=map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    error=0
    for j in range(2,int(i**1/2)+1):
        if i%j==0:
            error=1
            break
    if i != 1 and error==0:
        print(i)

#에라토스테네스의 체 기억하기.
'''
에라토스테네스의 체란 소수를 판별하는 알고리즘.

m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)

'''