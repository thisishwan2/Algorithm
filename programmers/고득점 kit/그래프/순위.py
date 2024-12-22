from collections import deque

def plus_function(start, lst, n):
    cnt = 0
    q = deque()
    visited = [0] * (n + 1)
    visited[start] = 1
    q.append(start)

    while q:
        start = q.popleft()
        for i in lst[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

def minus_function(start, lst, n):
    cnt = 0
    q = deque()
    visited = [0] * (n + 1)
    visited[start] = 1
    q.append(start)

    while q:
        start = q.popleft()
        for i in lst[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

def solution(n, results):
    answer = 0

    plus = [[] for _ in range(n + 1)]
    minus = [[] for _ in range(n + 1)]

    for i in results:
        a = i[0]
        b = i[1]

        plus[a].append(b)
        minus[b].append(a)

    print(plus)
    print(minus)

    for i in range(1, n + 1):
        plus_cnt = 0
        minus_cnt = 0

        plus_cnt = plus_function(i, plus, n)
        minus_cnt = minus_function(i, minus, n)

        if plus_cnt + minus_cnt == n - 1:
            answer += 1

    return answer


# 이 문제는 a선수의 순위를 알기 위해서는 a 선수와 나머지 선수와의 승패 기록을 알고 있어야 함.
# 따라서 이러한 승패에 대한 연쇄작용 a->b->c 순으로 이기는 경우를 고려하면 a->c 도 가능하므로
# 이를 고려하여 플로이드 위셜로 푼다.
def solution(n, results):
    board = [[0 for _ in range(n)] for _ in range(n)]
    # a가 b를 이기면 1, a가 b에게 지면 -1
    # 플로이드 위셜을 전부다 돌고 나면, 각 행에 0이 하나인. 즉 승패에 대한 기록이 없는 것이 하나 있다면,
    # 그 사람의 순위는 결정된것이다.
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1

    # 플로이드 워셜을 이용하여
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    # i는 k를 이기고, k는 j를 이기는 경우에는
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1 # i는 j를 반드시 이긴다.
                    # i는 k한테 지고, k는 j한테 지는 경우에는
                    elif board[i][k]==-1 and board[k][j]==-1:
                        board[i][j] = -1 # i는 j한테 반드시 진다.
    answer = 0
    for i in range(n):
        zero_cnt = 0
        for j in range(n):
            if board[i][j]==0:
                zero_cnt+=1
        if zero_cnt==1:
            answer+=1
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])