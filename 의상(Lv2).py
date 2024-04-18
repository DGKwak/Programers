def solution(clothes):
    ans = 1
    closet = {}
    
    for i in clothes:
        if i[1] in closet.keys():
            closet[i[1]] += 1
        else:
            closet[i[1]] = 1
    
    for j in closet.values():
        ans *= j+1
    
    return ans-1 

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))