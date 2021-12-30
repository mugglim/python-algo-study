import sys
input = lambda: sys.stdin.readline().rstrip()

dirDict = {
    0: [0,1],
    1: [-1,0],
    2: [0,-1],
    3: [1,0]
}

def moveLeft(dir): return (dir + 1) % 4
def moveRight(dir): return dir - 1 if dir != 0 else 3
def moveForward(point, dir): return [point[0] + dirDict[dir][0], point[1] + dirDict[dir][1]]
def moveBack(point, dir): return [point[0] + dirDict[(dir + 2) % 4][0], point[1] + dirDict[(dir + 2) % 4][1]]


def moveTurtle(cmds):
    start = [0,0]
    dir = 0

    minX = minY = maxX = maxY = 0

    for cmd in cmds:
        if cmd == "L": dir = moveLeft(dir)
        elif cmd == "R": dir = moveRight(dir)
        else:
            if cmd == "F": start = moveForward(start, dir)
            if cmd == "B": start = moveBack(start, dir)
            minX = min(minX, start[0])
            minY = min(minY, start[1])
            maxX = max(maxX, start[0])
            maxY = max(maxY, start[1])

    return abs(maxY - minY) * abs(maxX - minX)


t = int(input())
ans = []

for _ in range(t):
    cmds = input()
    ans.append(moveTurtle(cmds))

for x in ans: print(x)