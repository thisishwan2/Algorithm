def solution(user_id, banned_id):
    # 조합이 아닌 순열을 써서 모든 경우를 구해야함.(그리고 같은 원소를 가진 애들은 set을 해서 제외)
    def dfs(idx):
        if idx == len(banned_id):
            tmp_list = []
            for i in range(len(visited)):
                if visited[i]:
                    tmp_list.append(user_id[i])
            answer.add(tuple(tmp_list))

            return

        for i in range(len(user_id)):
            if not visited[i] and check(user_id[i], banned_id[idx]):
                visited[i] = True
                dfs(idx + 1)
                visited[i] = False

    def check(u, b):  # 비교하는 과정에서 순서가 동일해야하기 때문에 조합 대신 순열
        if len(u) != len(b):
            return False

        for i in range(len(u)):
            if b[i] == '*':
                continue
            if u[i] != b[i]:
                return False

        return True

    # answer = set()
    answer = set()
    visited = [False] * len(user_id)

    dfs(0)
    print(answer)

    return len(answer)

# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])