def solution(s):
    q = []

    left_cnt = 0
    for i in s:
        if i == "(":
            q.append("(")
        else:
            if len(q) == 0:
                return False
                break
            else:
                q.pop()

    if len(q) == 0:
        answer = True
    else:
        answer = False

    return answer

