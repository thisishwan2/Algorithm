# 최소 피로도: 탐험하기 위한 최소한의 피로도
# 소모 피로도: 탐험 후 깎이는 피도로
# 최대한 많은 던전 탐색

max_cnt = 0


def dfs(now_hp, cnt, dungeons, visited):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for idx, val in enumerate(dungeons):
        if visited[idx] == 0:  # 방문안한 경우
            if val[0] <= now_hp:  # 최소 피로도 이상의 피도로가 있는 경우
                visited[idx] = 1
                dfs(now_hp - val[1], cnt + 1, dungeons, visited)
                visited[idx] = 0


def solution(k, dungeons):
    answer = -1

    visited = [0 for _ in range(len(dungeons))]
    dfs(k, 0, dungeons, visited)
    answer = max(answer, max_cnt)

    return answer