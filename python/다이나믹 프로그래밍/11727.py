#11727
#규칙: n이 홀수에서 짝수로 넘어갈때는 *2+1 을 하고, 짝수에서 홀수로 넘어갈때는 *2-1 이다.

n=int(input())

dp=[0]*(n+1)
dp[1]=1

for i in range(2,n+1):
    if i%2==0:
        dp[i]=dp[i-1]*2+1
    else:
        dp[i]=dp[i-1]*2-1
print(dp[n]%10007)