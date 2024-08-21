from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    visited = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    rx, ry = 0, 0
    ex, ey = 0, 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                rx, ry = i, j
            elif board[i][j] == "G":
                ex, ey = i, j

    q = deque()
    q.append([rx, ry, 0])

    # R의 위치를 재방문 할 수 있음.
    # visited[rx][ry][0] = 1
    # visited[rx][ry][1] = 1
    # visited[rx][ry][2] = 1
    # visited[rx][ry][3] = 1

    while q:
        x, y, cnt = q.popleft()

        if (x, y) == (ex, ey):
            return cnt

        for i in range(4):
            flag = False
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D" and visited[nx][ny][i] == 0:
                visited[nx][ny][i] = 1
                nx = nx + dx[i]
                ny = ny + dy[i]
                flag = True
            if flag:
                q.append([nx - dx[i], ny - dy[i], cnt + 1])
        # print(*visited, sep='\n')
    return -1
# print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	))