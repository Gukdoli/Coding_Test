def solution(cards1, cards2, goal):
    
    answer = 'Yes'
    for word in goal:
        if 0 < len(cards1) and cards1[0] == word:
            cards1.pop(0)

        elif 0 < len(cards2) and cards2[0] == word:
            cards2.pop(0)
        else:
            answer = 'No'
            break
        if len(cards1) == 0 and len(cards2) == 0:
            answer = 'Yes'
    return answer
