def solution(n):
    ans = [[0 for i in range(x+1)] for x in range(n)]
    
    x, y = -1, 0
    tmp = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            ans[x][y] = tmp
            tmp += 1
    
    return sum(ans, [])