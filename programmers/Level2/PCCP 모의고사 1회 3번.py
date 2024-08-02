def solution(queries):
    answer = []

    for i in queries:
        n = i[0]  # 세대
        idx = i[1] - 1  # 위치
        lst = []  # 자식부터 부모까지(2세대) 타고 가면서 각 세대에서의 위치를 넣는다. ex: 만약 4세대 정보를 줬다면 [3세대 위치, 2세대 위치]

        # 1세대가 되면 탈출함
        while n > 1:
            lst.append(idx % 4)  #
            idx = idx // 4
            n -= 1

        # Rr 체크용
        check = False

        # 2세대부터 어느 위치인지 확인하면서, 한번이라도 맨끝(각 자식 노드의 맨끝은 항상 RR 아님 rr임)을 확인한다.
        while len(lst) > 0:
            num = lst.pop()
            if num == 0:
                check = True
                answer.append("RR")
                break
            elif num == 3:
                check = True
                answer.append("rr")
                break
        # 한번도 RR,rr 을 못만났으면 그건 Rr이다.
        if check == False:
            answer.append("Rr")

    return answer