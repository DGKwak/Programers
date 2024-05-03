def solution(b, y):
    ans = [0, 0]
    
    for i in range(1, y+1):
        if y % i == 0:
            w, h = i, y//i
            
            if (2*w + 2*h + 4) == b:
                ans[0] += w+2
                ans[1] += h+2
                ans.sort(reverse=True)
                
                return ans
            
b , y = 24, 24

print(solution(b, y))