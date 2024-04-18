def solution(num):
    if num == 1:
        return 0
    answer = -1
    for i in range(1, 501):
        if num % 2 == 0:
            num = num / 2
        elif num % 2 != 0:
            num = num * 3 + 1
        if num == 1:
            answer = i
            break

    return answer