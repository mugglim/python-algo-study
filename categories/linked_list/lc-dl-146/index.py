class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self): return self.size == 0

    def linkNode(self, prevNode, newNode, nextNode):
        newNode.prev, newNode.next = prevNode, nextNode
        prevNode.next, nextNode.prev = newNode, newNode
        self.size += 1

    def unlinkNode(self, deletedNode):
        if self.isEmpty() or not deletedNode: return False

        prevNode, nextNode = deletedNode.prev, deletedNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.size -= 1
        return deletedNode

    def appendLeft(self, newNode):
        prevNode, nextNode = self.head, self.head.next
        self.linkNode(prevNode, newNode, nextNode)

    def remove(self, deletedNode):
        self.unlinkNode(deletedNode)

    def pop(self):
        deletedNode = self.tail.prev
        return self.unlinkNode(deletedNode)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.dl = DoublyLinkedList()
        self.capacity = capacity

    def isFull(self): return len(self.cache) == self.capacity
    def isExist(self, key): return key in self.cache


    def update(self, key, value=None):
        deletedNode = self.cache.pop(key)
        self.dl.remove(deletedNode)

        newValue = value if value else deletedNode.value
        newNode = Node(key, newValue)
        self.dl.appendLeft(newNode)

        self.cache[key] = newNode
        return newNode

    def get(self, key: int) -> int:
        if not self.isExist(key): return -1

        updatedNode = self.update(key)
        return updatedNode.value

    def add(self, key,value):
        if self.isFull(): self.pop()

        newNode = Node(key,value)
        self.dl.appendLeft(newNode)
        self.cache[key] = newNode

    def pop(self):
        deletedNode = self.dl.pop()
        k, v = deletedNode.key, deletedNode.value
        self.cache.pop(k)

    def put(self, key: int, value: int) -> None:
        if self.isExist(key): self.update(key, value)
        else: self.add(key, value)



lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))


# lRUCache = LRUCache(2)
# print(lRUCache.get(2))
# lRUCache.put(2, 6)
# print(lRUCache.get(1))
# lRUCache.put(1, 5)
# lRUCache.put(1, 2)
# print(lRUCache.get(1))
# print(lRUCache.get(2))

