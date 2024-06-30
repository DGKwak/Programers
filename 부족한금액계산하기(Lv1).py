def solution(price, money, count):
    tmp = 0
    
    for i in range(1, count+1):
        tmp += price*i
        
    tmp -= money
    
    if tmp <= 0:
        return 0
        
    return tmp