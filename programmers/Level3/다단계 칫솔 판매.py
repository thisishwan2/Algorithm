def solution(enroll, referral, seller, amount):
    hierachy = {}
    for i in enroll:
        hierachy[i] = []
    for name, ref in zip(enroll, referral):

        if ref == "-":
            hierachy[name] = "center"
        else:
            hierachy[name] = ref

    point = {'center': 0}
    for i in enroll:
        point[i] = 0

    count = 0
    for seller_name, price in zip(seller, amount):
        count += 1
        total_price = price * 100

        while seller_name != 'center':
            if total_price >= 10:  # 절사할 수 있는 경우
                my_money = total_price - int(total_price * 0.1)
                point[seller_name] += my_money
                total_price = int(total_price * 0.1)
                seller_name = hierachy[seller_name]
            else:
                # 절사하지 않고 마무리
                point[seller_name] += total_price
                break

        if seller_name == 'center':
            point[seller_name] += total_price

    answer = []
    for i in point.keys():
        if i == 'center':
            continue
        answer.append(point[i])
    return answer

'''
간결한 풀이

import math

def solution(enroll, referral, seller, amount):

    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    
    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]

        while True :
            if earn < 10 : #10원 단위 이하라면 모두 받고 레퍼럴 종료
                answer[target] += earn
                break
            else : #10% 레퍼럴을 제외하고 받는다
                answer[target] += math.ceil(earn * 0.9)
                if parentTree[target] == "-": #상위가 없다면 종료
                    break
                earn = math.floor(earn*0.1)
                target = parentTree[target]
                    
    return list(answer.values())

'''