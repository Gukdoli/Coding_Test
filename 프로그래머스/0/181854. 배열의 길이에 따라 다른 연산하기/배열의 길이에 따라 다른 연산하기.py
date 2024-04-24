def solution(arr, n):
    answer = []
    for i,j in enumerate(arr):
        
        if len(arr) % 2 == 0:
            if i % 2 != 0:
                j += n
        else:
            if i % 2 == 0:
                j += n
        answer.append(j)
    return answer