# dfs 진행중에 늑대의 개수가 양과 동일해지면, 무조건 멈추고 이후 노드는 탐색하지 않아야함.

# 문제를 보면, 이전 노드로 돌아가서 반대편 노드로 가는것처럼 구현해야 할 것 같지만,
# 매번 갈 수 있는 노드 리스트를 만들어서 해당 노드 안에서 이동하면, 이미 갔던 위치를 되돌아가는 문제를 해결하면서, 전체 노드에 대해 탐색을 수행할 수 있다.
# 본 문제는 양이 늑대보다만 많다면, 늑대를 얼마든지 수집해도 무방한 문제
def dfs(num, tmp, sheep, wolf, info, graph):
    global answer

    # 양과 늑대의 개수를 업데이트해준다.
    if info[num] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1

    # 만약 늑대가 더 많다면 그 이후는 볼 필요도 없으니 중단한다.
    if wolf >= sheep:
        return

    # 갈수 있는 노드 추가
    tmp.extend(graph[num])
    # 갈 수 있는 노드들 중 i 노드를 간다고 설정하면 i를 제외한 나머지를 갈 수 있는 노드 리스트로 업데이트해서, dfs 수행
    for i in tmp:
        next_move_avaliable = []
        for j in tmp:
            if j != i:
                next_move_avaliable.append(j)
        dfs(i, next_move_avaliable, sheep, wolf, info, graph)


def solution(info, edges):
    global answer
    answer = 0

    n = len(info)

    # 인접리스트 생성
    graph = [[] for _ in range(n)]
    for i in edges:
        a, b = i
        graph[a].append(b)
    print(graph)

    dfs(0, [], 0, 0, info, graph)

    return answer

''' 아래는 큐를 활용한 풀이'''

from collections import deque


def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)

    q = deque()
    q.append([1, 0, 0, graph[0]])

    answer = 0

    while q:
        sheep, wolf, num, avaliable = q.popleft()  # 양의 수, 늑대의 수, 다음에 갈 노드 번호, 갈 수 있는 노드 리스트

        if answer < sheep:
            answer = sheep

        for idx, next in enumerate(avaliable):
            if info[next] == 1:  # 다음이 늑대면
                if sheep > wolf + 1:
                    q.append([sheep, wolf + 1, next, avaliable[:idx] + avaliable[idx + 1:] + graph[next]])

            else:
                q.append([sheep + 1, wolf, next, avaliable[:idx] + avaliable[idx + 1:] + graph[next]])
    return answer


solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])