def solution(m, n, board):
    answer = 0

    new_board = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(board[i][j])
        new_board.append(tmp)

    # print(new_board)

    while True:
        # 2*2 를 완탐하면서 비교해봄
        broken = [[0 for _ in range(n)] for _ in range(m)]
        flag = False

        for i in range(m - 1):
            for j in range(n - 1):
                now = new_board[i][j]

                if now != "" and now == new_board[i + 1][j] and now == new_board[i][j + 1] and now == new_board[i + 1][j + 1]:
                    flag = True
                    broken[i][j] = 1
                    broken[i + 1][j] = 1
                    broken[i][j + 1] = 1
                    broken[i + 1][j + 1] = 1

        # print(broken)

        if flag == False:
            break

        # 부셔질 위치 배열의 위치를 부신다.
        for i in range(m):
            for j in range(n):
                if broken[i][j] == 1:
                    new_board[i][j] = ""
                    answer += 1
        # print(new_board)

        # 빈칸을 채우러 이동
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if new_board[i][j] != "" and new_board[i+1][j]=="":
                    x=i
                    while True:
                        x = x + 1
                        if x== m or new_board[x][j] != "":
                            break
                    new_board[x-1][j] = new_board[i][j]
                    new_board[i][j] = ""

        # print(*new_board, sep = "\n")

    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))