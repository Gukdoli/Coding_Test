def solution(num_list, n):
    answer = []
    answer.append(num_list[n:])
    answer.append(num_list[:n])
    return sum(answer, [])