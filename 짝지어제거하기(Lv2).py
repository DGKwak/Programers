# 시간초과
def solution1(s):
    ans = 1
    
    while 1:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s.replace(s[i]+s[i+1], '', 1)
                break
        else:
            break
    
    if s:
        ans = 0

    return ans

# 다른 풀이
def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return 0
    
    return 1

s = 'baabaa'
print(solution(s))