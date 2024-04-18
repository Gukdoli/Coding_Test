def solution(x):
    answer = True
    a=str(x)
    c=0
    for i in range(len(a)):
        c += int(a[i])
    if x % c == 0:
        return True
    else:
        return False
    return answer