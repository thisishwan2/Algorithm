import heapq
n,k = map(int, input().split())

jewel = []
for _ in range(n):
    m,v = map(int, input().split()) # 무게, 가격
    jewel.append([m,v])

jewel = sorted(jewel, key=lambda x:(x[0],-x[1]))
# print(jewel)

hq=[]
for _ in range(k):
    c = int(input())
    heapq.heappush(hq, c)

idx=0
answer = 0
max_price = []
while hq:
    c = heapq.heappop(hq)
    while True:
        if idx<len(jewel) and c>= jewel[idx][0]:
            heapq.heappush(max_price, -jewel[idx][1])
            idx += 1
        else:
            break
    if max_price:
        answer += heapq.heappop(max_price)*-1
print(answer)