from collections import deque


def solution(priorities, location):
    q = deque()

    for idx, val in enumerate(priorities):
        q.append([idx, val])

    turn = 0
    while True:
        index, value = q.popleft()

        if value >= max(priorities):
            turn += 1
            priorities.remove(value)
            if index == location:
                return turn
        else:
            q.append([index, value])

    return turn

# 이건 큐안씀
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < max(priorities)):
            queue.append(cur)
        else:
            answer += 1
            priorities.remove(cur[1])
            if cur[0] == location:
                return answer