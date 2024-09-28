n,k = map(int, input().split())

coins = set()
for i in range(n):
    coins.add(int(input()))

coins = list(coins)
coins = sorted(coins)

dp = [1e9]*(k+1)
dp[0]=0

# n가지의 코인에 대해 k번을 다 돈다
for coin in coins:
    for i in range(coin,k+1):
        dp[i]=min(dp[i-coin]+1, dp[i])

if dp[k]==1e9:
    print(-1)
else:
    print(dp[k])
'''

인덱스
1 2 3 4 5 6 7 

값
1,2,3,4,1,

6은 dp[5]+dp[1] = 2
7은 dp[5]+dp[2] = 3


'''