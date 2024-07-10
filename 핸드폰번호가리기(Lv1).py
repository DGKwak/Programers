def solution(p_num):       
    return ''.join(list('*' if i < len(p_num)-4 else p_num[i] for i in range(len(p_num))))

def solution1(p_num):       
    return '*'*(len(p_num)-4) + p_num[-4:]