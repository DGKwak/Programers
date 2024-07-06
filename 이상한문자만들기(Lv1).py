def solution(s):
    s = s.split(' ')
    tmp = ''
    
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                tmp += i[j].upper()
            else:
                tmp += i[j].lower()
        
        tmp += ' '
    
    return tmp[0:-1]