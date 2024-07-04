def solution(x):
    x_list = list(map(int, list(str(x))))
    tmp = sum(x_list)
    
    if x % tmp == 0:
        return True
    else:
        return False