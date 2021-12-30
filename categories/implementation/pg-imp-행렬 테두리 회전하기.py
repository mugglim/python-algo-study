def solution(rows, columns, queries):
    answer = []

    #  i 행 j 열에 있는 숫자 -> ((i-1) x columns + j)
    board = [[i*columns + j for j in range(1,columns+1)] for i in range(rows)]


    for query in queries:
        y1,x1,y2,x2 = query
        y1,x1,y2,x2 = y1-1, x1-1, y2-1, x2-1

        top = [board[y1+1][x1]] + board[y1][x1:x2]
        bot = board[y2][x1+1:x2+1] + [board[y2-1][x2]]
        left = [board[i][x1] for i in range(y1+2,y2+1)]
        right = [board[i][x2] for i in range(y1,y2-1)]

        if top:
            for j in range(x1,x2+1):
                board[y1][j] = top[j-x1]
        if bot:
            for j in range(x1,x2+1):
                board[y2][j] = bot[j-x1]
        if left:
            for i in range(y1+1,y2):
                board[i][x1] = left[i-y1-1]
        if bot:
            for i in range(y1+1,y2):
                board[i][x2] = right[i-y1-1]


        answer.append(min(top+bot+left+right))


    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100,97,[[1,1,100,97]]))