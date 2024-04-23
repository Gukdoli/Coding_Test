def solution(money):
    answer = [0,0]
    if money / 5500 == 1:
        answer = [1,0]
    else:
        answer = [int(money/5500), money % 5500]
    return answer