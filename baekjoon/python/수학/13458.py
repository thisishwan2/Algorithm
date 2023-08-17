# 13458

import sys
input=sys.stdin.readline

n=int(input())
a = list(map(int,input().split())) # i번째 시험장 응시자수
b,c = map(int, input().split()) # 총 감독관이 한 시험장에서 감시 가능한 응시자 수, 부감독이 한 시험장에 감시 가능한 응시자 수

cnt=0

for i in a:
    left=i-b
    cnt+=1

    if left>0:
        if((left%c)==0): #나머지가 0 이라는 말은 나누어 떨어진다는 뜻
            cnt+=left//c
        else:
            cnt+=(left//c)+1

print(cnt)