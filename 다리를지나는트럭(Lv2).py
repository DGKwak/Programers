from collections import deque

# deque 사용
def solution(bl, wei, tr_wei):
    ans = 0
    bridge = deque([0] * bl)
    tr_wei = deque(tr_wei)

    curr = 0
    
    while len(tr_wei) > 0:
        ans += 1
        curr = curr - bridge.popleft()
        
        if curr + tr_wei[0] <= wei:
            curr += tr_wei[0]
            bridge.append(tr_wei.popleft())
        else:
            bridge.append(0)
            
    return ans + bl

# list 사용
def solution1(bl, wei, tr_wei):
    ans = 0
    bridge = [0] * bl
    
    curr = 0
    
    while len(tr_wei) > 0:
        ans += 1
        curr = curr - bridge.pop(0)
        
        if curr + tr_wei[0] <= wei:
            curr += tr_wei[0]
            bridge.append(tr_wei.pop(0))
        else:
            bridge.append(0)
            
    return ans + bl

bl = 2
wei = 10
tr_wei = [7,4,5,6]

print(solution(bl, wei, tr_wei))