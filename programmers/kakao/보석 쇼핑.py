# 두 풀이 둘다 n*m의 시간복잡도를 갖는다.
# 다만 둘의 차이는 투포인터의 경우 특정 범위를 탐색할때 쓰면 좋다. 이 경우도 투포인터롤 푸는게 좀 더 효율적이다.

def solution(gems):
    gem_dic = {}
    answer = []
    start = 0
    end = 0
    for idx, val in enumerate(gems):

        if val not in gem_dic.keys():
            gem_dic[val] = idx
            end = idx
            answer = [start + 1, end + 1]
        else:
            gem_dic[val] = idx
            end = idx
            if gems[start] == gems[idx]:
                mini = 1000000
                for j in gem_dic.values():
                    mini = min(mini, j)
                start = mini
                if (answer[1] - answer[0] > end - start):
                    answer = [start + 1, end + 1]
    return answer



'''
첫 번째 풀이.
for 문과 * max, min 부분에서 n*m 이 된다.

def solution(gems):
    
    n = []
    for i in gems:
        if i not in n:
            n.append(i)
    cnt = len(n)
    
    
    gems_dict={}
    answer=[]
    for idx, val in enumerate(gems):
        
        is_first = True
        
        gems_dict[val]= idx
        
        if len(gems_dict)== cnt:
            if is_first == True:
                tmp = gems_dict.values()
                is_first = False
                
                start = min(tmp)
                end = max(tmp)
                answer.append([end-start,start,end])
                continue
            
            else:
                if tmp != gems_dict.values(): # 변경점이 생기면
                    tmp = gems_dict.values()
                    start = min(tmp)
                    end = max(tmp)
                    answer.append([end-start,start,end])
                    continue
    
    ans = sorted(answer, key = lambda x:x[0])
    ans = ans[0]
    answer = [ans[1]+1, ans[2]+1]
    return answer

'''