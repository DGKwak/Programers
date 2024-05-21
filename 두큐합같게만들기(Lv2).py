from collections import deque

def solution(qu1, qu2):
    ans = 0
    qu1 = deque(qu1)
    qu2 = deque(qu2)
    s1, s2 = sum(qu1), sum(qu2)
    
    if s1 == s2:
        return ans
    elif (s1 + s2) % 2 == 1:
        return -1
    
    for _ in range(3*len(qu1)):
        if s1 > s2:
            s1 -= qu1[0]
            s2 += qu1[0]
            qu2.append(qu1.popleft())
            ans += 1
        elif s2 > s1:
            s1 += qu2[0]
            s2 -= qu2[0]
            qu1.append(qu2.popleft())
            ans += 1
        else:
            return ans
            
    else:
        return -1