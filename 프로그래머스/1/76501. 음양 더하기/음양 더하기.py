def solution(absolutes, signs):
    answer = 0
    for i,j in enumerate(signs):
        if j:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
        
    return answer