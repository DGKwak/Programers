from itertools import permutations
import math

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        
    return True

def solution(nums):
    ans = []
    nums = list(nums)
    per = []
    
    for i in range(1, len(nums)+1):
        per += list(permutations(nums, i))
        
    nums = set([int(''.join(x)) for x in per])
    
    for j in nums:
        ans.append(is_prime(j))
    
    return ans.count(True)

print(solution('011'))