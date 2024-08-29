def solution(cards):
    answer = 0

    # 1~n번 그룹을 넣을 박스 딕셔너리
    box = {}
    open_info = {}  # key = 박스 번호-1

    box_group_num = 1

    while len(open_info) < len(cards):
        for idx, val in enumerate(cards):

            # 아직 안열었다면
            if open_info.get(idx) == None:
                # n번 박스 그룹을 만든다.
                box_group = []
                box_num = idx
                box_group.append(idx)
                open_info[idx] = 1

                while True:
                    next_box_num = cards[box_num]
                    next_box_num -= 1
                    if open_info.get(next_box_num) == None:
                        box_group.append(next_box_num)
                        open_info[next_box_num] = 1
                        box_num = next_box_num
                    else:
                        break
                box[box_group_num] = box_group
                box_group_num += 1
    #print(box)

    val_list = list(box.values())
    if len(val_list) == 1:
        return 0
    val_list = sorted(val_list, key = lambda x:(-len(x)))
    answer = len(val_list[0])*len(val_list[1])


    return answer
solution([8,6,3,7,2,5,1,4]	)