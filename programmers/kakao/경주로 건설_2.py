from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 방향을 상태로 가지고 있어야 코너의 생성여부를 알 수 있음.
def solution(board):
    n = len(board)

    # 3차원 배열을 이용한다.
    visited = [[[1e9 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = 0
    visited[0][0][1] = 0
    visited[0][0][2] = 0
    visited[0][0][3] = 0
    q = deque()
    # x,y,dir, money
    q.append([0, 0, 1, 0])
    q.append([0, 0, 3, 0])

    money = []
    while q:
        x, y, dir, m = q.popleft()

        if (x, y) == (n - 1, n - 1):
            money.append(m)
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    if dir !=i and visited[nx][ny][i] > m+600:
                        q.append([nx, ny, i, m + 500 + 100])
                        visited[nx][ny][i] = m + 500 + 100
                    # 더 작은 돈을 들였다면
                    elif dir ==i and visited[nx][ny][i] > m+100:
                        q.append([nx, ny, dir, m + 100])
                        visited[nx][ny][dir] = m + 100
    money.sort()
    return money[0]

# solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])