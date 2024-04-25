def solution(a, b):
    c = int(str(a)+str(b))
    if c < 2 * a * b:
        return 2 * a* b
    
    return c