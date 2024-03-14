''' 정답 코드 '''
# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, land, visited, res):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1
    min_y, max_y = y,y

    while q:
        x, y = q.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1

    for i in range(min_y, max_y+1):
        res[i] += cnt

    return res


def solution(land):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    arr = []

    n = len(land)
    m = len(land[0])

    res = [0 for i in range(m+1)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                res = bfs(i, j,land,visited,res)

    return max(res)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))

''' 실패 코드 '''

# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, land, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


def solution(land):
    answer = 0

    for j in range(len(land[0])):  # 열
        tmp = 0
        visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
        for i in range(len(land)):  # 행
            if land[i][j] == 1 and visited[i][j] == 0:
                tmp += bfs(i, j, land, visited)
        answer = max(tmp, answer)

    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))

# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, land, visited, idx):
    q = deque()
    q.append([x, y])
    visited[x][y] = idx
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = idx
                    cnt += 1
    return cnt


def solution(land):
    answer = 0

    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    dic = {}
    idx = 1

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt = bfs(i, j, land, visited, idx)
                dic[idx] = cnt
                idx += 1
    ans = []
    for j in range(len(land[0])):
        tmp = list(dic.keys())
        val = 0
        for i in range(len(land)):
            if visited[i][j] in tmp:
                val += dic.get(visited[i][j])
                tmp.remove(visited[i][j])
        ans.append(val)

    return max(ans)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))



# 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다.
# 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
# 가장 많은 석유량을 return

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, land, visited, idx):
    q = deque()
    q.append([x, y])
    visited[x][y] = idx
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = idx
                    cnt += 1
    return cnt


def solution(land):
    answer = 0

    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    arr = []
    dic = {}
    idx = 1

    for j in range(len(land[0])):
        tmp = 0
        dic_tmp = list(dic.keys())
        for i in range(len(land)):
            if land[i][j] == 1:
                if visited[i][j] == 0:
                    cnt = bfs(i, j, land, visited, idx)
                    tmp += cnt
                    dic[idx] = cnt
                    idx += 1

                elif visited[i][j] in dic_tmp:
                    tmp += dic.get(visited[i][j])
                    dic_tmp.remove(visited[i][j])
        arr.append(tmp)

    return max(arr)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 1]]))

