def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1
    
    return ans

def solution1(n):
    return bin(n).count('1')

print(solution1(5))