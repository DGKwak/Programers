import math

def solution(progress, speeds):
    progress = [math.ceil((100-x)/y) for x, y in zip(progress, speeds)]
    ans = []
    buff = []
    
    for i in progress:
        if buff and max(buff) < i:
            ans.append(len(buff))
            buff = [i]
        else:
            buff.append(i)
    else:
        ans.append(len(buff))
    
    return ans

progress = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progress, speeds))