#9095
#n을 1,2,3 의 합으로 나태내는 방법의 수
from itertools import product

t=int(input())

for _ in range(t):
    n=int(input())
    a=[[1,2,3]]
    cnt=0

    for i in range(1, n-1):
        lst=list(product(*a))
        
        for j in lst:
            if sum(j)==n:
                cnt+=1
        a.append([1,2,3])
    

    print(cnt+(n-1)+1)

"-------------------------------------"
#좀 더 구현한 코드
import itertools
t=int(input())
for i in range(t):
    b=int(input())
    list1=[]
    for j in range(b+1):
        #product(반복가능한 객체, repeat=): 중복을 허용해서 반복가능한 객체중 reapet 횟수만큼 뽑는 경우를 구한다.
        # repeat이 1이어도 a 리스트는 생성된다.(product는 두개이상의 리스트일때만 되는 줄알았는데 아니었디.) 
        a=list(itertools.product(range(1,4), repeat = j+1))
        for k in a:
            if sum(k)==b:
                list1.append(k)
    print(len(list1))