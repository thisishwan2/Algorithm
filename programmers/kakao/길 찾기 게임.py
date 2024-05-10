# 시간 초과나는 풀이

#from collections import deque
#
#
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.left = None
#         self.right = None
#
#
# class BinaryTree():
#     def __init__(self):  # 트리 생성
#         self.root = None
#
# tmp = []
#
# def solution(nodeinfo):
#     max_x = max(x for x, y in nodeinfo)
#     max_y = max(y for x, y in nodeinfo)
#
#     print(max_x, max_y)
#
#     arr = [[0 for _ in range(max_x + 2)] for _ in range(max_y + 1)]
#     for idx, (x, y) in enumerate(nodeinfo):
#         arr[max_y - y][x] = idx + 1
#     print(*arr, sep='\n')
#
#     px = arr[0].index(max(arr[0]))
#     level = 1
#     num = max(arr[0])
#     lx = 0
#     rx = max_x + 1
#
#
#
#     tree = BinaryTree()
#     node = Node(num)
#     tree.root = node
#
#     q = deque()
#     q.append([px, lx, rx, level, num, node])
#
#     while q:
#         px, lx, rx, level, num, node = q.popleft()
#
#         for i in range(level, max_y + 1):
#             flag = False
#             if sum(arr[i]) == 0:
#                 continue
#             else:
#                 for idx, j in enumerate(arr[i]):
#                     if j == 0:
#                         continue
#                     if lx <= idx < px:  # 현재 노드 왼쪽에
#                         left_node = Node(arr[i][idx])
#                         node.left = left_node
#                         q.append([idx, lx, px, level+1, arr[i][idx], left_node])
#                         flag = True
#
#
#                     elif px < idx <= rx:  # 현재 노드 오른쪽에
#                         right_node = Node(arr[i][idx])
#                         node.right = right_node
#                         q.append([idx, px, rx, level+1, arr[i][idx], right_node])
#                         flag = True
#
#             if flag:
#                 break
#
#     global tmp
#
#     answer = []
#     preorder(tree.root)
#     answer.append(tmp)
#     tmp = []
#     postorder(tree.root)
#     answer.append(tmp)
#
#     return answer
#
# def preorder(node):
#     global tmp
#     if node.item != None:
#         tmp.append(node.item)
#         if node.left != None:
#             preorder(node.left)
#         if node.right != None:
#             preorder(node.right)
#
# def postorder(node):
#     if node.item != None:
#         if node.left != None:
#             postorder(node.left)
#         if node.right != None:
#             postorder(node.right)
#         tmp.append(node.item)
#
# solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
#
#


from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def build_tree(nodeinfo):
    # 노드 번호, x, y 순으로 리스트를 만들어서 y 기준으로 내림차순, x기준으로 오름차순 => 트리형태로 정렬됨
    nodes = sorted([(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[2], x[1]))
    root = Node(nodes[0][0], nodes[0][1], nodes[0][2])
    for idx, x, y in nodes[1:]:
        current = root
        new_node = Node(idx, x, y)

        # 루트 노드(현재 노드)로 부터 탐색을 시작하는 것을 반복
        while True:

            # new node의 x좌표와 현재 node의 x좌표를 비교해가면서 어느 노드의 왼쪽 혹은 오른쪽 서브 트리인지를 찾고, 현재 노드의 자식으로 연결함
            if x < current.x:  # Go left
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:  # Go right
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
    return root

def preorder(node, result):
    if not node:
        return
    result.append(node.idx)
    preorder(node.left, result)
    preorder(node.right, result)

def postorder(node, result):
    if not node:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.idx)

def solution(nodeinfo):
    root = build_tree(nodeinfo)
    pre_result, post_result = [], []
    preorder(root, pre_result)
    postorder(root, post_result)
    return [pre_result, post_result]

# Example usage
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))