def solution(arr):
    rslt = [arr[0]]
    
    for i in arr:
        if i != rslt[-1]:
            rslt.append(i)
    
    return rslt

a = [1,1,3,3,0,1,1]
print(solution(a))