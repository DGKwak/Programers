from itertools import combinations

def solution(numbers):
    return sorted(list(set(map(sum, combinations(numbers,2)))))

numbers = [5,0,2,7]
print(solution(numbers))