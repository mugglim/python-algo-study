## 링크
https://www.acmicpc.net/problem/8911

## 풀이 1

거북이는 가장 처음에는 (0,0) 지점에, 방향은 북쪽 방향을 바라보고 있다.  
방향은 북,서,남,동 방향을 각각 0,1,2,3으로 생각했다. 이후, dirDict을 선언 해 (dx,dy)를 방향 별로 설정했다.
```python
# dir : (dx,dy)
dirDict = {
    0: [0,1],    # 북
    1: [-1,0],   # 서
    2: [0,-1],   # 남
    3: [1,0]     # 동
}
```

우선, 거북이에게 명령하는 로직을 처리해보자.
- F/B: 한 눈금 앞으로/뒤로
  - F/B 명령어는 거리를 움직이는 로직이다. 
  - 기존의 위치에서 `dirDict`을 통해 (dx,dy)를 더해 주자
  - 단, B 명령어는 반대 방향으로 이동해야 하므로 180도 회전 방향을 알기 위해 `(dir + 2 ) % 4` 로 계산했다.
- L : 왼쪽으로 90도 회전
  - 기존의 방향에 1을 더하면 왼쪽으로 90도 회전 되며, 동->북을 반영하기 위해 `(dir + 1) % 4`로 방향을 계산했다.
- R : 오른쪽으로 90도 회전
  - 기존의 방향에 1을 뺴면 오른쪽으로 90도 회전 되며, 북->동을 반영하기 위해 dir이 0인 경우는 3으로 초기화 해주었다.


이제 거북이가 이동한 넓이를 구해보자.  
x,y의 최소 지점과 최대 지점을 선분으로 그어 공통 영역을 넓이로 생각하면 된다.  
(단, 거북이가 F/B 명령어를 통해서만 이동하므로, 해당 명령어가 수행될 때만 최소, 최대 지점을 갱신하자.)

### code
```python
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
```

## 결과
|   풀이    |   방식    |    시간    |
|:-------:|:-------:|:--------:|
|    1    | 구현 + 규칙 | 2628 ms  | 