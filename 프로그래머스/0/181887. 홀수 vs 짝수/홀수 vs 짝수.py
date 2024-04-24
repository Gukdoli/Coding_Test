def solution(num_list):
    a = 0
    b = 0
    for i,j in enumerate(num_list):
        if i % 2 ==0:
            a += j
        else:
            b += j
    if a > b:
        return a
    else:
        return b
        
    return 