import sys
input = sys.stdin.readline

#이분 탐색 로직
def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return (1)
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
    #수를 못찾으면 0을 반환
    return (0)

n=int(input())
arr=list(map(int, input().split()))
arr=sorted(arr)
m=int(input())
target=list(map(int, input().split()))

for i in target:
    res=binary_search(arr,i,0,n-1)
    print(res)