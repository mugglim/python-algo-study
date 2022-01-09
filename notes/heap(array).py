class Heap:
    def __init__(self):
        self.data = [0]

    def getSize(self):
        return len(self.data) - 1

    def isEmpty(self):
        return self.getSize() == 0

    def hasOnlyRoot(self):
        return self.getSize() == 1

    def hasLeftChild(self, idx):
        return idx * 2 <= self.getSize()

    def hasRightChild(self, idx):
        return idx * 2 + 1 <= self.getSize()

    def isLeafNode(self, idx):
        return not self.hasLeftChild(idx)

    def getMinChild(self, idx):
        leftChildValue = self.data[idx*2]
        rightChildValue = self.data[idx*2+1] if self.hasRightChild(idx) else None

        if not rightChildValue:
            return [leftChildValue, idx*2]
        else:
            return [leftChildValue, idx * 2] if leftChildValue < rightChildValue else [rightChildValue, idx*2+1]

    def push(self, value):
        self.data.append(value)

        childIdx = len(self.data) - 1
        parentIdx = childIdx // 2

        while childIdx != 1 and self.data[childIdx] < self.data[parentIdx]:
            self.data[childIdx], self.data[parentIdx] = self.data[parentIdx], self.data[childIdx]
            childIdx, parentIdx = parentIdx, parentIdx // 2

    def pop(self):
        if self.isEmpty(): return -1
        if self.hasOnlyRoot(): return self.data.pop()

        # swap
        rootValue = self.data[1]
        lastChildValue = self.data.pop()
        self.data[1] = lastChildValue

        # traverse
        currIdx, currValue = 1, lastChildValue

        while not self.isLeafNode(currIdx):
            minChildValue, minChildIdx = self.getMinChild(currIdx)

            if currValue < minChildValue: break

            self.data[currIdx], self.data[minChildIdx] = minChildValue, currValue
            currIdx = minChildIdx

        return rootValue
