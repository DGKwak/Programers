# 내 풀이
def solution(pri, loc):
    ans = []
    qu = [x for x in range(len(pri))]
    
    while qu:
        tmp = qu.pop(0)
        
        if any(pri[tmp] < pri[x] for x in qu):
            qu.append(tmp)
        else:
            ans.append(tmp)
            pri[tmp] = 0
    
    return ans.index(loc)+1

# 다른 사람 풀이
def solution1(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

pri = [2, 1, 3, 2]
loc = 2

print(solution(pri, loc))