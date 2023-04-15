import sys
input=sys.stdin.readline

#수들의 범위가 시간초과를 야기할수 있다. k=10**8 p=10**8 n=10**6
# 최악의 경우 (10**8)*(10**8)**(10**6) 1억*(1억)**(백만)

k,p,n=map(int, input().split())

for _ in range(n):
    k=k*p
    k=k%1000000007
print(k)

#주어진 범위와 시간, 메모리를 고려하는것을 까먹지 말자.