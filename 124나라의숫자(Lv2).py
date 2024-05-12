def solution(n):
    ans = ''
    while n > 0:
        q, r = divmod(n, 3)
        
        if r == 0:
            n = q-1
            ans += '4'
        else:
            n = q
            ans += str(r)
    
    return ans[::-1]

print(solution(99))