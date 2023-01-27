#2193

#1로 시작하고, 1이 연속 두번 나타나지 않는다.
#0,1이 붙는 규칙을 찾으려고 하지말고, 나열했을 때 어떤 갯수로 늘어나는지에 주목

n=int(input())

dp=[0]*91

if n==1:
    print(1)
if n>=2:
    dp[1]=1
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n])