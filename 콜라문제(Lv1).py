def solution(a, b, n):
    bonus = [(n//a)*b]
    tmp = bonus[-1] + (n % a)
    
    while tmp >= a:
        bonus.append((tmp//a)*b)
        tmp = bonus[-1] + (tmp % a)
    
    return sum(bonus)