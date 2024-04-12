# 시간초과 O(n^2)
# def solution(n, left, right):
#     ans = [0 for _ in range(left, right+1)]
#     buff = [[0 for _ in range(n)] for _ in range(n)]
#     buff[0][0] = 1
    
#     for i in range(n):
#         for j in range(i):
#             buff[i][j], buff[j][i], buff[i][i] = i+1, i+1, i+1
    
#     for x, y in enumerate(range(left, right+1)):
#         ans[x] = buff[y//n][y%n]
    
#     return ans

def solution(n, left, right):
    ans = []

    for i in range(left, right+1):
        if i // n == 0:
            ans.append(i % n + 1)
        else:
            if i % n <= i // n:
                ans.append((i // n) + 1)
            else:
                ans.append(i % n + 1)
    
    return ans

# 다른 사람 풀이
def solution1(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n, i%n)+1)
    return answer

n, left, right = 4, 7, 14
print(solution(n, left, right))