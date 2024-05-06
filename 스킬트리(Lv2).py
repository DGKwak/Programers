def solution(skill, skill_trees):
    ans = 0
    
    for i in skill_trees:
        tmp = list(skill)
        jdg = True
        
        for j in i:
            if j in tmp:
                if j == tmp[0]:
                    tmp.pop(0)
                else:
                    jdg = False
                    break
        if jdg:
            ans += 1
    
    return ans

skill = 'CBD'
skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_tree))