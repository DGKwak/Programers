def solution(s):
    buff = []
    
    for i in s:
        if i == '(':
            buff.append(i)
        elif buff and i == ')':
            buff.pop()
        else:
            return False
        
    if buff:
        return False

    return True

s = "(())()"
print(solution(s))