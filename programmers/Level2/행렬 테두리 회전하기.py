import copy


def solution(rows, columns, queries):
    answer = []

    board = []
    for i in range(rows):
        tmp = []
        for j in range(1, columns + 1):
            tmp.append(i * columns + j)
        board.append(tmp)

    for sx, sy, ex, ey in queries:
        sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
        minimum = 1e9

        temp = board[sx][sy]  # 좌측 상단 값을 임시로 저장
        minimum = min(minimum, temp)

        # 역순으로 좌표를 이동한다. (copy 쓰면 시간이 너무 오래걸린다.)
        # 좌측 열 이동
        for i in range(sx, ex):
            board[i][sy] = board[i + 1][sy]
            minimum = min(minimum, board[i][sy])

        # 하단 행 이동
        for j in range(sy, ey):
            board[ex][j] = board[ex][j + 1]
            minimum = min(minimum, board[ex][j])

        # 우측 열 이동
        for i in range(ex, sx, -1):
            board[i][ey] = board[i - 1][ey]
            minimum = min(minimum, board[i][ey])

        # 상단 행 이동
        for j in range(ey, sy, -1):
            board[sx][j] = board[sx][j - 1]
            minimum = min(minimum, board[sx][j])

        # 임시로 저장해둔 값을 마지막에 위치시킨다.
        board[sx][sy + 1] = temp
        minimum = min(minimum, temp)

        # 최소값 저장
        answer.append(minimum)
    # answer.sort()
    return answer