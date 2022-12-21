#17471
#삼성 코테 기출

#구역을 두 개의 선거구로 나눠야한다.
#선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
#두 선거구에 포함된 인구의 차이를 최소

#접근법: 선거구 두개에 부여되는 모든 지역의 경우의 수에 대해 진행함.(브루트포스) 각각의 선거루에 해당하는 지역을 설정했으면, 인접한지에 대한 BFS 실행.


#첫번째 풀이
#조합을 이용
import sys
input=sys.stdin.readline
from collections import deque
import itertools

n=int(input())
#구역의 인구수 1번부터
people=list(map(int, input().split()))

graph=[[]for _ in range(n)]

for i in range(n):
    #인접한 구역수, 인전합 구역의 번호 ....
    area=list(map(int, input().split()))
    for j in range(1,area[0]+1):
        graph[i].append(area[j]-1) #1을 빼는 이유는 문제는 1번부터 시작이지만, 나의 노드는 0번 부터 시작이기 때문.

def bfs(node):
    visit=[0 for i in range(n)]
    start=node[0]
    q=deque()
    q.append(start)
    visit[start]=1
    total=0

    while q:
        v=q.popleft()
        total+=people[v]
        for i in graph[v]:
            if visit[i]==0 and i in node:
                q.append(i)
                visit[i]=1
    
    cnt=visit.count(1)

    return total, cnt


#max값 혹은 무수히 큰 값으로 잡는 이유는 n<=10, 인구수<=100 이므로 그냥 큰값을 넣는것이 안전.
min_ans=sys.maxsize

for i in range(1, n//2+1):
    combis=list(itertools.combinations(range(n),i))
    for combi in combis:
        sum1, v1=bfs(combi)
        sum2, v2=bfs([i for i in range(n) if i not in combi])
        if v1+v2 ==n:
            min_ans=min(min_ans,abs(sum1-sum2))

if min_ans==sys.maxsize:
    print(-1)
else:
    print(min_ans)

#두번째 풀이
#조합대신 DFS로 선거구에 지역을 부여함.
import sys
input=sys.stdin.readline
from collections import deque

#연결정보
def bfs(g):
    q=deque()
    #방문처리
    check=[0 for _ in range(n)]
    q.append(g[0])
    check[g[0]] = 1
    cnt, ans = 1,0 #cnt= ,ans= 인구 수
    while q:
        x=q.popleft()
        ans+=people[x]
        #꺼낸 x에 인접한 노드를 nx넣음.
        for nx in graph[x]:
            #인접한 노드가 선거구 안에 있고, 방문을 안했으면
            if nx in g and not check[nx]:
                check[nx]=1
                cnt+=1
                q.append(nx)
    if cnt==len(g):
        return ans
    else:
        return 0

#선거구를 두개로 나누는 과정(cnt=하나의 선거구안에 넣은 지역 수, end=)
def dfs(cnt, x, end):
    global min_ans
    if cnt==end:
        g1, g2=deque(), deque()
        for i in range(n):
            if visited[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1)
        if not ans1:
            return
        ans2 = bfs(g2)
        if not ans2:
            return
        min_ans=min(min_ans, abs(ans2-ans1))
        return
    

    for i in range(x,n):
        if visited[i]:
            continue
        visited[i]=1
        dfs(cnt+1, i, end)
        visited[i]=0




n=int(input())
#구역의 인구수 1번부터
people=list(map(int, input().split()))

graph=[[]for _ in range(n)]

for i in range(n):
    #인접한 구역수, 인전합 구역의 번호 ....
    area=list(map(int, input().split()))
    for j in range(1,area[0]+1):
        graph[i].append(area[j]-1) #1을 빼는 이유는 문제는 1번부터 시작이지만, 나의 노드는 0번 부터 시작이기 때문.

min_ans=sys.maxsize
for i in range(1, n//2+1): #1번 선거구, 2번 선거구가 있다고 할때 i=1이면 1번 선거구에 1지역, 2번 선거구에 2,3,4,5,6지역 i=2이면 1번 선거구에 1,2지역 2번 선거구에 3,4,5,6 지역 같이 
                           # 즉, (1,5), (2,4), (3,3) 처럼 선거구 조합을 한다.
    visited=[0 for _ in range(n)]
    dfs(0,0,i)


if min_ans==sys.maxsize:
    print(-1)
else:
    print(min_ans)