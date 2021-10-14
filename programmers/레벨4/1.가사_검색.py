class Trie:
    # 트라이 Node
    def __init__(self):
        self.head = {}

    # 삽입
    def add(self, word):
        cur = self.head  # 루트 노드

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur["*"] = True

    # 탐색
    def search(self, word):
        cur = self.head
        for ch in word:
            if ch == "?":
                print(cur)
            else:
                if ch not in cur:
                    return False
                cur = cur[ch]

        return True if "*" in cur else False

def solution(words, queries):
    answer = []
    trie = Trie()
    for word in words:
        trie.add(word)

    for query in queries:
        answer.append(trie.search(query))

    print(answer)
    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
["fro??", "????o", "fr???", "fro???", "pro?"])