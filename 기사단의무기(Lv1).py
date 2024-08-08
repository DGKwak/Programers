import math

def measure(num):
    tmp = 2
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            if num // i == i:
                tmp += 1
            else:
                tmp +=2
            
    return tmp

def solution(number, limit, power):
    ans = [0, 1]
    
    for i in range(2, number+1):
        tmp = measure(i)
        if tmp > limit:
            ans.append(power)
        else:
            ans.append(tmp)
    
    return sum(ans)