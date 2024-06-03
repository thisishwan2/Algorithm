def solution(prices):
    answer = []
    n = len(prices)
    for idx, val in enumerate(prices):
        cnt = 0
        for i in range(idx + 1, n):
            if prices[i] < val:

                cnt += 1
                break
            else:
                cnt += 1

        answer.append(cnt)
    return answer