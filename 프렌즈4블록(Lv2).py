def check(m, n, board):
    buff = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0
    
    for i in range(m-1):
        for j in range(n-1):
            tmp1 = board[i][j]
            tmp2 = board[i][j+1]
            tmp3 = board[i+1][j]
            tmp4 = board[i+1][j+1]

            if tmp1 == tmp2 == tmp3 == tmp4 and tmp1 != '0':
                buff[i][j], buff[i+1][j], buff[i][j+1], buff[i+1][j+1] = 1, 1, 1, 1
    
    for i in range(m):
        for j in range(n):
            if buff[i][j] == 1:
                cnt += 1
                board[i][j] = '0'
                
    if cnt == 0:
        return cnt
    
    for i in range(m-2, -1, -1):
        for j in range(n):
            k = i
            while 0 <= k+1 < m and board[k+1][j] == '0':
                k += 1

            if k != i:
                board[k][j], board[i][j] = board[i][j], '0'

    return cnt


def solution(m, n, board):
    ans = 0
    board = list(map(list, board))

    while True:
        tmp = check(m, n, board)
        
        if tmp == 0:
            break
        
        ans += tmp

    return ans