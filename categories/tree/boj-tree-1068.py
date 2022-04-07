import sys
input = lambda : sys.stdin.readline().rstrip()

class Node:
    def __init__(self, val):
        self.val = val
        self.child_nodes = []

    def add_child(self, child_node):
        self.child_nodes.append(child_node)

    def is_leaf_node(self):
        return len(self.child_nodes) == 0

def count_leaf_node(root:Node):
    if not root: return 0
    if root.is_leaf_node(): return 1

    leaf_node_count = 0

    for child_node in root.child_nodes:
        leaf_node_count += count_leaf_node(child_node)

    return leaf_node_count


def sol(n, nodes, remove_node):
    adj_list = [Node(i) for i in range(n)]
    root = None

    for i, parent in enumerate(nodes):
        # 삭제할 노드 라면, 추가 하지 않음
        if i == remove_node: continue

        if parent == -1:
            root = adj_list[i]
        else:
            adj_list[parent].add_child(adj_list[i])

    # root 노드가 삭제할 노드인 경우
    if root and root.val == remove_node: return 0
    
    # 삭제할 노드가 root가 아닌 경우
    return count_leaf_node(root)

if __name__ == "__main__":
    n = int(input())
    nodes = list(map(int,input().split()))
    remove_node = int(input())

    print(sol(n, nodes, remove_node))
