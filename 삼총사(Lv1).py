def solution(num):
    ans = 0
    
    for i in range(len(num)-2):
        for j in range(i+1,len(num)-1):
            for k in range(j+1,len(num)):
                if num[i] + num[j] + num[k] == 0:
                    ans += 1
    
    return ans


num = [-2, 3, 0, 2, -5]
print(solution(num))