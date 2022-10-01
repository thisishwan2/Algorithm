#처음 푼 코드 꼭 함수형태로 안풀어도 된다.
def self10000():
    res=set()
    a=set()
    for i in range(1,10001):
        a.add(i)
        if i<10:
            di=i+i
            res.add(di)
        elif i<100:
            i=str(i)
            di=int(i)+int(i[0])+int(i[1])
            res.add(di)
        elif i<1000:
            i=str(i)
            di=int(i)+int(i[0])+int(i[1])+int(i[2])
            res.add(di)
        elif i<10000:
            i=str(i)
            di=int(i)+int(i[0])+int(i[1])+int(i[2])+int(i[3])
            res.add(di)
    selfNum=a-res
    var=list(selfNum)
    var.sort()
    i=0
    while i<len(var):
        
        print(var[i])
        i+=1

self10000()

#간략한 풀이
nat_num=set(range(1,10001))
gen_num=set()

for i in range(1,10001):            # i=33
    for j in str(i):                # '3' '3'
        i+=int(j)                   # i=33+3 -> i= (33+3)+3
    gen_num.add(i)                  # 생성자 있는 숫자를 추가

self_num=sorted(nat_num-gen_num)    #차집합을 이용후 정렬
for i in self_num:
    print(i)

#list활용
numbers = list(range(1, 10001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)