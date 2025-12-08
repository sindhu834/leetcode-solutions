class Solution:
    def isSameTree(self, p, q):
        # If both are None, they are same
        if not p and not q:
            return True

        # If one is None and the other is not, not same
        if not p or not q:
            return False

        # If values are different, not same
        if p.val != q.val:
            return False

        # Check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
