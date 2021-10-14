from functools import reduce

n = int(input())
players = [list(map(int,input().split())) for _ in range(n)]
players.sort(key=lambda x:(x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

answer = reduce(lambda a,b: [*a,b[0]], players[:3], [])

print(*answer)