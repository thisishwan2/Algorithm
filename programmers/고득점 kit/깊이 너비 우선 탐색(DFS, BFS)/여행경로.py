answer = []

def dfs(tmp, tickets, visited):
    if sum(visited) == len(tickets):
        answer.append(tmp[:])
        return
    last_dest = tmp[-1]
    for i, val in enumerate(tickets):
        if val[0] == last_dest and visited[i] == 0:
            visited[i] = 1
            dfs(tmp + [val[1]], tickets, visited)
            visited[i] = 0  # 백트래킹

def solution(tickets):
    tickets.sort()  # 알파벳 순으로 정렬
    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            visited = [0] * len(tickets)
            visited[i] = 1
            dfs([ticket[0], ticket[1]], tickets, visited)

    answer.sort()
    return answer[0]