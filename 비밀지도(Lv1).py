def solution(n, arr1, arr2):
    ans = []
    
    for x, y in zip(arr1, arr2):
        tmp = bin(x|y)[2:]
        tmp = '0' * (n-len(tmp)) + tmp
        
        ans.append(''.join([' ' if z == '0' else '#' for z in tmp]))
    
    return ans