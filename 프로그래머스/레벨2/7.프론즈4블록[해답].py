def solution(m, n, board):
    answer = 0
    board = [list(l) for l in board]
    is_pop = False
    dx = [0, 0, 1, 1]  # 0은 자기자신!
    dy = [0, 1, 0, 1]

    # 2X2 블록 팝!
    # 어차피 i-1,j-1까지만 해도 2X2 점검이 가능하다 !

    while True:
        pops = []
        for i in range(m - 1):
            for j in range(n - 1):
                # 왼쪽에서 시작하기 때문에, 오른쪽, 아래, 오른쪽 대각선이 2X2 면성립
                if board[i][j] != 0 and board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][
                    j] == board[i + 1][j + 1]:
                    pops.append([i, j])

        # pop 해버리자!
        for l in pops:
            y, x = l
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if board[ny][nx] != 0:
                    board[ny][nx] = 0
                    answer += 1

        # pop 된 공간 이동하장!
        for x in range(n):
            for y in range(m - 2, -1, -1):
                top, bottom = y, y + 1
                while bottom < m and board[top][x] != 0 and board[bottom][x] == 0:
                    board[bottom][x] = board[top][x]
                    board[top][x] = 0
                    top += 1
                    bottom += 1

        if len(pops) == 0:  # pop이 안됬으면 종료해야지 ㅎㅎ
            break

    return answer


# print(solution(2,2, ["AA", "AB"]))
# print(solution(3,2, ["AA", "AA", "AB"]))
# print(solution(4,2, ["CC", "AA", "AA", "CC"]))
# print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
print(solution(4, 4, ["ABCD", "BACE", "BCDD", "BCDD"]))
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))