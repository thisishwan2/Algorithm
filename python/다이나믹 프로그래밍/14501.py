#14501


n=int(input())

table=[[]]
for i in range(n):
    table.append(list(map(int, input().split())))

dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i]=max(dp[i], table[i][1]) #미리 dp에 있는 값과 테이블값중 큰걸 대입
    for j in range(i+table[i][0], n+1):
        dp[j]=max(table[j][1]+dp[i], dp[j])

for i in range(n,0,-1):
    if not table[i][0]+i<=n+1:
        dp.pop(i)

print(max(dp))