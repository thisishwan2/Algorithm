m=int(input())
n=int(input())
num=[]
i=1

while i**2<=n:          #i제곱이 n이하일때 수행되는 while
    if m<=i**2<=n:      #i제곱이 m과 n사이일때
        num.append(i**2)#그때의 i제곱값을 리스트에 추가
    i+=1                #i 증가
if num==[]:
    print(-1)
else:
    print(sum(num))
    print(num[0])

'''내가 처음 구상한 풀이와 비슷한 방법
m = int(input())
n = int(input())
 
num = []
for i in range(m, n+1):
    root = int(i ** 0.5)            #i제곱근을 정수로 변경한다
    if i == root ** 2:num.append(i) #그 값을 다시 제곱했을때 i와 같으면 리스트에 추가
 
if num == []:
    print(-1)
else:
    print(sum(num))
    print(num[0])
'''