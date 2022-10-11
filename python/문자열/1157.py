word = input().upper()  #대문자로 변경
list=list(set(word))    #중복없애고 리스트로 변환
cnt_list=[]             #카운트 리스트 생성
for i in list:          #중복 없는 문자열 하나씩 넣기
    cnt=word.count(i)   #count 메서드를 이용하여 중복된 횟수 cnt에 저장
    cnt_list.append(cnt)#중복된 횟수를 리스트에 저장
if cnt_list.count(max(cnt_list))>1: #중복횟수가 1이상 즉, 중복횟수가 같은 문자열이 있을시
    print("?")
else:
    index=cnt_list.index(max(cnt_list)) #최대 중복횟수의 인덱스를 얻는다
    print(list[index])
    #갯수 리스트 인덱스 = set 인덱스
    
