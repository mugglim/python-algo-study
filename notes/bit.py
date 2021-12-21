class BitMask:
    def __init__(self, size):
        self.bits = 0
        self.size = size

    def empty(self): self.bits = 0
    def all(self): self.bits = (1 << self.size) - 1
    def add(self, idx): self.bits |= (1 << idx)
    def remove(self, idx): self.bits &= ~(1 << idx)
    def isExist(self, idx): return self.bits & (1 << idx)
    def toggle(self, idx): self.bits ^= (1 << idx)

    def searchSmallest(self): return self.bits & -self.bits
    def removeSmallest(self): self.bits &= (self.bits - 1)


def union(s1,s2): return s1 | s2
def intersection(s1,s2): return s1 & s2
def diff(s1,s2): return s1 & ~s2

