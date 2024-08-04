def solution(arr1, arr2):
    ans = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    
    for a in range(len(arr1)):
        for b in range(len(arr1[0])):
            ans[a][b] = arr1[a][b] + arr2[a][b]
    
    return ans

def solution1(arr1, arr2):    
    return [[c+d for c,d in zip(a, b)] for a,b in zip(arr1, arr2)]

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution1(arr1, arr2))