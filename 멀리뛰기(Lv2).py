def solution(n):
    if n < 3:
        return n
    
    tmp = [0, 1, 2] + ([0] * (n-2))
    
    for i in range(3, n+1):
        tmp[i] = tmp[i-1] + tmp[i-2]
    
    return tmp[n] % 1234567