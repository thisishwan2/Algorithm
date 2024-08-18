import heapq
n,m = map(int, input().split()) # n: 카드의 개수, m: 합체 횟수
card = list(map(int, input().split())) # 초기 카드의 상태

hq = []
for i in card:
    heapq.heappush(hq,i)
for _ in range(m):
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)
    heapq.heappush(hq, num1+num2)
    heapq.heappush(hq, num1 + num2)
print(sum(hq))
