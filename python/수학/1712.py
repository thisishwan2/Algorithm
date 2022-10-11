import sys

a,b,c = map(int, sys.stdin.readline().split(" "))


if c-b<=0:      #대당 b의 값이 c보다 크면 수익이 날 수 없는구조
    print(-1)
else:
    print(int(a/(c-b)+1))   #a/c-b로 손익분기점이 되는 대수를 구하고 +1 해야 수익권
