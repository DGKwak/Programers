def solution(k, score):
    ans = []
    tmp = []
    
    for num, i in enumerate(score):
        tmp.append(i)
        tmp.sort(reverse=True)
        
        if len(tmp) > k:
            tmp.pop()
            
        ans.append(tmp[-1])
    
    return ans