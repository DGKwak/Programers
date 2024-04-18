def solution(n):
    buff = [0 for _ in range(n+1)]
    buff[1] = 1

    for i in range(2, n+1):
        buff[i] = buff[i-1] + buff[i-2]
    
    return buff[n] % 1234567

print(solution(5))