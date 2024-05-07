def solution(n):
    answer = [n]
    for i in range(1, 1000):
        if n != 1:
            if n % 2 == 0:
                n = n / 2
                answer.append(n)
            else:
                n = 3 * n + 1
                answer.append(n)
    return answer