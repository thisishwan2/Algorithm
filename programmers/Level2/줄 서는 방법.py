def solution(n, k):
    lst = []
    for i in range(1, n + 1):
        lst.append(i)

    pecto = []
    pecto.append(1)
    pecto.append(1)
    for i in range(2, n + 1):
        pecto.append(i * pecto[i - 1])

    answer = []
    for _ in range(n):
        num = (k - 1) // pecto[n - 1]
        answer.append(lst.pop(num))

        k = k % pecto[n - 1]
        n = n - 1

    return answer