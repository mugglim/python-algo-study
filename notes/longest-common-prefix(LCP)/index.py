class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word:str) -> None:
        curr = self.head
        for ch in word:
            if ch not in curr: curr[ch] = {}
            curr = curr[ch]
        curr['isLeaf'] = True

    def findLCP(self) -> str:
        curr = self.head
        ans = ""

        while True:
            ch = next(iter(curr))
            if ch == "isLeaf" or len(curr) > 1: break
            curr = curr[ch]
            ans += ch

        return ans


