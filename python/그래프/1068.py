#1068

import sys
input = sys.stdin.readline

def dfs(v):
    tree[v] = -2 #삭제 처리.
    for i in range(n): #전체 트리 반복 
        if v == tree[i]: # tree[i]는 부모의 노드 번호이므로(즉 해당 인덱스 노드는 자식임), v랑 같으면 지워야한다.
            dfs(i) # i의 자식도 지움
            
n = int(input())
tree = list(map(int, input().split())) # [-1, 0, 0, 1, 1]
erase = int(input())

dfs(erase)
cnt = 0

for i in range(n):
    if tree[i] != -2 and i not in tree: #tree의 -2들이 지우는 노드이다. 그리고 tree에 i가 속해있지 않는다는 건. 리프 노드라는 뜻 왜냐면 tree는 연결된 부모 노드를 적는 것이기 때문.
        cnt+=1

print(cnt)