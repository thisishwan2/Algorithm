def isAvaliable(q_candidate, col):
    curRow = len(q_candidate)
    for i in range(curRow):

        # 같은 열, 같은 대각선(서로 위치에서 열의 차이 뺀게 행의 차이 뺀거와 같은)
        if q_candidate[i] == col or abs(q_candidate[i] - col) == abs(i - curRow):
            return False
    return True


def nQueen(n, curRow, q_candidate):
    cnt = 0
    if n == curRow:
        return 1

    for col in range(n):
        flag = False
        for row in range(len(q_candidate)):  # curRow 의 열을 순회
            if col == q_candidate[row]:
                flag = True
                break
            if abs(q_candidate[row] - col) == abs(row - curRow):
                flag = True
                break
        if flag == False:
            cnt += nQueen(n, curRow + 1, q_candidate + [col])
    return cnt


def solution(n):
    answer = nQueen(n, 0, [])

    return answer