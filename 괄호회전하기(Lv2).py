def is_corr(s):
    bra_dic = {')':'(', ']':'[', '}':'{'}
    tmp = []
    
    for b in s:
        if b in bra_dic.values():
            tmp.append(b)
        elif tmp and b in bra_dic.keys():
            bra = tmp.pop()
            
            if bra != bra_dic[b]:
                return False
        else:
            return False
    else:
        if tmp:
            return False
        else:
            return True

def solution(s):
    ans = 0
    
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        
        if is_corr(tmp):
            ans += 1
    
    return ans