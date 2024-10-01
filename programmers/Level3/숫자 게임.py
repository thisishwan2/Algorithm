def solution(A, B):
    answer = 0

    # 최대로 많이 이기려면, A의 값보다 조금 더 큰놈이 출전하는게 좋음
    a = sorted(A)
    b = sorted(B)

    index = 0
    for i in a:
        if index == len(b):
            break

        if i < b[index]:
            answer += 1
            index += 1
        else:
            while i >= b[index]:
                index += 1

                if index == len(b):
                    return answer
            answer += 1
            index += 1

    return answer