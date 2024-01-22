from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, maps):
    q = deque()
    q.append([x, y])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny]==1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y]+1
    return visited


def solution(maps):
    visit = bfs(0, 0, maps)
    answer = visit[len(maps) - 1][len(maps[0]) - 1]

    if answer == 0:
        answer = -1
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))