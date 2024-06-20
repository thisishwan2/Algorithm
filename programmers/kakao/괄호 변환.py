# 올바른 괄호 문자열인지를 확인
def collect_word(word):
    # 시작이 ( 이면 올바른 괄호 문자임
    if word[0] == "(":
        return True
    else:
        return False

# 균형잡힌 문자열로 u,v로 분리
def balance(w):
    left = 0
    right = 0

    for idx, val in enumerate(w):
        if val == "(":
            left += 1
        elif val == ")":
            right += 1

        # 균형잡힌 문자열 인지 확인
        if (left != 0 and right != 0) and (left == right):

            # 균형잡힌 문자열 u 생성
            u = w[:idx + 1]

            if len(w) == idx + 1:
                v = ""
            else:
                v = w[idx + 1:]

            return u, v

def recursive(w):
    # 1번 입력이 빈 문자열이면, 빈 문자열을 반환한다.
    if len(w) == 0:
        return ""

    else:
        # 2번 균형잡힌 문자열 u,v로 분리
        u, v = balance(w)

        # 3번 u가 올바른 괄호 문자열인지 확인
        if collect_word(u):
            return u + recursive(v)
        # 4번 문자열 u가 올바른 괄호 문자열이 아닌경우
        else:
            tmp = "("  # 4-1
            tmp += recursive(v)  # 4-2
            tmp += ")"  # 4-3

            for s in u[1:len(u) - 1]:
                if s == '(':
                    tmp += ')'
                else:
                    tmp += '('
            return tmp


def solution(p):
    answer = recursive(p)
    print(answer)
    return answer

solution("(()())()"	)