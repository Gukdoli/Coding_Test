def solution(n):
    answer = 0
    if int(n ** (1/2)) == n ** (1/2):
        answer = int(n ** (1/2) + 1) ** 2
    else:
        return -1
    return answer