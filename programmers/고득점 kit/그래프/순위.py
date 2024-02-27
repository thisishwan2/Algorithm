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