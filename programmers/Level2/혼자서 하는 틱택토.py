# 선공이 O, 후공이 X 를 번갈아서 빈칸에 표시
# 같은 표시를 만들면, 그사람 승리, 9칸이 다차면 무승부

def solution(board):
    answer = 1

    o_cnt = 0
    x_cnt = 0
    o_line = False
    x_line = False

    # 행 검사
    for i in range(3):
        o_cnt_ = 0
        x_cnt_ = 0
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt_ += 1
            elif board[i][j] == 'X':
                x_cnt_ += 1

        o_cnt += o_cnt_
        x_cnt += x_cnt_

        if o_cnt_ == 3:
            o_line = True
        elif x_cnt_ == 3:
            x_line = True

    # 열 검사
    for j in range(3):
        o_cnt_ = 0
        x_cnt_ = 0
        for i in range(3):
            if board[i][j] == 'O':
                o_cnt_ += 1
            elif board[i][j] == 'X':
                x_cnt_ += 1

        if o_cnt_ == 3:
            o_line = True
        elif x_cnt_ == 3:
            x_line = True

    # 대각선
    o_cnt_ = 0
    x_cnt_ = 0
    for i in range(3):
        if board[i][i] == 'O':
            o_cnt_ += 1
        elif board[i][i] == 'X':
            x_cnt_ += 1

    if o_cnt_ == 3:
        o_line = True
    elif x_cnt_ == 3:
        x_line = True

    # 대각선
    o_cnt_ = 0
    x_cnt_ = 0
    for i in range(3):
        if board[i][2 - i] == 'O':
            o_cnt_ += 1
        elif board[i][2 - i] == 'X':
            x_cnt_ += 1

    if o_cnt_ == 3:
        o_line = True
    elif x_cnt_ == 3:
        x_line = True

    # 게임 가능 여부 판단
    if o_cnt == x_cnt:
        if o_line == True:
            answer = 0
    elif x_cnt > o_cnt:
        answer = 0

    elif x_cnt < o_cnt:
        if x_line == True:
            answer = 0
        elif o_cnt - x_cnt > 1:  # 개수가 2개이상 차이나는 것은 불가능
            answer = 0
    return answer

# 규칙

# 0을 반환하는 경우의 수를
# - O와 X의 개수 차이가 2개 이상인 경우
# - O와 X의 개수가 같은데, O가 가로, 세로, 대각선 중 연결된 것이 있는 경우
# - X가 O보다 더 많은 경우
# - O가 X보다 많은데, X중에 가로,세로,대각선 연결된게 있는 경우