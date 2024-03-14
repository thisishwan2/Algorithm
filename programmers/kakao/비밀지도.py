def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        arr = bin(i | j)[2:] # bin은 10진수를 2진수로 변환(10진수에 대해 or 연산을 하고 bin해도 결과는 동일)
        if len(arr) != n:
            arr = (n - len(arr)) * "0" + arr
            # zfill.(n)을 해주면 n개 만큼 0이 앞에 온다.
            # rjust를 통해 공백의 수, 공백을 메워줄 문자를 넣어
            # arr.rjust(n - len(arr), "0")

        arr = arr.replace("1", "#")
        arr = arr.replace("0", " ")
        answer.append(arr)

    return answer