import math

def solution(n):
    tmp = int(math.sqrt(n))
    
    if n == tmp**2:
        return (tmp + 1) ** 2
    else:
        return -1