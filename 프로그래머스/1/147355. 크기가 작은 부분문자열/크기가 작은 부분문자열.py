def solution(t, p):
    answer = 0
    a = []
    n = len(t)-len(p)
    if p != 1:
        for i in range(n+1): 
            a.append(t[i:(len(p)+i)])
            if a[i] <= p:
                answer +=1
        

    return answer