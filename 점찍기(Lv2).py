import math

def solution(k, d):
    rslt = 0
    
    for i in range(d//k+1):
        tmp = int(math.sqrt(d**2 - (i*k)**2))
        rslt += tmp//k + 1
    
    return rslt

print(solution(1, 5))