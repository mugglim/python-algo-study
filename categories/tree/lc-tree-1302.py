# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        ans = [0, 0]

        def dfs(curr, depth):
            if not curr.left and not curr.right:
                if depth > ans[1]:
                    ans[0] = 0
                    ans[1] = depth
                if depth == ans[1]:
                    ans[0] += curr.val

                return

            if curr.left: dfs(curr.left, depth + 1)
            if curr.right: dfs(curr.right, depth + 1)

        dfs(root, 0)
        return ans[0]
