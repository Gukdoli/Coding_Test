def solution(myString):
    a = myString.split("x")
    answer = []
    for i in a:
        if i != "":
            answer.append(i)
            
    return sorted(answer)