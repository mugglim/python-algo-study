class Trie:
    def __init__(self):
        self.data = {}
        self.head = self.data

    def insert(self, word: str) -> None:
        self.curr = self.head

        for ch in word:
            if ch not in self.curr: self.curr[ch] = {}
            self.curr = self.curr[ch]

        self.curr['*'] = True

    def search(self, word: str) -> bool:
        self.curr = self.head

        for ch in word:
            if ch not in self.curr: return False
            self.curr = self.curr[ch]

        return True if "*" in self.curr else False

    def startsWith(self, prefix: str) -> bool:
        self.curr = self.head

        for ch in prefix:
            if ch not in self.curr: return False
            self.curr = self.curr[ch]

        return len(self.curr) > 0

