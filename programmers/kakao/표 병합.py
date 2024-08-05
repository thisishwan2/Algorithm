def update_r_c(r, c, value, chart, pointer):
    # 포인터가 가르키는 그룹 = 머지된 혹은 개별 그룹 을 update
    for x,y in pointer[(r,c)]:
        chart[x][y] = value

def update_value(val1, val2, chart):
    for i in range(51):
        for j in range(51):
            if chart[i][j] == val1:
                chart[i][j] = val2

def merge(r1, c1, r2, c2, chart, pointer):
    # r1,c1이 "" 이 아닌 경우에는 r1,c1 값으로 다른 것들을 변경
    if chart[r1][c1] != "":
        pointer[(r1,c1)] = list(pointer[(r1,c1)] + pointer[(r2,c2)]) # 두 포인터 배열이 가르키는 값을 합쳐준다.
        for x,y in pointer[(r1,c1)]:
            # r1,c1 포인터 딕셔너리의 요소들이 모두 같은 value(집합)을 갖도록 한다.
            pointer[(x,y)] = pointer[(r1,c1)]
            chart[x][y] = chart[r1][c1]

    # r2,c2가 ""이 아닌 경우 혹은 둘다 빈칸인 경우(이 경우에는 아무거나 잡고 merge 해도 되긴함.)
    else:
        pointer[(r2, c2)] = list(set(pointer[(r1, c1)] + pointer[(r2, c2)]))  # 두 포인터 배열이 가르키는 값을 합쳐준다.(set 처리를 해야 하는 이유는 같은 그룹에 속한 경우의 중복을 제거)
        for x, y in pointer[(r2, c2)]:
            # r1,c1 포인터 딕셔너리의 요소들이 모두 같은 value(집합)을 갖도록 한다.
            pointer[(x, y)] = pointer[(r2, c2)]
            chart[x][y] = chart[r2][c2]

def unmerge(r1,c1,chart, pointer):
    for x,y in pointer[(r1,c1)]:
        pointer[(x,y)] = [(x,y)]
        if (x,y)!=(r1,c1):
            chart[x][y]=""

def solution(commands):
    answer = []
    chart = [["" for _ in range(51)] for _ in range(51)]

    # r,c 좌표가 가르키고 있는 그룹의 좌표들
    pointer = {}
    for i in range(51):
        for j in range(51):
            pointer[(i,j)] = [(i,j)]

    for command in commands:
        cmd_list = command.split()

        if cmd_list[0] == "UPDATE" and len(cmd_list) == 4:
            x, y, value = int(cmd_list[1]), int(cmd_list[2]), cmd_list[3]
            update_r_c(x, y, value, chart, pointer)

        elif cmd_list[0] == "UPDATE" and len(cmd_list) == 3:
            val1, val2 = cmd_list[1], cmd_list[2]
            update_value(val1, val2, chart)

        elif cmd_list[0] == "MERGE":
            x1, y1, x2, y2 = int(cmd_list[1]), int(cmd_list[2]), int(cmd_list[3]), int(cmd_list[4])
            merge(x1, y1, x2, y2, chart, pointer)

        elif cmd_list[0] == "UNMERGE":
            x1, y1 = int(cmd_list[1]), int(cmd_list[2])
            unmerge(x1,y1,chart, pointer)

        else:
            x, y = int(cmd_list[1]), int(cmd_list[2])
            if chart[x][y] == "":
                answer.append("EMPTY")
            else:
                answer.append(chart[x][y])
    print(answer)
    return answer

# solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
#solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])
#solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 3 3", "UNMERGE 1 1", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]) #["A","EMPTY","EMPTY","EMPTY"]
#solution(["MERGE 1 1 2 2", "PRINT 1 1"]) # ["EMPTY"]
#solution(["MERGE 1 1 2 2", "UPDATE 1 1 A", "UNMERGE 1 1", "PRINT 1 1", "PRINT 2 2"]) #  ['A', 'EMPTY']
#solution(["MERGE 1 1 2 2", "MERGE 1 1 3 3", "UPDATE 3 3 A", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]) # ["A", "A", "A"]
#solution(["MERGE 1 1 1 2","MERGE 1 2 1 1", "PRINT 1 1"])
#solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"])
# solution(["UPDATE 1 1 안녕", "MERGE 1 1 2 2", "MERGE 3 3 2 2", "PRINT 3 3", "PRINT 1 1"])
