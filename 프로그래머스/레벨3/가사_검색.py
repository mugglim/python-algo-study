class Trie1:
    def __init__(self):
        self.head = {}

    def add(self,word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        # Finish
        curr["*"] = True


def solution(words, queries):
    answer = ''
    trie1 = Trie1()
    for word in words:
        trie1.add(word)

    for query in queries:
        if query[0] != "?":
            print(query, query[::-1])
            idx = query[::-1].index("?")
            idx = len(query) - (idx+2)
            print(idx)

    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])