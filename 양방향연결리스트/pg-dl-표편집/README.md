## 링크
https://programmers.co.kr/learn/courses/30/lessons/81303

## 설명
- 양방향 연결 리스트는 삽입/삭제는 O(n)의 비용
- 효율성을 해결하기 위해서는 복구 과정에서 O(n)을 태우면 안 됨.
- 복구는 최근에 삭제된 순서 부터 실행 되므로 삭제 될 때 노드를 스택으로 가지고 있으면 됨.
```text
Doubly Linked Likst                    stack

head <-> a <-> b <-> c <-> tail        []

1) remove b                           
head <-> a <-> c <-> tail        [b:{prev:a, next:c}]

2) remove a
head <-> c <->tail               [b:{prev:a, next:c}, a:{prev:head, next:c}]

3) restore 
head <-> a <-> c <-> tail        [b:{prev:a, next:c}]

// ...
```
- 만약 b를 a보다 먼저 복구해야 한다면 위 처럼 수행하면 안 됨. (근데 문제에서는 복구 순서를 보장해 줌)

## 풀이 1
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self, n):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        self.checked = ["O"] * n

    def isEmpty(self): return self.size == 0
    def isLastNode(self): return self.curr.next == self.tail

    def move(self, opt, i):
        if opt == "L":
            for _ in range(i): self.curr = self.curr.prev
        else:
            for _ in range(i): self.curr = self.curr.next


    def linkNode(self, prevNode, newNode, nextNode):
        newNode.prev, newNode.next = prevNode, nextNode
        prevNode.next, nextNode.prev = newNode, newNode
        self.size += 1

    def unlinkNode(self, deletedNode=None):
        if self.isEmpty() or not deletedNode: return False
        prevNode, nextNode = deletedNode.prev, deletedNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.size -= 1

    def append(self, x):
        prevNode, nextNode = self.tail.prev, self.tail
        newNode = Node(x)
        self.linkNode(prevNode, newNode, nextNode)

    def restore(self, deletedNode):
        self.linkNode(deletedNode.prev, deletedNode, deletedNode.next)
        self.checked[deletedNode.value] = "O"

    def remove(self):
        deletedNode = self.curr
        newCurr = self.curr.prev if self.isLastNode() else self.curr.next
        self.checked[deletedNode.value] = "X"
        self.unlinkNode(deletedNode)
        return [deletedNode, newCurr]


def solution(n, k, cmd):
    stack = []
    dl = DoublyLinkedList(n)

    for i in range(n): dl.append(i)
    dl.move("R", k+1)


    for l in cmd:
        opt, *v = l.split(" ")
        v = int(v[0]) if v else v

        if opt == "U": dl.move("L", v)
        if opt == "D": dl.move("R", v)
        if opt == "C":
            deletedNode, newCurr = dl.remove()
            stack.append(deletedNode)
            dl.curr = newCurr
        if opt == "Z": dl.restore(stack.pop())

    return ''.join(dl.checked)
```


## 알게된 점
- 양방향 연결 리스트와 스택을 모두 사용하면 삭제 된 노드를 복구하는데 O(1)로 처리할 수 있다.
    - 단, 최근에 삭제 된 순서대로 복구 한다는 가정이 있어야 함.
## 결과
|풀이|방식|시간|
|:---:|:---:|:--------:|
|1| 양방향 연결 리스트 + 스택 | 통과 | 