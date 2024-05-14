def solution(dirs):
    buff = set()
    move = {'U':[1,0], 'D':[-1,0], 'R':[0,1], 'L':[0,-1]}
    x, y = 0, 0

    for i in range(len(dirs)):
        tmp = move[dirs[i]]
        tmp_x = x + tmp[0]
        tmp_y = y + tmp[1]
        
        if -5 <= tmp_x <= 5 and -5 <= tmp_y <= 5:
            buff.add(((x,y), (tmp_x,tmp_y)))
            buff.add(((tmp_x,tmp_y), (x,y)))
        
            x = tmp_x
            y = tmp_y
        
    return len(buff)//2

dirs = "LULLLLLLU"
print(solution(dirs))