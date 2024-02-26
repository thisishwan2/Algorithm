# 1차 시도 시간복잡도 문제
# 그 이유는 인접 행렬 즉, n*n 행렬을 만들어서 탐색하기 때문에 n^2시간이 걸림
def solution(n, edge):
    lst = [[0 for i in range(n + 1)] for _ in range(n + 1)]

    for i in edge:
        a = i[0]
        b = i[1]
        lst[a][b] = 1
        lst[b][a] = 1

    visited = [0] * (n + 1)
    depth = 1
    dic = {}  # 뎁스별로 노드가 담긴 딕셔너리
    for i in range(n):
        dic[i] = []

    visited[1] = 1
    for i in range(len(lst[1])):
        if lst[1][i] == 1:
            dic[1].append(i)
            visited[i] = 1

    while visited.count(1) != n:
        for i in dic[depth]:
            for j in range(len(lst[i])):
                if visited[j] == 0 and lst[i][j] == 1:
                    dic[depth + 1].append(j)
                    visited[j] = 1
        depth += 1

    answer = len(dic[depth])
    return answer

# 2차 시도 통과
# 2차원 인접 행렬에서 인접 리스트로 변경, 또한 BFS 방식을 이용해서 시간복잡도를 줄임 즉 O(n+e)
from collections import deque

def solution(n, edge):
    lst = [[] for _ in range(n + 1)]

    for i in edge:
        a = i[0]
        b = i[1]

        lst[a].append(b)
        lst[b].append(a)

    print(lst)

    visited = [0] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        ans = []
        for j in range(len(q)):
            idx = q.popleft()
            ans.append(idx)
            for i in lst[idx]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
    return len(ans)
