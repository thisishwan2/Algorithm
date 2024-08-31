# 배열읠 크기가 8, 길이는  8 = > 2중 순회 64*8 = 512
# 8! = 40320

import copy


def dfs(tmp, user_size, ban_size, visited, user_id):
    if len(tmp) == ban_size:
        candidate.append(copy.deepcopy(tmp))
        return

    for i in range(user_size):
        if visited[i] == 0:
            tmp.append(user_id[i])
            visited[i] = 1
            dfs(tmp, user_size, ban_size, visited, user_id)
            visited[i] = 0
            tmp.pop()


candidate = []


def solution(user_id, banned_id):
    ban_size = len(banned_id)
    user_size = len(user_id)
    visited = [0] * user_size
    dfs([], user_size, ban_size, visited, user_id)
    # print(candidate)

    cnt = 0
    answer = []
    for i in candidate:  # 40320
        equal_cnt = []
        for user, ban in zip(i, banned_id):  # 8
            flag = True

            if len(user) != len(ban):
                flag = False
                break

            for i, j in zip(user, ban):  # 8
                if j == "*":
                    continue
                elif i != j:
                    flag = False
                    break
            if flag:
                equal_cnt.append(user)
        if len(equal_cnt) == ban_size:
            # answer.append(equal_cnt)
            equal_cnt = sorted(equal_cnt)
            if equal_cnt not in answer:
                answer.append(equal_cnt)
    # print(answer)
    # print(cnt)
    return len(answer)


