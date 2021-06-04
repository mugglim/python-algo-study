class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.tail
        self.maxSize = 5
        self.size = 0

    def append(self,val):
        prev, curr = self.tail.prev, self.tail
        newNode = Node(val)

        newNode.next = curr
        newNode.prev = prev

        curr.prev = newNode
        prev.next = newNode

    def pop(self):
        curr = self.tail.prev
        pop_val = curr.val

        curr.next.prev = curr.prev
        curr.prev.next = curr.next

        del curr # free()
        return pop_val

class Stack:
    def __init__(self):
        self.dl = DoublyLinkedList()

    def push(self,val):
        if not self.isFull():
            self.dl.append(val)
            self.dl.size += 1
        else:
            print("[Error!] stack is already Full!")

    def pop(self):
        if not self.isEmpty():
            self.dl.size -= 1
            return self.dl.pop()
        else:
            print("[Error!] stack is empty!")

    def peek(self):
        if not self.isEmpty():
            return self.dl.tail.prev.val
        else:
            print("[Error!] stack is empty!")

    def isFull(self):
        return self.dl.size == self.dl.maxSize

    def isEmpty(self):
        return self.dl.size == 0
