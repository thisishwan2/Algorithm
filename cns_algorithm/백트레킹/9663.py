# 상하좌우대각선은 퀸이 있지못함.

import sys
input=sys.stdin.readline

n=int(input())
cnt=0

def is_vaild(candidate, current_column):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row]==current_column or abs(candidate[queen_row]-current_column) == abs(queen_row-current_row):
            return False
    return True



def back(n, current_row, current_candidate): # n, 현재 row, 각행의 컬럼 열 위치 모음
    global cnt

    if current_row==n:
        cnt+=1
        return

    for candidate_colum in range(n):
        if is_vaild(current_candidate, candidate_colum):
            current_candidate.append(candidate_colum)
            back(n, current_row+1, current_candidate)
            current_candidate.pop()

back(n, 0, [])
print(cnt)
