def solution(k, tan):
    ans = 0
    cnt = k
    cnt_dict = {}
    
    for i in tan:
        try:
            cnt_dict[i] += 1
        except:
            cnt_dict[i] = 1
        
    cnt_dict = sorted(cnt_dict.items(), key=lambda x:x[1], reverse=True)
    
    for j in cnt_dict:
        k -= j[1]
        ans += 1
        
        if k <= 0:
            break
    
    return ans