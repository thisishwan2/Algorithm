import sys
input=sys.stdin.readline
import heapq

n=int(input())

left=[] #최대힙
right=[] #최소힙

for _ in range(n):
    num=int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    if right and -left[0]>right[0]:
        leftv= heapq.heappop(left)
        rightv= heapq.heappop(right)

        heapq.heappush(left, -rightv)
        heapq.heappush(right, -leftv)
    
    print(-left[0])
