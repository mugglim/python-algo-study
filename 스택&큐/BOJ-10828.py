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
        return pop_val # return


class Stack:
    def __init__(self):
        self.dl = DoublyLinkedList()


    def size(self):
        return self.dl.size

    def push(self,val):
        self.dl.append(val)
        self.dl.size += 1

    def pop(self):
        if not self.isEmpty():
            self.dl.size -= 1
            return self.dl.pop()
        else:
            return -1

    def peek(self):
        if not self.isEmpty():
            return self.dl.tail.prev.val
        else:
            return -1

    def isEmpty(self):
        return self.dl.size == 0

if __name__ == "__main__":
    n = int(input())
    stack = Stack()
    answer = []

    for _ in range(n):
        opt = input().split()
        if opt[0] == "push":
            stack.push(int(opt[1]))
        elif opt[0] == "pop":
            answer.append(stack.pop())
        elif opt[0] == "size":
            answer.append(stack.size())
        elif opt[0] == "empty":
            answer.append(1 if stack.isEmpty() == True else 0)
        elif opt[0] == "top":
            answer.append(stack.peek())

    for e in answer:
        print(e)

