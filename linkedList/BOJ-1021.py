class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head


    def peek_left(self):
        if self.size > 0:
            return self.head.next.val

    def peek(self):
        if self.size > 0:
            return self.tail.prev.val

    def popleft(self):
        if self.size > 0:
            prev,next = self.head, self.head.next.next
            next.prev = prev
            prev.next = next
            self.size -= 1
            return self.peek_left()

    def pop(self):
        if self.size > 0:
            prev, next = self.tail.prev.prev, self.tail
            next.prev = prev
            prev.next = next
            self.size -= 1
            return self.peek()

    def append(self,val):
        prev,next = self.tail.prev, self.tail
        node = Node(val)

        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

        self.size += 1

    def append_left(self,val):
        prev,next = self.head, self.head.next
        node = Node(val)

        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node

        self.size += 1


    def rotate(self,dir):
        if self.size > 1: # 사이즈가 1보다 큰 경우에만 의미가 있음.
            if dir == 1: # right
                self.append_left(self.tail.prev.val)
                self.pop()
            else:
                self.append(self.head.next.val)
                self.popleft()

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.val if curr.val != None else "" , end="")
            curr = curr.next
        print()

    def index(self,val):
        idx = 0
        curr = self.head
        while curr != None:
            if curr.val == val:
                return idx
            curr = curr.next
            idx += 1
        return False

    def get_size(self):
        return self.size



if __name__ == "__main__":
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    cnt = 0
    deque = Deque()
    for i in range(1,n+1):
        deque.append(i)

    while len(nums) != 0:
        if deque.peek_left() == nums[0]:
            deque.popleft()
            nums = nums[1:]
        else:
            idx_num = deque.index(nums[0])

            l_cnt, r_cnt = idx_num -1, deque.get_size() - idx_num + 1

            if l_cnt <= r_cnt:
                for _ in range(l_cnt): deque.rotate(-1)
                cnt += l_cnt
                deque.popleft()
                nums = nums[1:]
            else:
                for _ in range(r_cnt): deque.rotate(1)
                cnt += r_cnt
                deque.popleft()
                nums = nums[1:]

    print(cnt)
