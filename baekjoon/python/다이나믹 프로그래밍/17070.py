#17070

# 파이프는 항상 빈 칸만 차지해야 한다. 파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향, 밀면서 회전을 할 수 있고, 회전은 45도만 가능.

import sys
input=sys.stdin.readline
from collections import deque

# 문제의 노란 파이프, 초록 파이프, 파란 파이프
dx=[0, 1, 1] 
dy=[1, 0, 1]

n=int(input())

graph=[]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# BFS로 푸는 법(시간초과)
# def bfs(start, end):
#     cnt=0
#     q=deque()
#     q.append([start,end, 0])

#     while q:
#         start, end, pos = q.popleft()
#         x1, y1 = start
#         x2, y2 = end
        
#         for i in range(3):
#             if pos == 0 and i==1: # 가로인 경우 초록파이프 경우 제외
#                 continue
#             if pos == 1 and i==0: # 세로인 경우 노란파이프 경우 제외
#                 continue

#             nx1,ny1=x2,y2
#             nx2=x2+dx[i]
#             ny2=y2+dy[i]

#             if 0<=nx2<n and 0<=ny2<n and graph[nx2][ny2]!=1: #범위내고, 파이트 끝자락이 빈칸인 경우
#                 if (i ==2 and graph[nx2-1][ny2]!=0) or (i==2 and graph[nx2][ny2-1]!=0): # 파이프가 대각선으로 향할때 주변 칸도 빈칸이어야함.
#                         continue

#                 if nx2==n-1 and ny2==n-1:
#                     cnt+=1
#                     continue
                
#                 q.append([[nx1,ny1], [nx2,ny2],i])
    
#     return cnt

# #애초에 도착점이 빈칸이 아닌
# if graph[n-1][n-1]==1:
#     print(0)
# else: 
#     print(bfs([0,0],[0,1]))

#dfs로 푸는 법(시간초과)
# def dfs(start, end, pos):
#     global count

#     x1, y1 = start
#     x2, y2 = end
    
#     if x2==n-1 and y2==n-1:
#         count+=1
        
#     for i in range(3):
#         if pos == 0 and i==1: # 가로인 경우 초록파이프 경우 제외
#                 continue
#         if pos == 1 and i==0: # 세로인 경우 노란파이프 경우 제외
#                 continue

#         nx1,ny1=x2,y2
#         nx2=x2+dx[i]
#         ny2=y2+dy[i]

#         if 0<=nx2<n and 0<=ny2<n and graph[nx2][ny2]!=1: #범위내고, 파이트 끝자락이 빈칸인 경우
#             if (i ==2 and graph[nx2-1][ny2]!=0) or (i==2 and graph[nx2][ny2-1]!=0): # 파이프가 대각선으로 향할때 주변 칸도 빈칸이어야함.
#                     continue
            
#             dfs([nx1,ny1], [nx2, ny2], i)
# count=0

# if graph[n-1][n-1]==1:
#     print(0)
# else: 
#     dfs([0,0],[0,1],0)
#     print(count)


def solution():

    '''
    참고: https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python

    dp[0][row][col] = 가로 파이프에 대한 dp
    dp[1][row][col] = 대각선 파이프에 대한 dp
    dp[2][row][col] = 세로 파이프에 대한 dp
    '''

    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    
    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                # r,c의 대각선 = r-1,c-1의 가로 + r-1,c-1의 대각선 + r-1,c-1의 세로 ( -\ + \\ + |\)
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                
	    # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                # r,c의 가로 = r,c-1의 가로 + r,c-1의 대각선( -- + \_ )
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                # r,c의 세로 = r-1,c의 세로 + r-1,c의 대각선( || + \| )
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    
    
    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()








