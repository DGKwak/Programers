# stack 미사용
def solution1(prices):
    ans = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            ans[i] += 1
            
            if prices[i] > prices[j]:
                break
    
    return ans

# stack 사용
def solution(prices):
    ans = [-1] * len(prices)
    stack = []
    
    for cur in range(len(prices)):
        while stack and prices[stack[-1]] > prices[cur]:
            past = stack.pop()
            ans[past] = cur - past
            
        stack.append(cur)
        
    for i in stack:
        ans[i] = len(prices) - i - 1
    
    return ans

prices = [1, 2, 3, 2, 3]
print(solution(prices))