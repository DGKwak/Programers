def solution(A,B):
    ans = 0
    A.sort()
    B.sort(reverse=True)
    
    for i, j in zip(A, B):
        ans += i * j

    return ans

A = [1, 4, 2]
B = [5, 4, 4]

print(solution(A,B))