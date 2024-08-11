import heapq

n=int(input())
arr = []
for i in range(n):
    si,ti = map(int, input().split())
    arr.append([si,ti])

arr.sort()

q=[]
heapq.heappush(q, arr[0][1])

# heapq는 항상 정렬된 상태를 갖는것이 아니고, 가장 작은 값(min heap)을 빠르게 가져오는 자료구조임.
for i in range(1,n):
    if arr[i][0]<q[0]:
        heapq.heappush(q,arr[i][1])

    else:
        heapq.heappop(q)
        heapq.heappush(q, arr[i][1])
print(len(q))