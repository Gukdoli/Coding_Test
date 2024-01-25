def solution(s):
    a = s.count("p")
    b = s.count("P")
    c = s.count("y")
    d = s.count("Y")
    pP=a+b
    yY=c+d
    if pP == yY:
        return True
    else:
        return False