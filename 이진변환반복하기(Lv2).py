def solution(s):
    ans = [0, 0]

    while s != '1':
        ans[0] += 1
        
        cnt = s.count('1')
        ans[1] += len(s) - cnt
        s = bin(cnt)[2:]
    
    return ans

def solution1(s):
    ans = [0, 0]

    while s != '1':
        ans[1] += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]

        ans[0] += 1

    return ans

s = "110010101001"
print(solution(s))