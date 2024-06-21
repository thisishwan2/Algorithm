st = input()
bomb =  input()
n = len(bomb)
stack = []

for i in st:
    stack.append(i)

    if "".join(stack[len(stack)-n:]) == bomb:
        for i in range(n):
            stack.pop()
        # 처음에는 아래와 같이 슬라이싱을 했다.
        # 그러나 그렇게 되면 최대 1,000,000번의 길이의 문자열에서 슬라이싱(완전탐색)을 하기 때문에 시간복잡도가 터진다.
        # 그에 반해 pop을 bomb의 크기만큼만 하면 매번 35번 이하만 연산을 수행한다.
        # stack = stack[:len(stack)-n]
if stack:
    print("".join(stack))
else:
    print("FRULA")