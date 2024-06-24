from itertools import permutations

# Time Out
def solution(num):
    num = list(map(str, num))
    
    return str(max(list(map(int, map(''.join, permutations(num))))))

# 통과
def solution1(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(num)))