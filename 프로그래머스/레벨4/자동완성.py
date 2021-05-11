class Trie:
    def __init__(self):
        self.head = {}

    # add
    def add(self,word):
        curr = self.head
        for ch in word:
            # 해당 문자가 처음인 경우
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
            if "*" in curr:
                curr["*"] += 1
            else:
                curr["*"] = 1

    # # search
    def search(self,word):
        curr = self.head
        cnt = 0
        for ch in word:
            if ("*" in curr and curr["*"] == 1 and len(curr) == 2):
                return cnt
            cnt += 1
            curr = curr[ch]

        return cnt

def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.add(word)

    for word in words:
        answer += trie.search(word)

    return answer

solution(["go","gone","guild"])
solution(["abc","def","ghi","jklm"]	)
solution(["word","war","warrior","world"]	)