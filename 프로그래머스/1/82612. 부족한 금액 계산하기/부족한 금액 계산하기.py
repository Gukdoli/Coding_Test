def solution(price, money, count):
    answer = 0
    a = 0
    if count == 1:
        if money >= price:
            return 0
        else:
            answer = money - price
    else:
        for i in range(1,count+1):
            a += price*i
        if money >= a:
                return 0
        else:
            answer = money - a
                
            
    return abs(answer)