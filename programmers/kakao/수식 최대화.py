import copy


def dfs(tmp, n, cal, visited):
    if len(tmp) == n:
        candidate.append(copy.deepcopy(tmp))
        return
    for i in range(len(cal)):
        if visited[i] == 0:
            visited[i] = 1
            tmp.append(cal[i])
            dfs(tmp, n, cal, visited)
            tmp.pop()
            visited[i] = 0


def operation(num1, num2, op):
    if op == '+':
        return (int(num1) + int(num2))
    if op == '-':
        return (int(num1) - int(num2))
    if op == '*':
        return (int(num1) * int(num2))


def cal(exp, op):
    array = []
    tmp = ""

    # 숫자인지, 연산자인지를 구분해서 배열에 넣는다.
    for i in exp:
        if i.isdigit() == True:
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)

    # 연산자 우선순위를 순회한다.
    for o in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            # 만약 연산자와 배열에서 뽑은 요소가 같으면, 연산을 수행한다.(이때, 스택에 마지막 요소와 배열의 첫요소(연산자 뽑고 난 뒤이므로 숫자가 된다)를 연산한다.
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack

    return abs(int(array[0]))


candidate = []


def solution(expression):
    # 연산자의 경우의 수를 구한다.
    visited = [0] * 3
    op = ["+", "-", "*"]
    dfs([], 3, op, visited)
    op = candidate

    result = []
    for i in op:
        result.append(cal(expression, i))

    return max(result)

