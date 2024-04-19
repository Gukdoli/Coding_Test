def solution(s):
    a=str(s)
    answer = []
    for i in range(len(a)):
        answer.append(a[i])
        
    return ''.join(sorted(answer,reverse=True))