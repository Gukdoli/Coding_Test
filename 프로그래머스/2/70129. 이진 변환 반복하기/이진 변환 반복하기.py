def solution(s): 
    answer = [0,0]
    a =''
    while s != '1':
        answer[1] += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
        answer[0] += 1
            
    return answer