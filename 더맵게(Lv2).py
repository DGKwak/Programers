import heapq

def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp)
        ans += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return ans