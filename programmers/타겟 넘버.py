# dfs
mat = [-1, 1]
tmp = []
answer = 0
def dfs(number, target):
    global answer
    if len(tmp) == len(number):
        if sum(tmp) == target:
            answer += 1
            return
    else:
        for i in range(2):
            tmp.append(number[len(tmp)] * mat[i])
            dfs(number, target)
            tmp.pop()


def solution(numbers, target):
    dfs(numbers, target)

    return answer

print(solution([1,1,1,1,1], 3))