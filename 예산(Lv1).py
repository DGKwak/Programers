def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    
    ans, tmp = 0, 0
    d.sort()
    
    for i in d:
        tmp += i
        
        if tmp > budget:
            break
        
        ans += 1
    
    return ans