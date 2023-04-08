#나의 풀이 
#너무 꼬아서 생각해ㅛ다.
import sys

nan_tall=[] #난쟁이 키를 담는 리스트
a=[]        #복사하기 위한 빈 리스트

# a와 nan_tall에 키를 담는다.
for _ in range(9):
    num=int(sys.stdin.readline().rstrip())
    nan_tall.append(num)
    a.append(num)


for i in range(9):
    a.pop(i)    #요소 하나를 없애고
    for j in range(8):
        a.pop(j)    #다른 요소도 하나 없앤다.
        if sum(a)==100:
            nan_tall.pop(i)
            nan_tall.pop(j)
            break
        else:
            a=nan_tall.copy()
            a.pop(i)
    if sum(nan_tall)==100:
        break
    a=nan_tall.copy()   #내부 for문이 끝나면 다시 원복된 리스트가 있어야되므로

nan_tall.sort()

for i in nan_tall:
    print(i)

#다른 풀이
n = 9
temp1, temp2 = 0, 0
arr = [int(input()) for _ in range(n)]
 
for i in range(n):
    for j in range(i+1, n):
        #전체 리스트의 합에서 두 요소를 뺀게 100과 같으면
        if sum(arr) - (arr[i] + arr[j]) == 100:
            #변수에 각 값을 저장
            temp1 = arr[i]
            temp2 = arr[j]


arr.remove(temp1)
arr.remove(temp2)
 
print('\n'.join(map(str, sorted(arr))))