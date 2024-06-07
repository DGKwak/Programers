def solution(n):
    cnt = bin(n).count('1')
    
    while 1:
        n += 1
        
        if bin(n).count('1') == cnt:
            break
    
    return n

n = 78
print(solution(78))