answer = []


def check(nodes, root):
    # 만약 특정 루트노드(서브트리의 루트도 가능)가 0이면 그의 자식들은 모두 0이어야 한다.
    if nodes[root] == "0" and ('1' in nodes):
        return False
    else:
        if len(nodes) == 1:
            return True
        else:
            left, right = nodes[:root], nodes[root + 1:]
            left_root, right_root = len(left) // 2, len(right) // 2
            res_left, res_right = check(left, left_root), check(right, right_root)

    if res_left and res_right:
        return True
    else:
        return False


def solution(numbers):
    for i in numbers:
        num = bin(i)[2:]  # 숫자를 이진수 문자열로 변환

        # 2진수로 변환된 num의 길이는 노드의 개수랑 같다. 따라서 노드의 개수가 포화 이진트리가 되려면 2의 제곱 -1 크기가 되야한다.
        # 따라서 num의 길이가 어느 제곱 사이인지를 파악하고, 큰 제곱에 맞도록 0을 앞에 넣는다.
        # ex: num = 1010101010 의 경우 포화 이진트리가 되려면 15개가 되야하므로 000001010101010 로 만들어 줘야 한다.
        node_cnt = len(num)
        square = 1

        while square <= node_cnt:
            square *= 2

        # node_cnt 크기가 square-1가 될 만큼 0을 앞에 채운다.
        num = (square - 1 - node_cnt) * "0" + num
        print(num)

        # 노드 개수
        node_cnt = len(num)
        root_node = node_cnt // 2

        if check(num, root_node):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([7, 42, 5]	))