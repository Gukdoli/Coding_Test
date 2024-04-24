def solution(array):
    answer = []
    for i,j in enumerate(array):
        if j == max(array):
            answer.append(j)
            answer.append(i)
            
    return answer