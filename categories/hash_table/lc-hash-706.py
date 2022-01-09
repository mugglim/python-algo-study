from typing import Union
HASH_TABLE_SIZE = 1000

class Node:
    def __init__(self, key:Union[None,int], value:Union[None,int]):
        self.key, self.value = key, value
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def linkNode(self, prevNode:Node, newNode:Node, nextNode:Node) -> None:
        prevNode.next, nextNode.prev = newNode, newNode
        newNode.prev, newNode.next = prevNode, nextNode

    def unlinkNode(self, deletedNode:Node) -> None:
        deletedNode.prev.next = deletedNode.next
        deletedNode.next.prev = deletedNode.prev

    def getNodeByKey(self, targetKey:int) -> Union[bool, Node]:
        curr = self.head

        while curr:
            if curr.key == targetKey: return curr
            curr = curr.next

        return False

    def isExistNode(self, key:int) -> bool:
        return True if self.getNodeByKey(key) else False

    def appendNode(self, key:int, value:int) -> None:
        newNode = Node(key, value)
        self.linkNode(self.tail.prev, newNode, self.tail)
        self.size += 1

    def updateNode(self, key:int, newValue:int) -> None:
        updatedNode = self.getNodeByKey(key)
        updatedNode.value = newValue

    def removeNode(self, key:int) -> None:
        if self.isEmpty() or not self.isExistNode(key): return

        deletedNode = self.getNodeByKey(key)
        self.unlinkNode(deletedNode)
        self.size -= 1


class MyHashMap:

    def __init__(self):
        self.tableSize = HASH_TABLE_SIZE
        self.table = [DoublyLinkedList() for _ in range(self.tableSize)]

    def getHashCode(self, value:int) -> int:
        return value % self.tableSize

    def isExistKey(self, hashCode:int, key:int) -> int:
        return self.table[hashCode].getNodeByKey(key)

    def add(self, hashCode:int,key:int,value:int) -> None:
        self.table[hashCode].appendNode(key,value)

    def update(self, hashCode:int, key:int, newValue:int) -> None:
        self.table[hashCode].updateNode(key, newValue)

    def put(self, key: int, value: int) -> None:
        hashCode = self.getHashCode(key)

        if self.isExistKey(hashCode, key):
            self.update(hashCode, key, value)
        else:
            self.add(hashCode, key, value)

    def get(self, key: int) -> int:
        hashCode = self.getHashCode(key)
        targetNode = self.table[hashCode].getNodeByKey(key)
        return targetNode.value if targetNode else -1

    def remove(self, key: int) -> None:
        hashCode = self.getHashCode(key)
        self.table[hashCode].removeNode(key)

