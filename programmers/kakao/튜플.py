def solution(s):
    answer = []

    a = s.strip()
    a = a[2:-2]
    b = a.split("},{")

    lst = list(b)

    arr = []
    for i in lst:
        tmp = i.strip()
        arr.append(list(tmp.split(",")))

    arr.sort(key=len)

    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
            else:
                pass

    return answer