while True:
    n=int(input())
    list=[]
    if n!=-1:
        for i in range(n):
            if n!=i+1:
                if n%(i+1)==0:
                    list.append(i+1)
    else:
        break

    if n==sum(list):
        print(n,"=" ," + ".join(map(str, list)))

    else:
        print(n, "is NOT perfect.")