# 1. XOR
X, Y, Z = 10, 11, 12

print(X ^ 0) # 1) X ^ 0 = X
print((X^Y)^Z == X^(Y^Z)) # 2) 결합법칙 => # (X^Y)^Z = X^(Y^Z)
print(X^Y == Y^X)  # 3) 교환법칙 => X^Y = Y^X

# 2. 👍 Bit Mask

class BitMask:
    def __init__(self, cnt):
        self.bits = 0
        self.mask = 2 ** cnt - 1

    def not_oper(self, bin):
        return bin ^ self.mask

    def add(self, idx):
        self.bits = self.bits | (1 << idx)

    def remove(self, idx):
        self.bits = self.bits & self.not_oper(1 << idx)

    def exist(self, idx):
        return self.bits & (1 << idx) != 0

    def toggle(self, idx):
        self.bits = self.bits ^ (1 << idx)

