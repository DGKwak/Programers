# DP 사용 - 혼자 생각해내지 못함 https://studyposting.tistory.com/93
def solution(x, y, n):
    buff = [float('inf') for _ in range(y+1)]
    buff[x] = 0
    
    for i in range(x, y+1):
        if buff[i] != float('inf'):
            if i + n <= y:
                buff[i+n] = min(buff[i+n], buff[i]+1)
            if i * 2 <= y:
                buff[i*2] = min(buff[i*2], buff[i]+1)
            if i * 3 <= y:
                buff[i*3] = min(buff[i*3], buff[i]+1)
    
    if buff[y] == float('inf'):
        return -1
    
    return buff[y]

x, y, n = 10, 40, 5
print(solution(x, y, n))