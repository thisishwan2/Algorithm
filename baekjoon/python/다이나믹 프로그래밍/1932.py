n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

dp=[[0 for _ in range(n)]for _ in range(n)]
dp[0][0]=graph[0][0]

#더할 수 있는 경우의 수는 한수를 지정하면 그 수의 인덱스, 인덱스+1이다. 따라서 두개다 구하고, DP배열에 기존에 값이 있으면 큰값을 저장한다.
for i in range(n-1):
    for j in range(len(graph[i])):
        dp[i+1][j]=max(dp[i][j]+graph[i+1][j], dp[i+1][j])
        dp[i+1][j+1]=max(dp[i][j]+graph[i+1][j+1], dp[i+1][j+1])
        
print(max(dp[n-1]))