def dfs(n, m, tmp, j_index, visited, ability):
    global answer

    if len(tmp) == m:
        answer = max(sum(tmp), answer)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            tmp.append(ability[i][j_index])
            dfs(n,m, tmp,j_index+1, visited, ability)
            tmp.pop()
            visited[i] = 0


answer = 0


def solution(ability):
    visited = [0] * len(ability)
    dfs(len(ability), len(ability[0]), [], 0, visited, ability)

    print(answer)
    return answer
solution([[20, 30], [30, 20], [20, 30]]	)