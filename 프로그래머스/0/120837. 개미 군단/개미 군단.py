def solution(hp):
    answer = 0
    a = hp // 5
    hp -= a * 5
    answer += a
    b = hp // 3
    hp -= b * 3
    answer += b
    c = hp // 1
    hp -= c * 1
    answer += c
    return answer