# 적이 공격해 내구도가 0이 되면 건물 파괴, 아군은 회복스킬로 건물 내구도 높임
# 중요한것은 한번 0이 되어도 이후 아군이 회복하거나 적이 공격해도 해당 건물은 회복 되거나 데미지를 입음.
# 즉, 모든 차례가 끝나고 그 이후에 내구도를 확인후 파괴되지 않은 건물 개수 확인

# type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
# type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.


#### 해당 코드는 효율성 검증에 실패한 코드

# def solution(board, skill):
    
#     for i in skill:
#         type = i[0]
#         r1,c1=i[1],i[2]
#         r2,c2=i[3],i[4]
#         degree=i[5]
        
#         if type==1: #적의 공격
#             for x in range(r1, r2+1):
#                 for y in range(c1,c2+1):
#                     board[x][y]=board[x][y]-degree
#         else:
#             for x in range(r1, r2+1):
#                 for y in range(c1,c2+1):
#                     board[x][y]=board[x][y]+degree

#     answer = 0
    
#     for i in board:
#         for j in i:
#             if j>0:
#                 answer+=1
    
#     return answer


def solution(board, skill):
    x=len(board)
    y=len(board[0])
    graph=[[0 for _ in range(y+1)]for _ in range(x+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type==1:
            degree=-degree
        
        graph[r1][c1]+=degree
        graph[r1][c2+1]-=degree
        graph[r2+1][c1]-=degree
        graph[r2+1][c2+1]+=degree
        
    for i in range(x+1):
        for j in range(y-1):
            graph[i][j+1]+=graph[i][j]
    
    for i in range(y-1):
        for j in range(x+1):
            graph[i+1][j] += graph[i][j]
    
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j]+=graph[i][j]
            
            if board[i][j]>0:
                answer+=1
    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))