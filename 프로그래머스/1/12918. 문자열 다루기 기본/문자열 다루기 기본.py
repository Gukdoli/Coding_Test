def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if not i.isdigit():  # 문자가 숫자가 아닌 경우
                return False
        return True
    else:
        return False