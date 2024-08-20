from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])

    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and visited[i][j] == 0:

                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                cnt = int(maps[i][j])

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                            cnt += int(maps[nx][ny])
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                answer.append(cnt)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer