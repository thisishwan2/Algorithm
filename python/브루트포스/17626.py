'''import math
import sys

n= int(sys.stdin.readline())

max_range=math.trunc(round(n**0.5))
#####여기까지는 고정 풀이 인듯##및에서 시간을 줄여야함.
#아래가 맞는 풀이긴 한데 시간이 너무 걸림, 
lst=[]

# 제곱수가 1일때
if n%(n**0.5)==0:
    lst.append(1)

#15663의 제곱근은 125, 11339의 제곱근은 106.4 이다. 즉, 우리는 큰수부터 없애는 접근 을 하면됨.
#최소 개주 제곱수 개수는 4개이하여야함.

for i in range(max_range, 0, -1):
    m=n-i**2
    new_max_range=math.trunc(round(m**0.5))
    for j in range(new_max_range,0,-1):
        if i**2+j**2==n:
            lst.append(2)
            break
        m=m-j**2
        new_max_range=math.trunc(round(m**0.5))
        for k in range(new_max_range, 0, -1):
            if i**2+j**2+k**2==n:
                lst.append(3)
                break
            m=m-k**2
            new_max_range=math.trunc(round(m**0.5))
            for l in range(new_max_range, 0, -1):
                if i**2+j**2+k**2+l**2==n:
                    lst.append(4)
                    break

print(min(lst))

#이러헥 하면 1**2+1**2 표현이 문제가 생김.
'''

#첫번째 풀이.
# 제곱근이 정수라면? 이라는 조건으로 문제를 푼다.

import sys 

n=int(sys.stdin.readline())

def sol(n):
    #n의 제곱근의 정수랑 n의 제곱근의 값이 같다면 1
    if int(n**0.5)==n**0.5:
        return 1    #ex) 25=5**2, 4=2**2
    
    #1~(n제곱근의 올림값(int()연산을 하면 소수점은 버림)을 i라고 하고 (n-i**2)의 제곱근이 정수와 같다면 2)
    for i in range(1, int(n**0.5)+1):
        if int((n-i**2)**0.5)==(n-i**2)**0.5:
            return 2
    
    #(n-i**2-j**2)의 제곱근이 정수라면 답은 3
    for i in range(1, int(n**0.5)+1):
        for j in range(1, int((n-i**2)**0.5)+1):
            if int((n-i**2-j**2)**0.5)==(n-i**2-j**2)**0.5:
                return 3
    
    #그 외의 경우는 문제에 명시되었다 싶이 4개
    return 4

print(sol(n))

'''
dp 풀이법. 다시보기
import sys


n = int(sys.stdin.readline())
dp = [0, 1]

# 반복문을 통해 합이 n번째까지 제곱수들의 최소 개수를 구함.
for i in range(2, n + 1):
    target = 1e9

    # 반복문을 통해 최대 50000의 제곱을 확인
    for j in range(1, 50001):

        # 현재 수의 제곱이 i보다 크다면 멈춘다. i를 구하기 위함이므로
        if j ** 2 > i:
            break

        # n보다 작거나 같은 제곱수를 찾고 n-제곱수를 인덱스로 가진 값에 1을 더해주면 된다.
        target = min(target, dp[i - (j**2)])

    dp.append(target + 1)

print(dp[n])
'''