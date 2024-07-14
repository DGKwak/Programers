def solution(num):
    ans = 0
    
    while num != 1:
        if ans == 500:
            return -1
        
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num = num / 2
            
        ans += 1
    
    return ans