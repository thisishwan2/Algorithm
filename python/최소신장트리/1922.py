#1922
# 크루스칼 알고리즘

import sys
input=sys.stdin.readline

n=int(input()) #컴퓨터 수
m=int(input()) #연결 선 수

# 부모테이블 초기화
parent =[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

# 부모찾기
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b= find_parent(parent, b)
    # 찾은 부모가 다르면
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


edges =[]
total_cost=0

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([c,a,b])

edges.sort()

for i in range(m):
    c,a,b=edges[i]
    # find 연산 후 부모노드기 다르면 사이클 발생 X이므로 union 연산 수행 -> 최소신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost+=c

print(total_cost)