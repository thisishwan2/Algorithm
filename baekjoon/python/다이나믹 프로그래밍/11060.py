#11060
#처음에 BFS 로 푸는데 너무 어려웠다. 찾아보니 DP로 푸는게 더 효율적이라고 한다.

#DP
import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

dp=[n+1]*n
dp[0]=0

for i in range(n):
    for j in range(1, arr[i]+1):
        if i+j<n:
            dp[i+j]=min(dp[i+j], dp[i]+1)
print(dp[n-1] if dp[n-1] != n+1 else -1)

#DFS
from collections import deque

n=int(sys.stdin.readline())
if n==1:
    print(0)
    exit()

a=list(map(int, sys.stdin.readline().split()))
#방문처리
visited=[0]*(n)


def bfs(start):
    q=deque()
    q.append((start, a[start]))

    while q:
        idx, jump =q.popleft()
        for i in range(1, jump+1):
            if i+idx>=n or visited[idx+i]:
                continue
            visited[idx+i]=visited[idx]+1
            q.append((idx+i, a[idx+i]))

bfs(0)
if visited[-1]:
    print(visited[-1])
else:
    print(-1)