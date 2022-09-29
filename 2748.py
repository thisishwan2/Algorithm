#생각보다 쉬웠지만 핵심 수학공식
#맞는데 런타임에러 난 풀이
from unittest import result


n=int(input())
f=[0,1]
for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
print(f[i])

#재귀를 이용한 풀이 재귀(자기자신을 호출) 이 풀이는 숫자가 커질수록 시간이 오래걸린다.
n=int(input())

def fibo(num):
    if num ==0:
        return 0
    elif num==2 or num==1:
        return 1

    return fibo(num-2)+fibo(num-1)

print(fibo(n))  #n번째 피보나치 수

#다이나믹 프로그래밍
n=int(input())
result=[0 for i in range(n+1)]          #0으로 이루어진 n개의 리스트
result[1]=1                             #1번째 리스트에 1값 대입

for i in range(2,n+1):                  
    result[i]=result[i-1]+result[i-2]   #피보나치로 이후 값들을 대입
   #result[2]=result[1]+result[0]
   #result[3]=result[2]+result[1]

print(result[-1])