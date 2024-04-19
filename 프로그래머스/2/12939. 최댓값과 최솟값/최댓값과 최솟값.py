def solution(s):
    answer = []
    a = s.split(" ")
    print(a)
    for i in range(len(a)):
        answer.append(int(a[i]))
    return f'{min(answer)} {max(answer)}'
