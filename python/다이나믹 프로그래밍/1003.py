# #1003
# #시간 초과 -> 메모이제이션 사용!

#메모이제이션
import sys
input=sys.stdin.readline

t=int(input())

# n번째 피보나치 수일때, 0과 1이 몇번씩 더해졌는지 확인하기 위해, 0과 1을 카운트 하는 리스트를 각각 만들어주고,
# 피보나치 원리를 생각해서, i-1, i-2번째의 값을 더하면, 0과 1이 몇번쓰였는지 알 수 있다.
def fibo(n):
    for i in range(2,n+1):
        cnt_0.append(cnt_0[i-2]+cnt_0[i-1])
        cnt_1.append(cnt_1[i-2]+cnt_1[i-1])
    print(cnt_0[n],cnt_1[n])

for _ in range(t):
    n=int(input())
    cnt_0=[1,0]
    cnt_1=[0,1]
    fibo(n)

"---------------------------["
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**6)

# t=int(input())

# def fibo(n):
#     global zero
#     global one
    
#     if n==0:
#         zero+=1
#         return 0
#     elif n==1:
#         one+=1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# for _ in range(t):
#     zero=0
#     one=0
#     n=int(input())
#     fibo(n)
#     print(zero, one)

"-----------------------"