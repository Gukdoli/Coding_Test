def solution(myString, pat):
    if pat in myString.replace("A", "X").replace("B", "A").replace("X", "B"):
        return 1
    else:
        return 0
    return 