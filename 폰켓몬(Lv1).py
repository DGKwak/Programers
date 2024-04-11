# 내 풀이
def solution(nums):
    ans = 0
    nums.sort()
    pick = len(nums) / 2
    tmp = {}
    
    for i in nums:
        try:
            tmp[i] += 1
        except:
            tmp[i] = 1
            
    if len(tmp) < pick:
        ans = len(tmp)
    else:
        ans = pick
    
    return int(ans)

# 다른 사람 풀이
def solution1(ls):
    return min(len(ls)/2, len(set(ls)))

nums = [3,1,2,3]
print(solution(nums))