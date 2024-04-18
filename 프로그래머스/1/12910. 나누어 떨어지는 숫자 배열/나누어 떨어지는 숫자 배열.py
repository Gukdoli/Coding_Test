def solution(arr, divisor):
    answer = []
    no = [-1]
    for i,j in enumerate(arr):
        if j % divisor == 0:
            answer.append(arr[i])
    
    if len(answer) == 0:
        return no
        
    return sorted(answer)