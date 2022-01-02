import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

n = int(input())
m = int(input())
recommends = list(map(int,input().split()))

heap = []

def getStudentIndex(studentNum):
    if not heap: return -1

    for i in range(len(heap)):
        if heap[i][2] == studentNum:
            return i

    return -1

def updateStudent(studentIdx):
    heap[studentIdx][0] += 1
    heapify(heap)

def isFull(): return len(heap) == n
def addStudent(time, studentNum): heappush(heap, [1, time, studentNum])

for time, studentNum in enumerate(recommends):
    if not heap:
        addStudent(time,studentNum)
    else:
        studentIdx = getStudentIndex(studentNum)
        if studentIdx != -1:
            updateStudent(studentIdx)
        else:
            if isFull(): heappop(heap)
            addStudent(time, studentNum)


ans = sorted([fig[2] for fig in heap])
print(*ans)


