from collections import deque


def solution(n, m, hole):
    tmp = n
    n = m
    m = tmp
    # print(n,m)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    board = [[0 for _ in range(m)] for _ in range(n)]
    for a, b in hole:
        board[b - 1][a - 1] = 1
    # print(*board, sep="\n")

    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0, 0, False, 0])  # x,y,점프 사용 여부, 시간
    visited[0][0][0] = 1
    visited[0][0][1] = 1

    while q:
        x, y, jump_info, time = q.popleft()

        if (x, y) == (n - 1, m - 1):
            return time

        if jump_info == False:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                n2x = x + dx[i] * 2
                n2y = y + dy[i] * 2

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][0] == 0 and board[nx][ny] == 0:
                    q.append([nx, ny, False, time + 1])
                    visited[nx][ny][0]=1
                if 0 <= n2x < n and 0 <= n2y < m and visited[n2x][n2y][1] == 0 and board[n2x][n2y] == 0:
                    q.append([n2x, n2y, True, time + 1])
                    visited[n2x][n2y][1] = 1
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][1] == 0 and board[nx][ny] == 0:
                    q.append([nx, ny, True, time + 1])
                    visited[nx][ny][1]=1

    return -1


print(solution(4,	4,	[[2, 3], [3, 3]]))
print(solution(5,	4,	[[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))