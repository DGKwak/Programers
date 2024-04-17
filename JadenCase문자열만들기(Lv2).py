def solution(s):
    s = s.split(' ')
    
    for x, i in enumerate(s):
        s[x] = i.capitalize()
    
    return ' '.join(s)

s = "3people unFollowed me"
print(solution(s))