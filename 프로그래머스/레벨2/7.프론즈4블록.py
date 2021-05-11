dx = [0,1,1,0]
dy = [0,0,1,1]

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    def check(y,x):
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or ny >=m or nx < 0 or nx >=n:
                return False
            if board[y][x] != board[ny][nx]:
                return False
        return True
    def count_pop(pop_list):
        cnt = 0
        for pop in pop_list:
            y,x = pop
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if board[ny][nx] != "0":
                    cnt += 1
                    board[ny][nx] = "0"
        return cnt

    def move_board():
        for j in range(n):
            for i in range(m-2,-1,-1):
                prev, next = i, i + 1
                if board[i][j] != "0":
                    while next < m  and board[next][j] == "0":
                        prev = next
                        next += 1
                    if prev != i:
                        board[prev][j] = board[i][j]
                        board[i][j] = "0"

    while True:
        pop_list = []
        for i in range(m):
            for j in range(n):
                if board[i][j] != "0" and check(i,j) == True:
                    pop_list.append([i,j])
        if len(pop_list) == 0:
            break
        else:
            answer += count_pop(pop_list)
            move_board()


    return answer


solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])