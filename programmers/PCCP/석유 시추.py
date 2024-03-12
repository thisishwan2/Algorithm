# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, land, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


def solution(land):
    answer = 0

    for j in range(len(land[0])):  # 열
        tmp = 0
        visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
        for i in range(len(land)):  # 행
            if land[i][j] == 1 and visited[i][j] == 0:
                tmp += bfs(i, j, land, visited)
        answer = max(tmp, answer)

    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))