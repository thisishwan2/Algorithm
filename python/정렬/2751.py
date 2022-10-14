#sorted 이용
'''import sys
input=sys.stdin.readline

n=int(input())
list1=[]

for i in range(n):
    list1.append(int(input()))

for i in sorted(list1):
    print(i)
'''
#병합정렬을 이용하여
def merge_sort(array):
    if len(array)<=1:
        return array
    #재귀함수를 이용하여 끝까지 분할한다.    
    mid = len(array)//2
    #left는 0부터 mid전까지
    left=merge_sort(array[:mid])
    #right는 mid부터 끝까지
    right=merge_sort(array[mid:])

    i,j,k=0,0,0
    arr=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    
    #while문 빠져 나온 후, left혹은 right에 남은 요소들 arr에 넣어주기
    arr += left[i:] 
    arr += right[j:]
 
    return arr

N = int(input())
arr=[]

for _ in range(N):
  arr.append(int(input()))

arr = merge_sort(arr)

for i in arr:
  print(i)