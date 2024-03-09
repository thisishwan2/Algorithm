# 첫 풀이 방식 8,10 번 시간초과
# max 는 o(n) 복잡도를 가짐

# def solution(number, k):
#     answer = ''
#     start = 0
#     end = k + 1
#
#     for i in range(len(number) - k):
#
#         if ((len(number[start:])) == (k - len(answer))):
#             answer += number[start:]
#             break
#
#         tmp = list(map(int, number[start:end]))
#
#         max_val = max(tmp)
#
#         answer += str(max_val)
#         start = start + tmp.index(max_val) + 1
#         end = end + 1
#
#     return answer

def solution(number, k):
    stack = []

    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1

        stack.append(i)

    return ''.join(stack[:len(number) - k])