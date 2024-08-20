# 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
# 3차원 배열로 푼다.
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    time = 0
    n = len(maps)
    m = len(maps[0])

    sx, sy = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j

    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([sx, sy, 0])

    while q:
        x, y, lever_info = q.popleft()

        # 레버를 당긴 뒤 도착점에 온 경우
        if (x, y) == (ex, ey) and lever_info == 1:
            time = visited[x][y][lever_info]
            print(visited[x][y][lever_info])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "X":
                    continue
                # 다음 칸이 레버이고, 방문한적 없는 경우
                if maps[nx][ny] == "L" and visited[nx][ny][1] == 0:
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])

                # 다음칸이 레버가 아닌 경우에
                elif maps[nx][ny] != "L":
                    # 아직 레버를 누르지 않은 경우
                    if visited[nx][ny][0] == 0 and lever_info == 0:
                        visited[nx][ny][0] = visited[x][y][0] + 1
                        q.append([nx, ny, 0])
                    # 레버를 누른 경우
                    elif visited[nx][ny][1] == 0 and lever_info == 1:
                        visited[nx][ny][1] = visited[x][y][1] + 1
                        q.append([nx, ny, 1])
    # print(*visited, sep = '\n')

    if time != 0:
        return time
    else:
        return -1