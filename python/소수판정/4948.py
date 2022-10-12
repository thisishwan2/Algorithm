#시간초과..
'''
while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    for i in range(n+1,2*n+1):
        if i==2:
            cnt+=1
            continue
        else:
            #for-else 구문 이용(for문이 break안되고 다 실행되면, else문 실행)
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    break
            else:
                cnt+=1
    print(cnt)    
'''
#시간을 단축시키기 위해서는 while문 내부에서 소수판별을 위한 에라토스테네스의 공식을 계속해서 돌것이 아니라
# 미리 소수를 판별하는 것이 포인트이다. 

#소수를 구하는 방식을 prime함수로 설정.
def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

list=list(range(2,246912))  #문제의 n의 범위 1~123456의 2배 범위
prime_list=[]

#미리 정해진 범위의 소수를 다 구해서 prime_list에 저장
for i in list:
    if prime(i):    #prime 함수에서 True가 반환되면 그수는 소수
        prime_list.append(i)

#소수의 갯수 판별
while True:
    n=int(input())
    count=0
    if n==0:
        break
    #prime_list(소수 리스트)를 i에 넣어주고, 그 i가 n보다 크고 2*n작거나 같으면 카운트 한다.
    for i in prime_list:
        if n<i<=2*n:
            count+=1
    print(count)
