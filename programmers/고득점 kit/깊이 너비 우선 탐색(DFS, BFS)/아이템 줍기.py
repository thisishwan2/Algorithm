from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    ans = 0
    # 전체적으로 스케일을 2배로 증가시킴
    board = [[-1 for _ in range(101)] for _ in range(101)]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x1, y1, x2, y2 in rectangle:

        x1 = 2 * x1
        y1 = 2 * y1
        x2 = 2 * x2
        y2 = 2 * y2

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):

                # 테두리가 아닌, 내부이면
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                # 내부가 아닌 경우 = 테두리 (단 내부로 표시가 안되어있어야함. 내부로 한번 표시가 된곳이면 아무리 테두리여도 내부임.)
                elif board[i][j] != 0:
                    board[i][j] = 1

    # 내부는 0, 테두리는 1, 외부는 -1
    # print(*board, sep='\n')

    characterX = 2 * characterX
    characterY = 2 * characterY
    itemX = 2 * itemX
    itemY = 2 * itemY
    visited = [[1 for _ in range(101)] for _ in range(101)]

    q = deque()
    q.append([characterX, characterY])

    while q:
        x, y = q.popleft()

        if (x, y) == (itemX, itemY):
            ans = visited[x][y] // 2
            break
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if board[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append([nx, ny])

    return ans