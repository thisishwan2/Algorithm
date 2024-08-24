def solution(sequence):
    tmp1 = []
    tmp2 = []
    n = len(sequence)

    cal = 1
    for i in range(n):
        tmp1.append(cal)
        tmp2.append(-cal)
        cal *= -1

    seq1 = []
    seq2 = []

    for i, j in zip(sequence, tmp1):
        seq1.append(i * j)
    for i, j in zip(sequence, tmp2):
        seq2.append(i * j)

    # print(seq1)
    # print(seq2)

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = seq1[0]
    dp2[0] = seq2[0]

    answer = max(dp1[0], dp2[0])

    for i in range(1, n):
        dp1[i] = max(seq1[i], seq1[i] + dp1[i - 1])
        answer = max(answer, dp1[i])
    for i in range(1, n):
        dp2[i] = max(seq2[i], seq2[i] + dp2[i - 1])
        answer = max(answer, dp2[i])

    #     print(dp1)
    #     print(dp2)

    return answer
# 1,-1,1,-1
# -1,1,-1,1
# 두가지의 경우를 구해서 dp를 한다.
