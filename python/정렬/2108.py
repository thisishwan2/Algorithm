import sys
#산술평균
def avg(a):
    average=round(sum(a)/len(a))
    return average
#중앙값
def mid(a):
    middle=len(a)//2
    a=sorted(a)
    return a[middle]
#최빈값(시간초과가 나온다. 그 이유는 .count를 사용하면 시간초과가 된다.)
'''def max_cnt(a):
    b=sorted(list(set(a)))
    dic={}
    max_list=[]
    for i in b:
        dic[i]=a.count(i)
    max_cnt=max(dic.values())
    if len(b)==1:
        return b[0]
    elif max_cnt==1:
        return b[1]
    else:
        for key, value in dic.items():
            if value==max(dic.values()):
                max_list.append(key)
        if len(max_list)==1:
            return max_list[0]
        else:
            return max_list[1]'''
#범위
def range_num(a):
    return max(a)-min(a)


input=sys.stdin.readline
n=int(input())
num_list=[]
for i in range(n):
    num=int(input())
    num_list.append(num)

print(avg(num_list))
print(mid(num_list))
print(max_cnt(num_list))
print(range_num(num_list))
#최빈값
def max_cnt(a):
    dic={}
    #빈 딕셔너리에 i가 있을시 +1(중복값 증가), 없으면 1을 저장
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    #최빈값 저장
    max_value=max(dic.values())
    #최빈값에 해당하는 key값을 넣을 리스트 생성
    max_key=[]
    #.items()메서드를 통해 key값과 value값을 각각 할당
    for key,value in dic.items():
        #만약 해당 value의 값이 최빈값이면
        if value==max_value:
            #추가
            max_key.append(key)
    #최빈값 key만 있는 리스트 정렬
    result=sorted(max_key)
    #최빈값이 하나면
    if len(result)==1:
        return result[0]
    #1개 이상이먄
    else:
        return result[1]