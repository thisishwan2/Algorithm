#이 문제는 다시보고 기억하기


n=int(input())
list=[]
for _ in range(n):
    name,d,m,y=input().split()
    d,m,y=int(d),int(m),int(y)
    birth=y,m,d,name
    list.append(birth)
list.sort()             #list맨 뒤에 name(문자열)이 있어도 오름차순 정렬됨)
print(list[-1][-1])     #맨뒤 리스트(나이 젤 어린) 중에 맨뒤의(name)출력
print(list[0][-1])      #맨 앞의 리스트(나이 젤 많은)중에 맨뒤의(name)출력
