'''N = int(input())
i=2
while N !=1:
    if N%i==0:
        print(i)
        N=N//i
    else:
        i=i+1'''
#다시보자

n=int(input())

for i in range(2,n+2):
    while n%i==0:
        print(i)
        n=n//i