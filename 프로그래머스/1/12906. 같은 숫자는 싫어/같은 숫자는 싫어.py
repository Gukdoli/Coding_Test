# def solution(arr):
#     answer = []
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i])
#     answer.append(arr[-1])
#     return answer

def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer