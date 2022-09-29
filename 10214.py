t=int(input())

for _ in range(t):
    y=0
    k=0
    for _ in range(9):
        y_score,k_score=map(int, input().split())
        y+=y_score
        k+=k_score
    if y>k:
        print("Yonsei")
    elif y<k:
        print("Korea")
    else:
        print("Draw")
