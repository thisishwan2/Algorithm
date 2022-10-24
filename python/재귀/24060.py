import sys
input=sys.stdin.readline

def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid= (len(arr)+1)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i,j = 0,0
    array=[]
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            array.append(right[j])
            ans.append(right[j])
            j+=1
            
        else:
            array.append(left[i])
            ans.append(left[i])
            i+=1
    #위의 while문 돌고 남은 요소들 저장해주는 방법
    while i<len(left):
        array.append(left[i])
        ans.append(left[i])
        i+=1
    while j<len(right):
        array.append(right[j])
        ans.append(right[j])
        j+=1
    '''
    array+= left[i:]
    ans.append(left[i:])
    array+= right[j:]
    ans.append(right[j:])'''

    return array








n, k = map(int, input().split())

arr=list(map(int, input().split()))
#저장되는 수들을 저장되는 순서대로 모아놓은 list
ans=[]
merge_sort(arr)

if len(ans)>=k:
    print(ans[k-1])#인덱스를 생각해서 -1한 값 호출
else:
    print(-1)