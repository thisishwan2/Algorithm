# 본 문제에서 가장 중요한 건 바로 좌우 이동이다.
# 우선 각 알파벳이 조이스틱을 몇번 움직여야 하는지는 아스키 코드를 이용하면 쉽게 알 수 있다.(여기서 z부터 내림차순의 경우는 1을 더해준다.(A->Z 과정이 있기 때문)
# 파이썬에서는 자바와 다르게 정수에 대해서는 chr(), 문자는 ord()를 써야한다.
# 그리고 좌우 움직임은 일반적으로 그냥 한방향으로 쭉가면 되나? 싶지만 그렇지 않다. 바로 A가 연속적으로 끼어 있을 수 있으므로 좌우로 왓다갓다 하는 경우가 생긴다.
# 따라서 본 문제는 가장 긴 A 연속이 몇번째 인덱스 부터 몇번째 인덱스 까지인지를 알면 가장 조금 좌우로 움직이는 경우를 알 수 있다.
# 모든 알파벳에 대해 순회하며 A연속을 만날때 마다 시작(인덱스)과 끝지점(증가시킨 next)를 바탕으로 min 값을 구해서 비교하면 된다.

def solution(name):
    joy = 0

    for i, v in enumerate(name):
        joy += min(ord(v) - ord("A"), ord("Z") - ord(v) + 1)

    print(joy)

    move = len(name) - 1
    for i, v in enumerate(name):

        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        move = min(move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
    joy += move
    return joy