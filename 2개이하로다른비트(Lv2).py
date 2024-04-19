def solution(num):
    ans = []
    
    for i in num:
        if i % 2 == 0:
            ans.append(i+1)
        else:
            tmp = '0' + bin(i)[2:]
            tmp_n = tmp.rfind('0')
            tmp = list(tmp)
            
            tmp[tmp_n], tmp[tmp_n+1] = '1', '0'
            ans.append(int('0b'+''.join(tmp), 2))
        
    return ans

print(solution([2, 7]))