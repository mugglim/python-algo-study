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
            if opt == "L":
                if self.curr.prev != None: self.curr = self.curr.prev
            else:
                if self.curr.next != self.tail: self.curr = self.curr.next

    def insert(self,val):
        prev,next = self.curr, self.curr.next

        # init node
        node = Node(val)

        # insert node
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
    s = input()
    m = int(input())
    dl = DL()

    for x in s:
        dl.insert(x)

    for _ in range(m):
        x = input().split()
        if x[0] == "L" or x[0] == "D": dl.move(x[0])
        elif x[0] == "B": dl.delete()
        else: dl.insert(x[1])

    print(dl.print())


