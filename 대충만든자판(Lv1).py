# 혼자 해본 것
# def solution(keymap, targets):
#     rslt = [0 for x in range(len(targets))]
#     tmp = [y for x in keymap for y in x]
#     tmp = sorted(set(tmp))
#     k = [list(x) for x in keymap]
    
#     for x, i in enumerate(targets):
#         ans = 0
#         for j in i:
#             temp = 0
#             if j in tmp:
#                 for y in k:
#                     if j in y:
#                         if temp == 0:
#                             temp = y.index(j) + 1
#                         elif temp > y.index(j) + 1:
#                             temp = y.index(j) + 1
#             else:
#                 ans = -1
#                 break

#             ans += temp

#         rslt[x] += ans
#     return rslt

# 확인한 풀이
def solution(keymap, targets):
    rslt = []
    hs = {}

    for i in keymap:
        for j, ch in enumerate(i):
            hs[ch] = min(j+1, hs[ch]) if ch in hs else j+1

    for t in targets:
        ret = 0

        for ch in t:
            if ch not in hs:
                ret = -1
                break

            ret += hs[ch]
        
        rslt.append(ret)

    return rslt

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

print(solution(keymap, targets))