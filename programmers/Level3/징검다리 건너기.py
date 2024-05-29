from collections import deque

from collections import deque


def solution_sliding_window(stones, k):
    n = len(stones)
    q = deque()
    q.append(0)  # 0번째 인덱스 추가

    for i in range(1, k):

        # 집어넣는 값보다 이미 큐의 마지막에 존재하는 값이 작은 경우에는 앞쪽의 값들을 없앤다.
        while q and stones[q[-1]] < stones[i]:
            q.pop()

        # 비었거나, 값이 더 큰 경우에만 집어넣기
        if not q or stones[q[-1]] >= stones[i]:
            q.append(i)

    answer = stones[q[0]]

    for i in range(k, n):
        # 큐의 가장 마지막 부분을 제거
        while q and stones[q[-1]] < stones[i]:
            q.pop()

        # 앞쪽 제거
        while q and q[0] <= i - k:
            q.popleft()

        # 더 큰 경우에만 집어넣기
        if not q or stones[q[-1]] >= stones[i]:
            q.append(i)

        answer = min(answer, stones[q[0]])
    return answer

def solution_bs(stones, k):
    answer = 0

    # 이진탐색(배열의 크기가 2억이므로)
    start = min(stones)
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if (stone - mid <= 0):
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                break

        if cnt >= k:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer



# 효율성 실패
# def solution(stones, k):
#     answer = 0
#
#     # 이진탐색(배열의 크기가 2억이므로)
#     start = min(stones)
#     end = max(stones)
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         # 아래 방식은 200000을 여러번 탐색하므로 비효율적이고 시간초과가 발생함
#         new_stones = []
#         for i, val in enumerate(stones):
#             new_stones.append(stones[i] - mid)
#
#         # 연속으로 0이하의 값이 몇개 존재하는지 확인
#         seq_cnt = 0
#         if new_stones[0] <= 0:
#             cnt = 1
#         else:
#             cnt = 0
#         for i in range(1, len(new_stones)):
#
#             if new_stones[i] <= 0:
#                 if new_stones[i - 1] <= 0:
#                     cnt += 1
#                 else:
#                     cnt = 1
#             else:
#                 seq_cnt = max(seq_cnt, cnt)
#
#         seq_cnt = max(seq_cnt, cnt)
#
#         # 0보다 작은 디딤돌의 개수가 k보다 크거나 같으면
#         # print("cnt = "+str(seq_cnt))
#         if seq_cnt >= k:
#             end = mid - 1
#             answer = mid
#         else:
#             start = mid + 1
#
#     return answer