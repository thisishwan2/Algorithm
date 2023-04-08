#17135
#새로 알게된점 삼성 코테는 itertools를 사용 못하므로 조합을 직접 구현해야한다.

#문제 접근법
# 궁수는 가까운 적을 쏜다.(동시에 쏜다고 생각)
# 만약 여러 굴수가 같은 적을 쏜다면, 적은 한명만 죽고, 궁수 두명은 쏜게 된다.(이 부분이 중요)
# 그렇게 적을 한턴 죽이면, 그래프를 한줄씩 내리고, 이를 반복.

import sys
input=sys.stdin.readline
import copy
from collections import deque


# d거리 안에 가장 가까운 적을 찾는다.
def bfs(x,y,length):
    q=deque()
    q.append([x,y,length])
    visited=[[0 for _ in range(m)] for _ in range(n+1)] #궁수의 위치까지 포함한 방문처리 리스트
    visited[x][y]=1
    attack=[] # 공격 가능한 적의 (거리, y좌표, x좌표)를 담을 리스트

    while q:
        x,y,length=q.popleft()

        # 그래프의 해당 위치에 적이 있고, 공격가능 거리안에 있을 때
        if temp[x][y]==1 and length<=d:
            attack.append([length, y, x]) #정렬 조건에 따라 attack리스트에 추가
            continue
        
        for i in range(3):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 다음 장소가 방문하지 않았고, 공격 가능 거리안에 있을 떄
                if visited[nx][ny]==0 and length<=d:
                    q.append([nx,ny,length+1])
                    visited[nx][ny]=1
    
    # 정렬해서 반환
    return sorted(attack)

# 적이 아래로 한칸 씩 이동
def graph_move():
    #n번째 행은 궁수 행이므로 n-1행부터 1번 행까지
    for i in range(n-1, 0, -1):
        for j in range(m):
            temp[i][j]=temp[i-1][j]
    # 맨 윗줄에 빈칸 추가
    for i in range(m):
        temp[0][i]=0


# 적의 존재 여부( while 문을 종료하기 위한 조건)
def is_empty():
    for i in range(n):
        for j in range(m):
            if temp[i][j]==1:
                return False
    return True

# 조합 구현(yield 활용)
def combinations(array, r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]]+next


n,m,d=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
append_graph=[-1 for _ in range(m)]
graph.insert(n,append_graph) #마지막 줄에 궁수들 위치를 잡을 수 있도록 한줄 추가

#아래는 볼 필요 없다.(궁수 입장에서 탐색하기 때문에)
dx=[-1,0,0]
dy=[0,-1,1]

# 조합을 구할 리스트
items=[i for i in range(m)]
result=0

for a in combinations(items, 3):
    temp = copy.deepcopy(graph) # 기존 그래프는 불변해야하므로, 깊은 복사
    count=0 #죽인 적 수

    while not is_empty():
        position=[] #적 좌표 넣을 리스트
        for i in range(3):
            target_enemy=bfs(n,a[i],0)
            if len(target_enemy)!=0:
                target_enemy=target_enemy[0] # 가장 첫번째 인자를 뽑아옴(가장 가깝고, 왼쪽의 적)
                position.append((target_enemy[2],target_enemy[1]))
        
        #중복 제거
        position=list(set(position))

        for i in position:
            temp[i[0]][i[1]]=0
            count+=1
        
        graph_move()
    result=max(result,count)
print(result)