t=int(input())

for i in range(t):
    s_lsit=[]
    l_list=[]
    n=int(input())
    for j in range(n):
        s,l=input().split()
        l=int(l)
        s_lsit.append(s)
        l_list.append(l)
    a=l_list.index(max(l_list))
    print(s_lsit[a])

"""딕셔너리로 푸는법
t=int(input())

for - in range(t):
    dic={}
    n=int(input())
    for _ in range(n):
        s,l=input().split()
        dic[s]=int(l)
    swap_dic=dict(zip(dic.values(),dic.keys()))  #dict로 새 딕셔너리 생성, zip으로 두 리스트를 묶어줌. 키랑 밸류의 위치를 변경함
    print(swap_dic[max(swap_dic)])  #swap_dic의 키 값의 최대를 구해 벨류를 구함    
"""
#쉬운 풀이
"""T = int(input())
for _ in range(T):
    N = int(input())
    max = 0
    mName = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            mName = name
    print(mName)
"""