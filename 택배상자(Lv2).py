def solution(order):
    ans = 0
    tmp = []
    i = 1
    
    while i != len(order)+1:
        tmp.append(i)
        
        while tmp and tmp[-1] == order[ans]:
            ans += 1
            tmp.pop()
        
        i += 1
    
    return ans

def solution1(order):
    ans = 0
    tmp = []
    
    for i in range(len(order)):
        tmp.append(i+1)

        while tmp and tmp[-1] == order[ans]:
            tmp.pop()
            ans += 1
    
    return ans

order = [4, 3, 1, 2, 5]
print(solution1(order))