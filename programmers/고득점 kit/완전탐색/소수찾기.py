import math
import sys

sys.setrecursionlimit(10000)

ans = []


def per(tmp, lst, used, i):
    if len(tmp) == i and tmp not in ans:
        ans.append("".join(tmp))
        return
    for j in range(len(lst)):
        if used[j] == False:
            used[j] = True
            tmp.append(lst[j])
            per(tmp, lst, used, i)
            tmp.pop()
            used[j] = False


def solution(numbers):
    answer = 0
    lst = list(numbers)
    used = [False for i in range(len(numbers))]

    for i in range(1, len(lst) + 1):
        per([], lst, used, i)

    nums = list(set(list(map(int, ans))))
    print(nums)
    for i in nums:
        if i <= 1:
            continue
        if i == 2:
            answer += 1
            continue

        sosu=False

        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                sosu=True
                break

        if sosu==False:
            answer += 1

    return answer