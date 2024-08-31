# k개 이상 연속된 0 이하의 디딤돌이 있으면 그 전 까지 건널 수 있다.
# 즉, n명 건넛을때, 0의 연속 개수를 파악하자.
# 이때 배열의 max 값이 즉, 건널 수 있는 최대 인원 수
def solution(stones, k):
    start = 1
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2 # 2명이 건넘

        seq = 0
        for i in stones:
            if i <= mid:
                seq += 1
            else:
                seq = 0
            if seq >= k:
                break

        # k를 만족하는 가장 첫번째 경우를 찾는다. lower bound: k이상의 첫번째
        if seq >= k:
            end = mid -1
        elif seq < k:
            start = mid + 1

    return start


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


