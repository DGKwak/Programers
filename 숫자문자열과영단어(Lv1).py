s = "one4seveneight"

numdic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

tmp = ''
ans = ''

for i in s:
    if i.isalpha():
        tmp += i

        if tmp in numdic.keys():
            ans += str(numdic[tmp])
            tmp = ''

    else:
        ans += i

print(ans)