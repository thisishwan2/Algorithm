#2156
#2579 계단오르기와 똑같은 로직
import sys
input = sys.stdin.readline
n=int(input())
grape=[0]

for i in range(n):
    grape.append(int(input()))

dp=[0]
dp.append(grape[1])
if n>1:
    dp.append(grape[1]+grape[2])

for i in range(3,n+1):
    dp[i]=max(dp[i-2]+grape[i], dp[i-1], dp[i-3]+grape[i-1]+grape[i])
print(dp[n-1])