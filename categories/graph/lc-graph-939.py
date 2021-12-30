class Solution:
    result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return

        if low <= root.val and root.val <= high:
            self.result += root.val

        self.rangeSumBST(root.left, low, high);
        self.rangeSumBST(root.right, low, high);

        return self.result