def solution(sides):
    sides = sorted(sides)
    plus = int(sides[0]+sides[1])
    if plus > max(sides):
        return 1
    else:
        return 2
        
    return 1