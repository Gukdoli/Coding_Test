def solution(my_string):
    numbers = [int(x) for x in my_string if x.isdigit()]
    
    return sum(numbers)