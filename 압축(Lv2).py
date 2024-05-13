def solution(msg):
    ans = []
    ind = [chr(ord('A')+x) for x in range(26)]
    
    low, high = 0, 0
    
    while 1:
        high += 1
        
        if high == len(msg):
            ans.append(ind.index(msg[low:high])+1)
            break
        
        if msg[low:high+1] not in ind:
            ind.append(msg[low:high+1])
            ans.append(ind.index(msg[low:high])+1)
            low = high
            
    return ans

msg = 'KAKAO'
print(solution(msg))