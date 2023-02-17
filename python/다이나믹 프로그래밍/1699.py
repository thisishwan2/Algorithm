#1699
#최소 제곱합 항의 갯수

import sys
input=sys.stdin.readline

n=int(input())

dp=[0]*100001

for i in range(1, n+1):
    if int(i**0.5)==i**0.5:
        dp[i]=1
    else:
        min_value=1e9
        for j in range(1, int(i**0.5)+1):
            min_value=min(min_value, dp[i-j**2])
        dp[i]=min_value+1

print(dp[n])