def solution(arr1, arr2):
    answer = []
    
    for arr in arr1:
        tmpl = []
        for i in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr2)):
                tmp += arr[j]*arr2[j][i]
            
            tmpl.append(tmp)
        answer.append(tmpl)
    
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))