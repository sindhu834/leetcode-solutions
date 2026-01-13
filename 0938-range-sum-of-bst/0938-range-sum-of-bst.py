class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if not root:
            return 0

        # If node value is smaller than low, skip left subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If node value is greater than high, skip right subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # Node value is within range
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
