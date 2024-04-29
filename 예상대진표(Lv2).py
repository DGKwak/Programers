# 서로 2의 몫이 같을 때까지 연산
def solution(n,a,b):
    ans = 0
    while a != b:
        ans += 1
        a = (a+1)//2
        b = (b+1)//2
    
    return ans

# bit연산으로 계산
def solution1(n,a,b):
    return ((a-1)^(b-1)).bitlength()

print(solution(8, 4, 7))