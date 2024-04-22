def solution(s):
    answer = []
    
    a = s.split(" ")
    for i in a:
        for j in range(len(i)):
            if j == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
            
    return ''.join(answer[:-1])