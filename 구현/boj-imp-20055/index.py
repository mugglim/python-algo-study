import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
durabilitys = list(map(int,input().split()))
belts = deque([[d, False] for d in durabilitys])

step = 1
cnt = 0
downIdx = n - 1

def moveBelts(): belts.rotate(1)
def isFinished(): return cnt >= k
def canMoveRobot(idx): return belts[idx][0] > 0 and not belts[idx][1]
def handleDownRobot(): belts[downIdx][1] = False


def handleMoveRobot(idx):
    global cnt
    if idx == downIdx: return handleDownRobot()
    if not canMoveRobot(idx + 1): return

    belts[idx][1], belts[idx+1][1] = False, True
    belts[idx+1][0] -= 1

    if idx + 1 == downIdx: belts[idx+1][1] = False
    if belts[idx+1][0] == 0: cnt += 1

def locateRobot(): handleMoveRobot(-1)

def moveRobots():
    for i in range(downIdx, -1, -1):
        if belts[i][1]: handleMoveRobot(i)


while True:
    # 1. step1
    moveBelts()

    # 2. step2
    moveRobots()

    # 3. step3
    locateRobot()

    # 4. step4
    if isFinished(): break

    step += 1

print(step)