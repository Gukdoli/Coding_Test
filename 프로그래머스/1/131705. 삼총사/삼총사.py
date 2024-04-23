def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for _ in range(j+1, len(number)):
                if number[i] + number[j] + number[_] == 0:
                    answer += 1
    return answer