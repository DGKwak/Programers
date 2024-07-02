def solution(s):
    answer = []
    tmp = ''
    
    for i in s:
        cnt = 1

        if i not in tmp:
            answer.append(-1)
            tmp = i + tmp
        else:
            for j in tmp:
                if j == i:
                    answer.append(cnt)
                    tmp = i + tmp
                    break
                else:
                    cnt += 1
    
    return answer