def solution(record):
    answer = []
    buff = [x.split() for x in record]
    id_dic = {}

    for i in buff:
        if len(i) == 3:
            id_dic[i[1]] = i[2]

    for j in buff:
        if j[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(id_dic[j[1]]))
        elif j[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(id_dic[j[1]]))
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))