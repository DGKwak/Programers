def solution(num, hand):
    rslt = ''
    pad = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1),
           6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}
    lLast, rLast = (3, 0), (3, 2)
    rhanded = (hand == 'right')

    for i in num:
        if i in [1, 4, 7]:
            lLast = pad[i]
            rslt += 'L'
        elif i in [3, 6, 9]:
            rLast = pad[i]
            rslt += 'R'
        else:
            l = abs(lLast[0]-pad[i][0]) + abs(lLast[1]-pad[i][1])
            r = abs(rLast[0]-pad[i][0]) + abs(rLast[1]-pad[i][1])

            if l > r:
                rslt += 'R'
                rLast = pad[i]
            elif l < r:
                rslt += 'L'
                lLast = pad[i]
            elif rhanded:
                rslt += 'R'
                rLast = pad[i]
            else:
                rslt += 'L'
                lLast = pad[i]
                
    return rslt

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(numbers, hand))