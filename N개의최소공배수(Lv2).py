def gcd(a, b):
    a, b = min(a,b), max(a, b)
    
    while a != 0:
        r = b % a
        a, b = r, a
    
    return b

def solution(arr):
    ans = 0
    
    for i in range(len(arr)-1):
        if i == 0:
            tmp = [arr[i], arr[i+1]]
        else:
            tmp = [ans, arr[i+1]]

        ans = (tmp[0] * tmp[1]) / gcd(tmp[0], tmp[1])
    
    return ans

arr = [2,6,8,14]
print(solution(arr))