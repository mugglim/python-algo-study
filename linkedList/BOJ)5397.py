import sys
input = lambda:sys.stdin.readline().rstrip()

class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.curr = self.head

    def move(self,opt):
        if self.size != 0:
            if opt == "<":
                if self.curr.prev != None: self.curr = self.curr.prev
            else:
                if self.curr.next != self.tail: self.curr = self.curr.next

    def insert(self,val):
        prev,next = self.curr, self.curr.next

        node = Node(val)

        node.prev = prev
        node.next = next
        next.prev = node
        prev.next = node
        self.curr = node

        self.size += 1

    def delete(self):
        if self.size != 0 and self.curr != self.head:
            prev,next = self.curr.prev, self.curr.next

            next.prev = prev
            prev.next = next

            self.curr = prev

            self.size -= 1

    def print(self):
        curr = self.head
        s = []

        while curr != None:
            s.append(curr.val if curr.val != None else "")
            curr = curr.next

        return "".join(s)


if __name__ == "__main__":
    answer = []
    t = int(input())
    for _ in range(t):
        s = input()
        dl = DL()
        for x in s:
            if x == ">" or x == "<": dl.move(x)
            elif x == "-": dl.delete()
            else: dl.insert(x)
        answer.append(dl.print())

    for s in answer: print(s)

