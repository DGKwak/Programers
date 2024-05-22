from itertools import product

def solution(word):
    vow = ['A', 'E', 'I', 'O', 'U']
    
    rslt = []
    for i in range(1, 6):
        tmp = list(product(vow, repeat=i))
        
        for j in tmp:
            rslt.append(''.join(j))
    
    rslt.sort()
        
    return rslt.index(word) + 1

def solution1(word):
    ans = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    li = [5**i for i in range(len(dic))]

    for i in range(len(word)-1,-1,-1):
        idx = dic.index(word[i])
        for j in range(5-i):
            ans += li[j]*idx
        ans+=1
        
    return ans

word = "AAAE"
print(solution(word))