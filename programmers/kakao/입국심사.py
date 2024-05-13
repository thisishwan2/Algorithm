# 이분 탐색은 탐색하고자 하는 범위를 어떤것으로 잡을건지
# 비교할 값의 기준은 어떤것을 할것인지가 중요함
# 따라서 현재 문제에서는 탐색 범위가 time 이라는 것을 유추할 수 있음
# 중요한건 time 범위에서 어떤 기준을 가지고 비교할건데, 이 문제에서는 심사받는 사람의 수 n을 기준으로 비교할것이다.

def solution(n, times):
    answer = 0

    left = min(times) # 최소 시간
    right = max(times) * n # 최대 시간

    while (left <= right): # 같다를 해줘야함
        mid = (left + right) // 2

        total = 0
        for i in times:
            total += mid // i

            if total >= n: # n명 이상 심사할 수 있는 경우는 mid가 answer이거나 큰 경우임
                break

        if total >= n: # mid가 answer이거나 큰 경우
            answer = mid
            right = mid - 1
        else: # n명 미만인 경우
            left = mid + 1

    return answer
solution(6, [7, 10])