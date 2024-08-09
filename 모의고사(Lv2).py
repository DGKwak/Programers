def solution(answers):
    sp = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in range(3):
        if len(sp[i]) < len(answers):
            tmp = len(answers) - len(sp[i])
            sp[i] = sp[i]+(sp[i]*(tmp//len(sp[i])))+(sp[i][:(tmp%len(sp[i]))+1])
        else:
            sp[i] = sp[i][:len(answers)]
    
    sp_tmp = [sum([1 if x == y else 0 for x,y in zip(answers, sp[z])]) for z in range(3)]
    
    return [x+1 for x in list(filter(lambda x: sp_tmp[x] == max(sp_tmp), range(len(sp_tmp))))]