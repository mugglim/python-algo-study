from sys import stdin
input = stdin.readline

class BitMask:
    def __init__(self, size):
        self.bit = 0
        self.size = size

    def add(self, idx): self.bit |= (1 << idx)
    def remove(self, idx): self.bit &= ~(1 << idx)
    def toggle(self, idx): self.bit ^= (1 << idx)
    def all(self): self.bit = (1 << self.size) - 1
    def empty(self): self.bit = 0

    def check(self, idx): return self.bit & (1 << idx) != 0


bitMask = BitMask(20)
m = int(input())

for _ in range(m):
    cmd, *v = input().split()
    v = int(v[0]) - 1 if v else v

    if cmd == "add": bitMask.add(v)
    if cmd == "remove": bitMask.remove(v)
    if cmd == "check": print(1 if bitMask.check(v) else 0)
    if cmd == "toggle": bitMask.toggle(v)
    if cmd == "all": bitMask.all()
    if cmd == "empty": bitMask.empty()

