# def solution(numbers):
#     answer = ''
#
#     lst = []
#     for i in numbers:
#         if i // 10 == 0:
#             lst.append((str(i * 100+99), i))
#         elif i // 100 == 0:
#             lst.append((str(i * 10+9), i))
#         else:
#             lst.append((str(i),i))
#
#     print(lst)
#
#     lst.sort(key=lambda x: (-int(x[0][0]), -int(x[0][1]), -int(x[0][2])))
#     print(lst)
#
#     for fake_val, real_val in lst:
#         answer += str(real_val)
#     print(answer)
#     return answer

# 문자열 sort는 맨 앞 요소부터 차례로 비교한다.
# *3을 하는 이유는 아래의 예시를 보자
# s = ['9', '66', '6', '60', '22', '2', '10']
# s[0]*3 -> '999' s[1]*3 -> '666666' s[2]*3 -> '666' s[3]*3-> '606060'
# 1,2,3 인덱스를 비교해보면 가장 큰 숫자를 만들기 위해 6 66 60 혹은 66 6 60 이다. 그러면 이걸 비교하기 위해서 3을 곱하는 것이다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) #마지막에 str int는 '0000' 같은 걸 '0'으로 바꾸기 위해

print(solution([0, 000, 0000]))