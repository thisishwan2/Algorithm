#탐색으로 풀면 시간 초과

n,m=map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp=[[0 for _ in range(m)]for _ in range(n)]

dp[0][0]=graph[0][0]

for j in range(0,m-1):
    dp[0][j+1]=dp[0][j]+graph[0][j+1]

for j in range(0, n-1):
    dp[j+1][0]=dp[j][0]+graph[j+1][0]

# 1 3 6 10
# 1
# 10

for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=max(dp[i-1][j]+graph[i][j], dp[i][j-1]+graph[i][j])

print(dp[n-1][m-1])


"""
#탐색으로 풀면 시간 초과
from collections import deque

n,m=map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

candy=[[0 for _ in range(m)]for _ in range(n)]

dx=[1,0,1]
dy=[0,1,1]

def bfs():
    q=deque()
    q.append([0,0])
    candy[0][0]=graph[0][0]

    while q:
        x,y=q.popleft()
        for i in range(3):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                nex_candy=graph[nx][ny]+candy[x][y]
                if nex_candy>=candy[nx][ny]:
                    candy[nx][ny]=nex_candy
                    q.append([nx,ny])

bfs()
print(candy[n-1][m-1])
            

1000000은 단순히 숫자 크기만으로는 1초 안에 처리 가능한 양이라고 할 수 있습니다. 
하지만 이 문제에서는 입력 크기에 대한 정보가 그냥 하나만 주어지는 것이 아니라, 
그 크기에 따라 연산 횟수와 이에 따른 시간 복잡도가 달라지는 알고리즘이 사용되고 있습니다. 

"""