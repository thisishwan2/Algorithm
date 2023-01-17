a=int(input())
lst=list(map(int, input().split()))

dp=[0]*a

for i in range(a):
    dp[i]=1
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i]=max(dp[j]+1, dp[i])

print(max(dp))

"-----------------------------------------"
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))