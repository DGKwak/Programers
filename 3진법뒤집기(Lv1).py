def solution(n):
    ans = ''
    
    while n:
        n, x = divmod(n, 3)
        ans = str(x) + ans
        
    return int(ans[::-1], 3)