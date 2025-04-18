from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(storage, requests):
    answer = 0

    n = len(storage)
    m = len(storage[0])
    container = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            container[i][j] = 1
    # print(*container, sep = '\n')

    for req in requests:
        if len(req) == 1:  # 지게차로 외부와 연결된 컨테이너만 지움
            # 외부만 탐색
            q = deque()
            q.append([0, 0])
            visited = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
            visited[0][0] = 1

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 중요한건 외부에서 꺼낸 컨테이너 내부쪽에 같은 컨테이너가 있으면 애는 빼면 안됨
                    if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                        if visited[nx][ny] == 0:
                            # 외부와 연결됨
                            if container[nx][ny] == 0:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                            # 지게차로 빼야하는 부분은 큐에 담지 않는다.
                            elif container[x][y] == 0 and container[nx][ny] == 1 and storage[nx - 1][ny - 1] == req:
                                container[nx][ny] = 0
                                visited[nx][ny] = 1
                            # 외부랑 연결되어 있는데, 크레인으로 뺀 부분은 그 옆에 또 크레인으로 뺀놈이 있을 수 있으므로 큐에 담는다.
                            elif container[x][y] == 0 and container[nx][ny] == -1:
                                container[nx][ny] = 0
                                visited[nx][ny] = 1
                                q.append([nx, ny])


        else:  # 크레인으로 모든 해당하는 컨테이너 지움
            for i in range(n + 2):
                for j in range(m + 2):
                    if container[i][j] == 1 and storage[i - 1][j - 1] == req[0]:
                        container[i][j] = -1

            # -1 중에서 외부와 연결된 녀석을 찾아서 이어준다.
            q = deque()
            q.append([0, 0])
            visited = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
            visited[0][0] = 1
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                        if visited[nx][ny] == 0:
                            if container[nx][ny] == 0:
                                q.append([nx, ny])
                                visited[nx][ny] = 1

                            # -1 인 부분
                            elif container[x][y] == 0 and container[nx][ny] == -1:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                                container[nx][ny] = 0

    #         print("============")
    #         print(*container, sep='\n')

    for i in range(n + 2):
        for j in range(m + 2):
            if container[i][j] == 1:
                answer += 1
    return answer