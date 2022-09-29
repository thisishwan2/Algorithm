k, n, m = map(int,input().split())

money=m-k*n
if money<0:
    print(abs(money))
else:
    print(0)
    