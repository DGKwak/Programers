def solution(t, p):
    ans = 0
    
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            ans += 1
    
    return ans