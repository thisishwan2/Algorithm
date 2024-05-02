# 이모티콘 플러스 가입자를 최대한 늘린다
# 그 다음 판매액을 최대한 늘린다.
# 이모티콘 할인율은 10,20,30,40 중 하나

sales = [10, 20, 30, 40]
candi = [] # 중복 순열을 이용하여 모든 경우의 수를 담을 리스트

def dfs(lst, n):  # 중복 순열

    if len(lst) == n:
        candi.append(lst[:])
        return

    for i in sales:
        lst.append(i)
        dfs(lst, n)
        lst.pop()

def solution(users, emoticons):  # users=[비율, 가격], emotions = 이모티콘 정가

    # emotions의 개수만큼 10,20,30,40이 설정될 모든 경우의 수를 따진다.
    # 최악의 경우 4**7 이다.(16384)
    n = len(emoticons)
    dfs([], n)

    price = []
    # 각 이모티콘에 대해 [할인 가격, 할인률] 형태로 담음
    for sale in candi: # 16384
        tmp = []
        # 이모티콘 정가에 할인율을 적용한 가격과 할인율을 리스트에 담는다.
        for sale_per, emo_pri in zip(sale, emoticons):
            tmp.append([int(emo_pri * (100 - sale_per) * 0.01), sale_per])
        price.append(tmp)

    # 최악의 경우 천만번 실행
    answer = []
    # 각 이모티콘 할인률의 경우를 따진다.
    for emoticon_list in price:
        res = [0, 0]  # 이모티콘 플러스 가입자, 이모티콘 판매액
        for user in users:
            buy_price = 0
            user_buy_per = user[0]
            user_limit_price = user[1]

            for emoticon in emoticon_list:  # 유저별로 구매하는 이모티콘을 확인한다.
                emoticon_price = emoticon[0]
                per = emoticon[1]

                # 유저는 자신이 지정한 할인률 이상의 이모티콘만 구매함
                if user_buy_per <= per:  # 구매
                    buy_price += emoticon_price
            # 만약 구매액이 유저 한계 금액이상이면, 유저는 이모티콘 플러스에 가입
            if user_limit_price <= buy_price:
                res[0] += 1
            # 그게 아니면, 판매액을 증가시킨다.
            else:
                res[1] += buy_price
        answer.append(res)

    answer = sorted(answer, key=lambda x: (x[0], x[1]))[-1]  # 2번 테케에서 60이 빈다.
    return answer