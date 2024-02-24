def solution(cards1, cards2, goal):
    answer = 'Yes' #  런타임 에러가 발생하는 이유는 answer 변수가 초기화되지 않은 상태에서 answer 변수를 break문 이후에 사용하기 때문
    for i in goal:
        if 0 < len(cards1) and cards1[0] == i: # cards1 리스트가 비어있는 상태에서 cards1[0]을 접근하려고 하면 인덱스 에러가 발생
            cards1.pop(0)
        elif 0 < len(cards2) and cards2[0] == i:
            cards2.pop(0)
        else:
            answer = 'No'
            break
    return answer
