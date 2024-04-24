def solution(cipher, code):
    return ''.join([str(j) for i,j in enumerate(cipher, start = 1) if i % code == 0])
