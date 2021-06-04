class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def empty(self):
        return True if self.size == 0 else False

    # 1. Access, search
    def get(self,idx):
        if not self.empty():
            curr = self.head
            for _ in range(idx): curr = curr.next
            return curr.val

    # 2. insertion
    def insert(self,idx,val):
        if idx == 1:
            self.appendLeft(val)
        else:
            newNode = Node(val)
            prev, curr = self.head, self.head.next
            for _ in range(idx -1):
                prev = curr
                curr = curr.next

            newNode.next = curr
            prev.next = newNode

        self.size += 1

    def appendLeft(self,val):
        prev, curr = self.head, self.head.next
        newNode = Node(val)

        newNode.next = curr
        prev.next = newNode

    # 3. deletion
    def remove(self,idx):
        if not self.empty():
            prev, curr = self.head, self.head.next
            for _ in range(idx-1):
                prev = curr
                curr = curr.next

            prev.next = curr.next
            del curr

            self.size -= 1

    # traverse for print
    def traverse(self):
        if self.empty():
            print("Empty!!")
        else:
            curr = self.head
            while curr != None:
                print(curr.val if curr.val != None else "", end="")
                curr = curr.next
            print()


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert(1,1)
    linked_list.insert(2,2)
    linked_list.insert(3,3)
    linked_list.insert(4,4)
    linked_list.traverse()

    linked_list.remove(4)
    linked_list.traverse()
    linked_list.remove(3)
    linked_list.traverse()
    linked_list.remove(2)
    linked_list.traverse()
    linked_list.remove(1)
    linked_list.traverse()










