
v=int(input())
'''vote=input()

vote_list=list(vote)
a_count=vote_list.count("A")
b_count=vote_list.count("B")
if a_count>b_count:
    print("A")
elif a_count<b_count:
    print("B")
else:
    print("Tie")'''


vote=list(str(input()))
A=0
B=0
for i in vote:
    if i =="A":
        A+=1
    else:
        B+=1
if A>B:
    print("A")
elif A==B:
    print("Tie")
else:
    print("B")

