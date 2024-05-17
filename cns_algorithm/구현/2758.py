import sys
input= sys.stdin.readline

# 빙고판에 있는 숫자들을 체크하는 함수
def check(visited):
    line = 0

    # 가로줄 체크
    for i in range(5):
        if sum(visited[i]) == 5:
            line += 1

    # 세로줄 체크
    for j in range(5):
        cnt = 0
        for i in range(5):
            if visited[i][j] == 1:
                cnt+=1
        if cnt == 5:
            line += 1

    # 대각선 체크
    cnt = 0
    for i,j in zip(range(5),range(5)):
        if visited[i][j] == 1:
            cnt +=1
    if cnt == 5:
        line+=1

    # 대각선 체크
    cnt = 0
    for i, j in zip(range(4,-1,-1), range(5)):
        if visited[i][j] == 1:
            cnt += 1
    if cnt == 5:
        line += 1

    return line

board = []

# 빙고 입력
for i in range(5):
    board.append(list(map(int, input().split())))

# print(*board, sep='\n')

numbers = []
# 사회자가 부르는 수
for i in range(5):
    number = list(map(int, input().split()))
    for j in number:
        numbers.append(j)

# print(numbers)

# 빙고 시작
visited=[[0 for _ in range(5)]for _ in range(5)]
for idx, number in enumerate(numbers):
    for i in range(5):
        for j in range(5):
            if board[i][j]==number:
                visited[i][j] = 1
                line = check(visited)
                if line>=3:
                    print(idx+1)
                    exit()