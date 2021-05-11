def solution(n, build_frame):
    board = [[[False,False] for _ in range(n+1)] for i in range(n+1)]

    def check_column(x,y):
        # 1. 기둥은 바닥에 있거나
        if y == 0:
            return True
        else: # 2. 보의 한쪽 끝 부분 위에 있거나 또는 다른 기둥위에 있어야함
            if (x -1 >= 0 and board[y][x-1][1] == True) or board[y][x][1] == True:
                return True
            if board[y-1][x][0] == True:
                return True
        return False

    def check_bim(x,y):
        # bim은 건물의 바닥에 설치되는 경우가 없음.
        # 1.한 쪽 끝 부분이 기둥위에 있거나
        if board[y-1][x][0] == True:
            return True
        if x +1 <= n and board[y-1][x+1][0] == True:
            return True
        # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
        if (0<= x-1 and x+1 <=n) and (board[y][x-1][1] == True and board[y][x+1][1] == True):
            return True

        return False

    def check_all():
        for y in range(n+1):
            for x in range(n+1):
                for i,v in enumerate(board[y][x]):
                    if (i == 0 and v == True) and check_column(x,y) == False:
                        return False
                    elif (i == 1 and v == True) and check_bim(x,y) == False:
                        return False
        return True

    def get_val():
        answer = []
        for y in range(n+1):
            for x in range(n+1):
                for idx,v in enumerate(board[y][x]):
                    if v != False:
                        answer.append([x,y,idx])
        return sorted(answer,key=lambda x:(x[0],x[1],x[2]))

    for info in build_frame:
        # a:0(기둥),1(보)
        # b:0(해체),1:(설치)
        x,y,a,b = info
        # 설치하는 경우에는 전수검사를 하지 않아도 됨.
        if b == 1:
            if a == 0 and check_column(x, y) == True:
                board[y][x][0] = True
            elif a == 1 and check_bim(x, y) == True:
                board[y][x][1] = True
        elif b == 0: # 해체하는 경우
            board[y][x][a] = False
            if check_all() == False:
                board[y][x][a] = True
    return get_val()

# print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
