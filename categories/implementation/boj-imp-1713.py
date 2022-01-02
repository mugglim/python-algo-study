import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

n = int(input())
m = int(input())
recommends = list(map(int,input().split()))

heap = []


def isExistStudent(studentNum):
    if not heap: return False

    for i in range(len(heap)):
        if heap[i][2] == studentNum:
            return True

    return False


def getStudentIndex(studentNum):
    for i in range(len(heap)):
        if heap[i][2] == studentNum:
            return i

    return -1


def updateStudent(studentIdx):
    heap[studentIdx][0] += 1
    heapify(heap)

def isFull(): return len(heap) == n

def addStudent(time, studentNum):
    if isFull(): heappop(heap)
    heappush(heap, [1, time, studentNum])

for time, studentNum in enumerate(recommends):
    if not heap or not isExistStudent(studentNum):
        addStudent(time,studentNum)
    else:
        studentIdx = getStudentIndex(studentNum)
        updateStudent(studentIdx)


ans = sorted([fig[2] for fig in heap])
print(*ans)

