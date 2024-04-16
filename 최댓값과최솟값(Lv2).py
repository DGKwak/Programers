def solution(s):
    buff = list(map(int, s.split()))
    buff.sort()
    
    return str(buff[0]) + " " + str(buff[-1])

s = "1 2 3 4"
print(solution(s))