# 1) DFS or BFS 를 이용하여 좌표탐색을 한다 - 조각 모음을 좌표로 저장한다
# 2) 받은 좌표들을 사각형 형태로 가공한다.
# 3) 사각형 형태의 가공물들을 90도 회전하는 함수를 만든다.
# 4) 비교 및 검사

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

table_snippets = []
visited = []


def table_bfs(new_table, table, x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    new_table[x][y] = 1
    n = len(table)
    m = len(table[0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if table[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    new_table[nx][ny] = 1
                    q.append([nx, ny])

    new_table = del_row(new_table)
    new_table = spin_90(new_table)
    new_table = del_row(new_table)
    return new_table


def table_append(table, res):
    for i in range(3):
        table = spin_90(table)
        res.append(table)

    return res


def spin_90(table):
    n = len(table)
    m = len(table[0])
    new_table = [[0 for _ in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            row = i
            col = j
            new_row = col
            new_col = n - row - 1
            new_table[new_row][new_col] = table[row][col]
    return new_table


def del_row(table):
    new_table = []
    for i, val in enumerate(table):
        if sum(val) != 0:
            new_table.append(table[i])

    return new_table


def make_x_y_arr(table):
    x = len(table)
    y = len(table[0])

    arr = [[0 for _ in range(y)] for _ in range(x)]

    for i in range(x):
        for j in range(y):
            arr[i][j] = table[i][j]

    return arr


def matching(new_table, game_board, x, y, table_snippets, visited):
    block_cnt = 1

    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    new_table[x][y] = 1
    n = len(game_board)
    m = len(game_board[0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if game_board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    new_table[nx][ny] = 1
                    q.append([nx, ny])
                    block_cnt += 1

    new_table = del_row(new_table)
    new_table = spin_90(new_table)
    new_table = del_row(new_table)

    # return new_table

    for i, val in enumerate(table_snippets):
        for j in val:
            if new_table == j:
                table_snippets.pop(i)
                return block_cnt
    return 0


def solution(game_board, table):
    n = len(table)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and visited[i][j] == 0:
                new_table = [[0 for _ in range(n)] for _ in range(n)]
                res_table = table_bfs(new_table, table, i, j, visited)

                snippet = []
                snippet.append(res_table)
                res = table_append(res_table, snippet)
                table_snippets.append(res)

    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and game_board[i][j] == 0:
                new_table = [[0 for _ in range(n)] for _ in range(n)]
                block_cnt = matching(new_table, game_board, i, j, table_snippets, visited)
                cnt += block_cnt
    return cnt

# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))