t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    maxi = 0
    total_price = 0

    # 미래의 가격부터 순차적으로 탐색해서 차익을 실현한다.
    for i in range(n-1,-1,-1):
        if price[i]>maxi:
            maxi=price[i]
        else:
            total_price += maxi - price[i]
    print(total_price)