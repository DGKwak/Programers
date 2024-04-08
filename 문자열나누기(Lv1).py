# 내가 한 거
def solution(s):
    rslt = 0
    le = 0
    st = None

    for x, i in enumerate(s):
        if x == len(s)-1:
            rslt += 1
            break
        
        if st == None:
            st = i
            le += 1
            continue        

        if i == st:
            le += 1
        else:
            le -= 1

            if le == 0:
                rslt += 1
                st = None
    
    return rslt

# 다른 사람이 한 거
def solution1(s):
    j = 0 
    cnt = 0 
    ans =0
    for idx,i in enumerate(s): 
        cnt += 1 if s[j] == i else -1 
        if cnt == 0 : 
            ans +=1 
            j = idx+1 
    return ans + 1 if cnt else ans

s = "aaabbaccccabba"
print(solution(s))