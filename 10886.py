n=int(input())
not_cute=0
cute=0
for i in range(n):
    opinion=int(input())
    if opinion ==1:
        cute+=1
    else:
        not_cute+=1
if not_cute>cute:
    print("Junhee is not cute!")
elif cute>not_cute:
    print("Junhee is cute!")