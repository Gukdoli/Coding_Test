def solution(n):
    a = str(n)
    answer = []
    for i in range(len(a)):
        answer.append(int(a[i]))
    answer.reverse()
    return answer
