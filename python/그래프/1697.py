#1697
#비교적 쉬웠다.
import sys
input=sys.stdin.readline
from collections import deque

def bfs(start):
    
    dx=[-1, 1, 2]
    q=deque()
    q.append(start)
    visited[start]=1

    while q:
        x=q.popleft()
        if x==k:
            break
        for i in range(3):
            
            if i==2:
                new_x=dx[2]*x
                if 0<=new_x<=100000:
                    if visited[new_x]==0:
                        q.append(new_x)
                        visited[new_x]=1
                        cnt[new_x]=cnt[x]+1
            else:
                new_x=x+dx[i]
                if 0<=new_x<=100000:
                    if visited[new_x]==0:
                        q.append(new_x)
                        visited[new_x]=1
                        cnt[new_x]=cnt[x]+1


n, k =map(int, input().split())
visited=[0]*100001
cnt=[0]*100001
bfs(n)
print(cnt[k])
'''
깔끔한 풀이


from collections import deque

def bfs():
    q = deque()             # deque는 양쪽에서 입출력 가능
    q.append(n)             # q = deque([5])
    while  q:
        x = q.popleft()     # 처음 시작점은 x = 5, q = deque([])
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):    # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)    # q = deque([4, 6, "10"])

MAX = 10 ** 5               # 시간초과 안나게 수 제한
dist = [0] * (MAX + 1)      # 이동하는 거리를 알기 위한 변수
n, k = map(int, input().split())

bfs()

'''