def solution(arr):
    answer = [-1]
    if len(arr) == 1:
        return answer
    else:
        c = min(arr)
        arr.remove(c)
    return arr