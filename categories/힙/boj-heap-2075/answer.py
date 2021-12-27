import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

class MinHeap:
    def __init__(self, size):
        self.minHeap = []
        self.size = size;

    def isFull(self):
        return len(self.minHeap) == self.size

    def push(self, data):
        heapq.heappush(self.minHeap, data)

    def pop(self):
        heapq.heappop(self.minHeap)

    def add(self, data):
        if not self.isFull():
            self.push(data)
        else:
            if self.minHeap[0] < data:
                self.pop()
                self.push(data)

    def getMinimum(self):
        return self.minHeap[0]

n = int(input())
minHeap = MinHeap(n)

for i in range(n):
    row = list(map(int,input().split()))
    for x in row: minHeap.add(x)

print(minHeap.getMinimum())