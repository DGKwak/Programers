from itertools import combinations

def solution(nums):
    answer = 0
    prime = [False, False]+[True]*49999
    
    for i in range(2, int(50000**0.5)+1):
        if prime:
            for j in range(i+i, 50001, i):
                prime[j] = False
                
    tmp = list(map(sum, combinations(nums, 3)))
    
    for x in tmp:
        if prime[x]:
            answer += 1

    return answer