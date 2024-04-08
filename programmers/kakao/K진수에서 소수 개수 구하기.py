import math


def solution(n, k):
    answer = -1

    # 10진수를 k진수로 바꾸는 방법
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k

    tmp = tmp[::-1]

    lst = tmp.split("0")
    ans = []
    for i in lst:
        if len(i) != 0:
            ans.append(int(i))

    cnt = 0
    for i in ans:
        print(cnt)
        if i == 1:
            continue

        for j in range(2, math.ceil(i ** (1 / 2)) + 1):
            flag = False
            if j != i and i % j == 0:
                flag = True
                break

        if flag == False:
            cnt += 1

    return cnt