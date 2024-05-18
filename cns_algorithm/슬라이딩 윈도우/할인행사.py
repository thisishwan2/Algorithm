# 일정 금액 지불시 -> 10일간 회원이 됨
# 회원 대상 매일 한가지 제품 할인
# 할인품은 1일1구매만 가능
# 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치하는 날을 모두 count

# 슬라이딩 윈도우
def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):

        product_dict = {}
        for product, num in zip(want, number):
            product_dict[product] = num

        start = i
        end = i + 10
        for j in discount[start:end]:
            # print(j)
            if j in product_dict.keys():
                product_dict[j] -= 1
                if product_dict[j] == 0:
                    product_dict.pop(j)
        # print(product_dict)
        if len(product_dict) == 0:
            answer += 1

    return answer