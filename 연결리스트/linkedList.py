class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class DoublelyLikedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def is_empty(self):
        return True if self.size == 0 else False

    def appendleft(self,val):
        if self.is_empty() == True:
            self.head.next = Node(val)
        else:
            prev,next = self.head, self.head.next
            newNode = Node(val)
            newNode.next= next
            prev.next = newNode
        self.size += 1

    def append(self, val):
        if self.is_empty() == True:
            self.head.next = Node(val)
        else:
            prev, next = self.head, self.head.next
            newNode = Node(val)
            newNode.next = next
            prev.next = newNode
        self.size += 1

    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.val if curr.val != None else "" ,end=" ")
            curr = curr.next
        print()


if __name__ == "__main__":
    linked_list = DoublelyLikedList()



