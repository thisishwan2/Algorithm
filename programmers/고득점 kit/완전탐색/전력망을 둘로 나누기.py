import copy
from collections import deque


def bfs(num, arr, n):
    q = deque()
    q.append(num)
    visited = [0] * (n + 1)
    visited[num] = 1

    while q:
        num = q.popleft()

        for i in arr[num]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

    return sum(visited)


def solution(n, wires):
    answer = 1e9

    arr = [[] for _ in range(n + 1)]

    # 각 연결정보를 연결한 인접리스트 생성
    for i in wires:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])

    # print(arr)

    # 모든 부분을 한번씩 끊어봄
    for idx, val in enumerate(wires):
        tmp_arr = copy.deepcopy(arr)

        # 끊는다
        tmp_arr[val[0]].remove(val[1])
        tmp_arr[val[1]].remove(val[0])

        # print(tmp_arr)
        # 탐색해서 각각 몇개씩 나오는지 확인(bfs)
        line1 = bfs(val[0], tmp_arr, n)
        line2 = bfs(val[1], tmp_arr, n)

        # 두 전력망의 노드 개수 차이가 가장 작은 것이 정답
        answer = min(answer, abs(line1 - line2))
    return answer