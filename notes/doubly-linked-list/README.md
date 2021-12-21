# Doubly Linked List
- 연습 문제 
    - https://www.acmicpc.net/problem/10866

|InsertAt|RemoveAt|AppendLeft|Append|PopLeft|Pop|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|O(N)|O(N)|O(1)|O(1)|O(1)|O(1)|

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self): return self.size == 0

    def indexAt(self, i):
        curr = self.head
        for i in range(i): curr = curr.next
        return curr

    def linkNode(self, prevNode, newNode, nextNode):
        newNode.prev, newNode.next = prevNode, nextNode
        prevNode.next, nextNode.prev = newNode, newNode
        self.size += 1

    def unlinkNode(self, deletedNode=None):
        if self.isEmpty() or not deletedNode: return False

        prevNode, nextNode = deletedNode.prev, deletedNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.size -= 1
        return deletedNode.value

    def insert(self, i, x):
        if i == 0: self.appendLeft(x)
        elif i == self.size: self.append(x)
        else: self.insertAt(i, x)

    def insertAt(self, i, x):
        nextNode = self.indexAt(i)
        prevNode = nextNode.prev
        newNode = Node(x)
        self.linkNode(prevNode, newNode, nextNode)

    def appendLeft(self, x):
        prevNode, nextNode = self.head, self.head.next
        newNode = Node(x)
        self.linkNode(prevNode, newNode, nextNode)

    def append(self, x):
        prevNode, nextNode = self.tail.prev, self.tail
        newNode = Node(x)
        self.linkNode(prevNode, newNode, nextNode)

    def remove(self, i):
        deletedNode = self.indexAt(i)
        return self.unlinkNode(deletedNode)

    def popLeft(self):
        deletedNode = self.head.next
        return self.unlinkNode(deletedNode)

    def pop(self):
        deletedNode = self.tail.prev
        return self.unlinkNode(deletedNode)

    def front(self):
        return False if self.isEmpty() else self.head.next.value

    def back(self):
        return False if self.isEmpty() else self.tail.prev.value
```

# Doubly Linked List + Stack
- 연습 문제 
    - https://programmers.co.kr/learn/courses/30/lessons/81303 + [풀이](../../양방향연결리스트/pg-dl-표편집/README.md)
- ✅ 삭제 된 순서대로 Restore가 발생한다면!

|Restore|AppendLeft|Append|PopLeft|Pop|
|:----:|:-----:|:-----:|:-----:|:-----:|
|O(1)|O(1)|O(1)|O(1)|O(1)|O(1)|

# Dobuly Linked List + Hash
- 연습문제 
    - https://leetcode.com/problems/lru-cache + [풀이](../../양방향연결리스트/lc-dl-146/README.md)