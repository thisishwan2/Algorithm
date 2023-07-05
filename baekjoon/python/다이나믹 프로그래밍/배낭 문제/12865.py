#12865 배낭 문제

# 핵심아이디어
# 1. 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.(이전의 최대를 가져옴)
# 2. 그렇지 않는다면, 다음 두가지중 고른다.
#   2.1 현재 넣을 물건의 무게만큼 배낭에서 빼고, 현재 물건을 넣는다.
#   2.2 현재 물건을 넣지 않고 이전 배낭 무게를 그대로 가져간다.

# 식으로 표현하면 i: 현재 담을 물건의 인덱스, j: 현재 허용용량, weight: 무게, value: 가치
# 1. j<weight => dp[i][j]=dp[i-1][j]
# 2. d[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)


import sys
input=sys.stdin.readline

n,k = map(int, input().split())

lst=[[0,0]]

for i in range(n):
    lst.append(list(map(int, input().split())))

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight=lst[i][0]
        value=lst[i][1]

        if weight>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][k])
               


