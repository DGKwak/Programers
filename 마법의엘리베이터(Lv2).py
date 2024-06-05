def solution(storey):
    ans = 0
    st = [int(x) for x in str(storey)[-1::-1]] + [0]

    for i in range(len(st)):
        if st[i] > 5 or (st[i] == 5 and st[i+1] >=5):
            ans += 10 - st[i]
            st[i+1] += 1
        else:
            ans += st[i]
    
    return ans