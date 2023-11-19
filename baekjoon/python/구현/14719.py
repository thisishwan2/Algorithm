#14719

import sys
input=sys.stdin.readline

h,w=map(int, input().split())

height=list(map(int, input().split()))

area=[[0 for j in range(w)]for i in range(h)]

for j in range(w):
    count=0
    for i in range(h-1,-1,-1):
        if count==height[j]:
            break
        area[i][j]=1
        count+=1

count=0
start=0
idx=[]
for i in area:
    if len(idx) == 2:
        count += (idx[-1] - idx[-2] - 1)
    idx=[]
    for j in range(len(i)):

        if len(idx)==2:
            count+=(idx[-1]-idx[-2]-1)
            idx.pop(-2)

        if i[j]==1:
            idx.append(j)

print(count)

'''
h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)

'''