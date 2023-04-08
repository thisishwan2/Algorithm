#1965

import sys
input=sys.stdin.readline

n=int(input())
boxes=list(map(int, input().split()))

dp=[0]*1001

dp[boxes[0]]=1

for i in range(1,n):
    dp[boxes[i]]=1
    for j in range(boxes[i]-1,-1,-1):
        if dp[j]!=0:
            dp[boxes[i]]=max(dp[j]+1,dp[boxes[i]])
            
    
print(max(dp))

"""
최적화 풀이

n = int(input())
s = list(map(int, input().split()))
dp = []
dp.append(1)
for i in range(1, n):
    d = []
    for j in range(i):
        if s[i] > s[j]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))


"""