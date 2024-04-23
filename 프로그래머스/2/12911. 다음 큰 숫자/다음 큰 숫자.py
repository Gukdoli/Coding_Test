def solution(n):
    b=bin(n)
    a = ''
    for i in range(n+1,1000001):
        a = bin(i)
        if a.count('1') == b.count('1'):
            return i
    return b