# #11055

#정답
n=int(input())
lst=list(map(int, input().split()))

dp=[0]*n
dp[0]=lst[0]
for i in range(1,n):
    for j in range(i): 
        if lst[i]>lst[j]:
            dp[i]=max(dp[i],dp[j]+lst[i])
        else:
            dp[i]=max(dp[i],lst[i])

print(max(dp))


# 최적화 풀이
n = int(input())
li = list(map(int, input().split()))
dp = [0]*1001
for i in range(n):
    temp = li[i]
    dp[temp] = max(dp[0:temp])+temp
print(max(dp))