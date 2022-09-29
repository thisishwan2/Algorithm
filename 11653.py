#최초 코드
N = int(input())
i=2
while N !=1:
    if N%i==0:
        print(i)
        N=N//i
    else:
        i=i+1


#더 쉬운 풀이

'''n=int(input())

for i in range(2,n+2):
    while n%i==0:
        print(i)
        n=n//i'''