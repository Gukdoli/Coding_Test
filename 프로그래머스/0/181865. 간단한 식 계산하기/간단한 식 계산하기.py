def solution(binomial):
    sp = binomial.split(" ")
    answer = 0
    if '+' in sp:
        answer = int(sp[0]) + int(sp[2])
    elif '-' in sp:
        answer = int(sp[0]) - int(sp[2])
    else:
        answer = int(sp[0]) * int(sp[2])
        
        
    return answer