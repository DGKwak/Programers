def solution(a, b):
    ans = 0
    
    for x, y in zip(a, b):
        ans += x * y
    
    return ans