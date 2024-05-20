def solution(picks, minerals):
    ans = 0

    min_dict = {'diamond':1, 'iron':2, 'stone':3}
    minerals = [min_dict[x] for x in minerals]
    cnt = [minerals[x:x+5] for x in range(0, len(minerals), 5)]

    cost = []
    for i in cnt:
        cst = [0, 0, 0]
        for j in i:
            if j == 1:
                cst[0] += 25
                cst[1] += 5
                cst[2] += 1
            elif j == 2:
                cst[0] += 5
                cst[1] += 1
                cst[2] += 1
            else:
                cst[0] += 1
                cst[1] += 1
                cst[2] += 1

        cost.append(cst)

    else:
        while len(cost) > sum(picks):
            cost.pop()

    cost_sort = sorted(cost, key=lambda x: x[0], reverse=True)

    for k in cost_sort:
        if picks[0] > 0:
            ans += k[2]
            picks[0] -= 1
        elif picks[1] > 0:
            ans += k[1]
            picks[1] -= 1
        else:
            ans += k[0]
            picks[2] -= 1
    
    return ans

picks = [1, 3, 2]
mineral = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, mineral))