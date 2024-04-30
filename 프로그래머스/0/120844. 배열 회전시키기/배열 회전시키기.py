def solution(numbers, direction):
    if direction == "right":
        a = numbers.pop()
        a
        numbers.insert(0,a)
        
    if direction == "left":
        numbers.append(numbers.pop(0))
    return numbers