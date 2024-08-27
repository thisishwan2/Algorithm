# 본 문제는 DP문제이다. bfs 와 같은 완탐으로 문제를 푼다면, 100종류의 화폐를 탐색하는게 큐의 개수에 비례하게 증가하는데, 최악의 경우 시간이 터진다.
# DP로 접근하기 위해 생각해야할 것이 있다.
# 예제와 동일하게 money는 1,2,5가 있고 n은 최대 8이라고 가정하고 이를 표로 나타낸다.
'''
                        표현하고자 하는 수
표현가능한 동전(원)  1  2  3  4  5  6  7  8
        1        1  1  1  1  1  1  1  1
        2        0  1  1
        5
'''


# 1원을 이용하여 1~8을 표현하는 방법은? 1,1+1,1+1+1 ... 과 같이 1만 이용해 더하는 것이다. 따라서, 1로 표현한 경우의 수는 수마다 1개다
# 2원을 이용하여 1~8을 표현하는 방법은? 표현불가, 2, 1+2, 2+2 와 같이 표현가능하다.
# 이때, 1은 2를 이용하여 표현할 수 없으니 0으로 설정한다. 2는 2로 표현하므로 1로 설정한다.
# 이제 3,4를 표현하는 방법에 대해 잘 보자 1+2 이다. 즉, 다르게 생각하면, 어떠한 수에 2를 더한다. 이때 어떠한 수를 표현하는 경우는 몇가지가 있을까?
# 1을 표현하는 방법은 1가지이다. 따라서 2,3 위치는 1이다.
# 4를 표현하는 방법은 1+1+2, 2+2 로 2가지가 있다. 이는 어떠한 수에 2를 더한다. 이때 어떠한 수인 2를 표현하는 방법은 몇가지 일까?
# 즉, (1,2), (2,2)의 경우의 수를 더해주는 것이다.
# 이처럼 표현가능한 동전 x원이 있을때 x원 보다 큰 수를 표현하려면  큰 수 - x원의 차익만큼을 표현하는 방법을 알면 된다.

def solution(n, money):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in money:  # i원으로 표현가능한
        for j in range(i, n + 1):
            dp[j] = dp[j] + dp[j - i]
    # print(dp)

    return dp[-1] % 1000000007

# from collections import deque
#
#
# def solution(n, money):
#     answer = 0
#     q = deque()
#     q.append([0, 0])  # 가격, 시작 인덱스
#
#     money_size = len(money)
#     while q:
#         len_q = len(q)
#         # print("===")
#         for _ in range(len_q):
#             # print(q[0])
#             total, idx = q.popleft()
#
#             if total == n:
#                 answer = (answer + 1) % 1000000007
#             elif total > n:
#                 continue
#
#             for i in range(idx, money_size):
#                 if total + money[i] > n:
#                     continue
#                 else:
#                     q.append([total + money[i], i])
#
#     return answer