# 최소 신장 트리: 최소 비용으로 만들수 있는 신장 트리를 찾는다.
# 크루스칼 알고리즘: 적은 비용으로 모든 노드를 연결할 수 있다.(싸이클 없음)

def get_parents(x, parents):
    if parents[x] == x: # 결국 x에 대한 부모는 재귀를 돌리면 찾아짐. 왜냐면 부모는 배열에서 자기자신을 값으로 지님
        return x
    return get_parents(parents[x], parents)


def find_parents(x,y,parents):
    x = get_parents(x, parents)
    y = get_parents(y, parents)

    if x==y:
        return True
    else:
        return False



def union(x,y,parents):
    # 두 부모는 다를것임. 왜냐면 이전에 두 부모가 다른것을 확인했기 때문
    x = get_parents(x, parents)
    y = get_parents(y, parents)

    # 부모를 비교해서 작은 부모로 설정
    if x<y:
        parents[y]=x
    else:
        parents[x]=y



def solution(n, costs):  # a섬, b섬, 비용

    answer = 0

    # 비용이 작은 순서대로 정렬
    costs.sort(key=lambda x: x[2])
    print(costs)

    parents = [i for i in range(n)]

    for i in costs:
        if not find_parents(i[0], i[1], parents): # 부모가 다르면
            union(i[0], i[1], parents) # 두 간선을 연결.
            answer += i[2]
    # union

    return answer
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# print(solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])) # 159