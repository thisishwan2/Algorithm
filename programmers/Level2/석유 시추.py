# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, land, visited, res):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1
    min_y, max_y = y,y

    while q:
        x, y = q.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1

    for i in range(min_y, max_y+1):
        res[i] += cnt

    return res


def solution(land):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    arr = []

    n = len(land)
    m = len(land[0])

    res = [0 for i in range(m+1)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                res = bfs(i, j,land,visited,res)

    return max(res)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))



# 다른 풀이
# 수직으로 뚫을때, 가장 많은 석유를 뽑는 시추관의 위치를 구한다.
#  발견된 석유의 상하좌우로 연결된 석유는 하나의 덩어리이다.
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(land):
    n = len(land)
    m = len(land[0])
    area_num = 0
    oil_dict = {}
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                area_num += 1
                amount = 0
                q = deque()
                q.append([i, j])
                visited[i][j] = area_num

                while q:
                    x, y = q.popleft()
                    amount += 1
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]

                        if 0 <= nx < n and 0 <= ny < m:
                            if visited[nx][ny] == 0 and land[nx][ny] == 1:
                                q.append([nx, ny])
                                visited[nx][ny] = area_num

                oil_dict[area_num] = amount
    # print(*visited, sep='\n')
    result = 0
    for j in range(m):
        visit_area = set()
        answer = 0
        for i in range(n):
            if land[i][j] == 1 and visited[i][j] not in visit_area:
                answer += oil_dict[visited[i][j]]
                visit_area.add(visited[i][j])

        result = max(result, answer)

    # print(result)
    return result
# print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
#                 [1, 1, 1, 0, 0, 0, 1, 1]]))