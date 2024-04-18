# def solution(a, b):
#     answer = a+b
#     c=0
#     if a > b:
#         for i in range(a-b-1):
#             answer += b+i+1
#             return answer
#     elif a < b:
#         for i in range(b-a-1):
#             answer += a+i+1
#             return answer
#     else:
#         return a  
#     return answer

def solution(a, b):
    answer = 0
    if a > b:
        for i in range(b,a+1,1):
            answer += i
    elif a < b:
        for i in range(a,b+1,1):
            answer += i
    else:
        return a  
    return answer