#골드바흐 추측
#나의 풀이(시간초과)
'''
t=int(input())

for _ in range(t):
    n=int(input())  #짝수
    list1=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            list1.append(i)
    pati=10000
    for a in list1:
        for b in list1:
            if a+b==n:
                pati=min(abs(a-b),pati)
                if a<=b:
                    gold=a,b
    print(gold)
    '''

#매우 간단한 풀이
#입력받은 n을 반으로 쪼개고 하나는 +1, 나머지 하나는 -1을 해주면서 두수가 모두 소수인지 확인해 보는 것이다.
#반을 쪼갰기 때문에 제일 처음 소수로 판별나는 것이 차가 가장 작은 소수다.

#소수를 구하는 함수
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())

    a,b =n//2 , n//2    #n은 짝수이므로 반을 쪼갠다.
    while True:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1