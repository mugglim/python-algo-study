## 링크
https://leetcode.com/problems/lru-cache/submissions/

## 설명
- LRUCache를 위한 자료구조를 디자인한다.
- get 메소드
    - key 있는 경우 페이지를 최신화 하고 value 반환
    - 없는 경우 -1 반환
- put 메소드
    - key 있는 경우 페이지 최신화 
    - 없는 경우 key 반영  
    (단, 캐시 용량이 꽉 찬 경우, 가장 사용한 지 오래된 페이지를 제거한다.)
        
## 풀이 1(default dict + iterator)
dict는 입력 순서를 보장한다. (> Python 3.6)   
그렇기에, 가장 첫 번째 key 값을 오래된 페이지 값으로 생각하였다.

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    # 기본으로 구현해야 하는 메소드
    def get(self, key: int) -> int:
        if key in self.cache:
            self.update(key, self.cache[key])
            return self.cache[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.update(key, value)
        else:
            if self.isFull(): self.popLeft()
            self.cache[key] = value

    #  추가로 구현한 메소드
    def update(self, key, value):
        del self.cache[key]
        self.cache[key] = value

    def popLeft(self):
        k = next(iter(self.cache))
        del self.cache[k]

    def isFull(self):
        return len(self.cache) == self.capacity
```

### 풀이 2(Doubly Linked List + Hash)

양방향 연결리스트에서 노드의 위치를 Hash로 관리하여 Search의 시간복잡도를 O(1)로 처리해보자.

```python
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
```


## 알게된 점
- iter(iterable) 함수를 통해 iterator를 반환 받을 수 있다. O(1)
```python
arr = [1,2,3,4,5]
it = iter(arr)
print(next(it)) # 1
```
- 양방향 연결리스트와 해시를 조합해서 Search의 시간 복잡도를 O(1)로 처리할 수 있다.
    - 단, 값이 중복된다면 다른 방법으로 key를 관리해야 함.
```python
dic = {}
dl = DoublyLinkedList()
node = Node(value)

# add
dic[value] = node
dl.append(node)

# remove
deletedNode = dic.pop(value)
dl.remove(deletedNode)
```

## 결과

|풀이|방식|시간|
|:---:|:---:|:--------:|
|1|default dict + iterator|966ms| 
|2|Doubly Linked List + Hash|1136ms| 