def recursion(word, a, b, cnt):
    if((a>=b)):
        return str(1), str(cnt)
    elif(word[a]!=word[b]):
        return str(0), str(cnt)
    else:
        cnt+=1
        return recursion(word, a+1, b-1, cnt)


        

def isPalindrome(word):
    return recursion(word, 0, len(word)-1, 1)


n=int(input())
for _ in range(n):
    word=input()
    print(" ".join(isPalindrome(word)))

# 더 빠른 코드

import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        S = sys.stdin.readline().rstrip()
        for l, r, i in zip(S, reversed(S), range(1, len(S))):
            if l != r:
                print(0, i)
                break
        else:
            print(1, len(S) // 2 + 1)

# name이 main일때만 실행(즉 다른 파일에서는 실행하지 않음)
if __name__ == '__main__':
    main()