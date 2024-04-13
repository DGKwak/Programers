def solution(n, words):
    answer = []
    cnt = {x+1:0 for x in range(n)}
    buff = []
    count = 1

    for i, j in enumerate(words):
        cnt[count] += 1

        if i == 0:
            count += 1
            buff.append(j)
            continue

        if j[0] != buff[-1][-1] or j in buff:
            answer = [count, cnt[count]]
            break

        buff.append(j)
        count += 1

        if count > n:
            count = 1
    else:
        return [0, 0]

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))