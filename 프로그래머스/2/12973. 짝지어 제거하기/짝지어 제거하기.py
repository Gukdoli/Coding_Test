def solution(s):
    stack = []
    for i in s:
        if len(stack) != 0 and stack[-1] == i:  # 스택의 마지막 요소가 현재 문자와 같으면
            stack.pop()  # 스택에서 제거
        else:
            stack.append(i)  # 스택에 추가
    if len(stack) == 0:  # 스택이 비어있으면
        return 1
    return 0
