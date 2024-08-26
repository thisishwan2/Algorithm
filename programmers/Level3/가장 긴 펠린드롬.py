def isPalindrome(str):
    if str == str[::-1]:
        return True
    return False


def solution(s):
    answer = 1

    # 2중 for문으로 해결가능

    # 첫 for문은 시작점을 두번째 for문은 끝점을 잡고, 배열을 뒤집어서 검사
    for start in range(len(s)):
        for end in range(len(s), start - 1, -1):
            if (isPalindrome(s[start:end])):
                answer = max(answer, end - start)

    return answer