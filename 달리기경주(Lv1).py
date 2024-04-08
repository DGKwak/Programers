def solution(pl, call):
    temp = {y:x for x,y in enumerate(pl)}

    for i in call:
        idx = temp[i]
        temp[i] -= 1
        temp[pl[idx-1]] += 1
        
        pl[idx-1], pl[idx] = pl[idx], pl[idx-1]
        
    return pl

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))