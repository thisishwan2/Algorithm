n=int(input())
Q1=0
Q2=0
Q3=0
Q4=0
AXIS=0


for i in range(n):
    x,y=map(int, input().split())
    if x>0:
        if y>0:
            Q1+=1
        elif y<0:
            Q4+=1
        else:
            AXIS+=1
    elif x<0:
        if y>0:
            Q2+=1
        elif y<0:
            Q3+=1
        else:
            AXIS+=1
    else:
        AXIS+=1
print("Q1:",Q1,"\nQ2:" ,Q2,"\nQ3:",Q3,"\nQ4:",Q4,"\nAXIS:",AXIS)
