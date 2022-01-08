from typing import List

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters, self.combinationLength = characters, combinationLength
        self.combinationList = []
        self.getCobinationList(0, [])
        self.curr = 0

    def getCobinationList(self, start: int, trace: List[str]):
        if len(trace) == self.combinationLength:
            self.combinationList.append(''.join(trace))
            return trace

        for i in range(start, len(self.characters)):
            trace.append(self.characters[i])
            self.getCobinationList(i+1, trace)
            trace.pop()

    def next(self) -> str:
        self.curr += 1
        return self.combinationList[self.curr - 1]

    def hasNext(self) -> bool:
        return self.curr < len(self.combinationList)

