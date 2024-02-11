def solution(array, commands):
    answer = []
    for lst in commands:
        i = lst[0]
        j = lst[1]
        k = lst[2]

        slice_arr = array[i - 1:j]
        slice_arr.sort()
        answer.append(slice_arr[k - 1])
    return answer