def convert(num, form):
    form_l = '0123456789ABCDEF'
    q, r = divmod(num, form)
    
    if q == 0:
        return form_l[r]
    else:
        return convert(q, form) + form_l[r]

def solution(n, t, m, p):
    ans = ''
    buff = ''
    
    for i in range(t*m+1):
        buff += convert(i, n)
    
    while len(ans) < t:
        ans += buff[p-1]
        p += m
    
    return ans

print(solution(2, 4, 2, 1))