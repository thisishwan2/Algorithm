# from collections import deque
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def solution(board):
#     n = len(board)

#     # cost[방향][x][y]
#     cost = [[[1e9] * n for _ in range(n)] for _ in range(4)]
#     # 0,0의 모든 방향은 0으로 시작
#     for i in range(4): cost[i][0][0] = 0

#     q = deque()
#     # 큐에는 오른쪽, 아래 방향으로 초기에 넣는다.
#     q.append([0,1,100,1])
#     q.append([1,0,100,3])# x, y, cost, direction
#     cost[1][0][1] = 100
#     cost[3][1][0] = 100

#     while q:
#         x,y,price,dir = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= n or board[ny][nx]: continue

#             # 방향이 같다.
#             if dir == i:
#                 nprice = price + 100
#             # 방향이 다르다.
#             else:
#                 nprice = price + 600

#             if nprice > cost[i][nx][ny]: continue
#             cost[i][nx][ny] = nprice
#             q.append([nx,ny,nprice,i])

#     return min(cost[0][n - 1][n - 1],cost[1][n - 1][n - 1],cost[2][n - 1][n - 1],cost[3][n - 1][n - 1])
# # print(solution([[0,0,0],[0,0,0],[0,0,0]]))

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    n = len(board)

    # cost[방향][x][y]
    cost = [[[1e9] * n for _ in range(n)] for _ in range(4)]
    # 0,0의 모든 방향은 0으로 시작
    for i in range(4): cost[i][0][0] = 0

    q = deque()
    # 큐에는 오른쪽, 아래 방향으로 초기에 넣는다.
    q.append([0,0,0,1])
    q.append([0,0,0,3])# x, y, cost, direction
    cost[1][0][1] = 100
    cost[3][1][0] = 100

    while q:
        x,y,price,dir = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:

                # 방향이 같다.
                if dir == i:
                    nprice = price + 100
                    if cost[i][nx][ny] > nprice:
                        cost[i][nx][ny] = nprice
                        q.append([nx,ny,nprice,i])

                # 방향이 다르다.
                else:
                    nprice = price + 600
                    if cost[i][nx][ny] > nprice:
                        cost[i][nx][ny] = nprice
                        q.append([nx,ny,nprice,i])

    return min(cost[0][n - 1][n - 1],cost[1][n - 1][n - 1],cost[2][n - 1][n - 1],cost[3][n - 1][n - 1])
print(solution([[0,0,0],[0,0,0],[0,0,0]]))