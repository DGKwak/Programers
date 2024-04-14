def solution(part, comp):
    buff = {}
    hashsum = 0
    
    for i in part:
        buff[abs(hash(i))] = i
        hashsum += abs(hash(i))
        
    for j in comp:
        hashsum -= abs(hash(j))
        
    return buff[hashsum]

part = ["marina", "josipa", "nikola", "vinko", "filipa"]
comp = ["josipa", "filipa", "marina", "nikola"]

print(solution(part, comp))