import copy


def dfs(tmp, cal, n, visited):
    if len(tmp) == n:
        candidate.append(copy.deepcopy(tmp))
        return

    for i in range(n):
        if visited[i] == 0:
            tmp.append(cal[i])
            visited[i] = 1
            dfs(tmp, cal, n, visited)
            tmp.pop()
            visited[i] = 0


def calculate(num1, mat, num2):
    if mat == "-":
        return num1 - num2
    elif mat == "+":
        return num1 + num2
    else:
        return num1 * num2


candidate = []


def solution(expression):
    exp = []  # 식을 쪼갠다.
    cal = set()  # 연산자를 담는다.
    # 연산자 우선순위를 고려하여 경우의 수를 만든다.
    num = ""
    for i in expression:
        if i != "-" and i != "*" and i != "+":
            num += i
        else:
            exp.append(int(num))
            exp.append(i)
            cal.add(i)
            num = ""
    exp.append(int(num))
    # print(cal)
    print(exp)

    cal = list(cal)
    visited = [0] * len(cal)
    dfs([], cal, len(cal), visited)
    print(candidate)

    answer = 0
    for c in candidate:
        test_exp = copy.deepcopy(exp)
        s = []
        for matrix in c:
            for idx, val in enumerate(test_exp):
                if test_exp[idx - 1] == matrix:
                    s.append(val)
                    num2 = s.pop()
                    mat = s.pop()
                    num1 = s.pop()

                    res = calculate(num1, mat, num2)
                    s.append(res)

                else:
                    s.append(val)
            test_exp = copy.deepcopy(s)
            s = []
        answer = max(answer, abs(test_exp[0]))
    return answer