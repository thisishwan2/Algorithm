# 1중 for 문으로 해결
# def solution(phone_book):
#     phone_book = sorted(phone_book)
#     answer = True
#
#     for i in range(len(phone_book) - 1):
#
#         if phone_book[i + 1].startswith(phone_book[i]): #startswith 함수를 활용해서 접두어를 확인
#             answer = False
#             break
#
#     return answer

# 이렇게 풀어도 o(n^2)이 아님 왜냐면 전화번호 길이가 20자로 제한이라 최대 20000000 임
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: # 마지막 조건은 자기 자신이 == 되는 경우를 제외한것
                answer = False
    return answer

solution(["119", "97674223", "1195524421"]	)