#2579
#중요한 점.
# 1. 마지막 계단의 전 계단을 밟은 경우와(=마지막 계단+ 전 계단+ 전전전 계단 을 밟는 경우)
# 2. 마지막 계단의 전 계단을 밟지 않은 경우가 있다.(=마지막 계단 + 전전 계단)
#이 아이디어가 -> dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

n=int(input())
stairs=[]
for _ in range(n):
    stairs.append(int(input()))

dp=[0]*n

if n==1:
    print(stairs[0])
elif n==2:
    print(stairs[0]+stairs[1])
elif n==3:
    print(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
else:
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n):
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[n-1])

