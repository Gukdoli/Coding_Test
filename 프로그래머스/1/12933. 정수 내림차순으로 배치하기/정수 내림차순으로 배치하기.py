def solution(n):
    answer = []
    a = str(n)
    for i in range(len(a)):
        answer.append(a[i])
    b = sorted(answer, reverse=True)
    c = int(''.join(b))
    return c