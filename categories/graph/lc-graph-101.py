class Solution:
    def optionalBfs(self, root, option):
        if not root:
            return False

        result = [root.val]
        queue = deque([root])

        def insertNodeQueue(node):
            if not node:
                result.append('null')
            else:
                queue.append(node)
                result.append(node.val)

        while queue:
            node = queue.popleft()

            if option == "l":
                insertNodeQueue(node.left)
                insertNodeQueue(node.right)
            else:
                insertNodeQueue(node.right)
                insertNodeQueue(node.left)

        return result

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.optionalBfs(root.left, 'l') == self.optionalBfs(root.right, 'r')




