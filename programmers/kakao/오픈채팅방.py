# 채팅방에서 닉을 변경하는 방법은 나갓다가 다시 들어오거나 닉네임 변경을 함
# 닉네임 변경시에는 기존에 채팅방에 출력되어 있던 메세지 닉도 전부 변경됨
#

def solution(record):  # 입장: Enter, 퇴장 Leave, 변경 Change
    name_dict = {}
    answer = []

    for i in record:
        lst = i.split()
        status = lst[0]
        uid = lst[1]

        # 처음에는 name_dict에 대해서 LEAVE시에 pop 메서드를 진행했음 왜냐면 채팅방에서 나갔으니까?
        # 근데 그러면 나간 행위가 record의 마지막 행위면 그 놈에 대해서는 닉네임이 존재하지 않는 문제가 있음 ㅇㅇ
        if status == "Enter":
            answer.append([uid, "님이 들어왔습니다."])
            name_dict[uid] = lst[2]
        elif status == "Leave":
            answer.append([uid, "님이 나갔습니다."])
        else:
            name_dict[uid] = lst[2]

    # print(answer)
    # print(name_dict)

    result = []
    for uid, action in answer:
        name = name_dict[uid]
        sentence = name + action
        result.append(sentence)
    return result