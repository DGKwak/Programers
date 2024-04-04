# 내가 한 거
def solution(band, hp, att):
    last = att[-1][0]
    suc = 0
    max_hp = hp
    att_ord = 0

    for i in range(1,last+1):
        if i == att[att_ord][0]:
            hp -= att[att_ord][1]
            att_ord += 1
            suc = 0

        else:
            hp += band[1]
            
            if hp > max_hp:
                hp = max_hp
            
            suc += 1
                
            if suc == band[0]:
                hp += band[2]
                suc = 0
                
            if hp > max_hp:
                hp = max_hp

        if hp <= 0:
            hp = -1
            break
    
    return hp

# 다른 사람이 푼 거
def solution_01(bandage, health, attacks):
    hp = health
    start = 1
    for i, j in attacks:
        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
        start = i + 1
        if hp >= health:
            hp = health
        hp -= j
        if hp <= 0:
            return -1
    return hp

band = [5, 1, 5]
hp = 30
att = [[2, 10], [9, 15], [10, 5], [11, 5]]

print(solution(band, hp, att))