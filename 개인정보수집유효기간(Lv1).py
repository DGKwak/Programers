def solution(today, terms, privacies):
    rslt = []
    to = int(''.join(today.split('.')))
    ter = {i.split()[0]:int(i.split()[1]) for i in terms}
    pri = [i.split() for i in privacies]
    
    for i,j in enumerate(pri):
        tmp = list(map(int, j[0].split('.')))
        tmp[0] += (ter[j[1]] // 12)
        tmp[1] += (ter[j[1]] % 12)

        if tmp[1] > 12:
            tmp[0] += 1
            tmp[1] -= 12

        if (tmp[0]*10000 + (tmp[1] * 100) + tmp[2]) <= to:
            rslt.append(i+1)
    
    return rslt

to = "2020.01.01"
te = ["Z 3", "D 5"]
pr = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(to, te, pr))