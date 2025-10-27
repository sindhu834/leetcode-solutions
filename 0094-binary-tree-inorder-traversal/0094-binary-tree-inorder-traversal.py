class Solution:
    def inorderTraversal(self, root):
        result, stack = [], []
        curr = root

        while curr or stack:
            # Reach leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop and visit
            curr = stack.pop()
            result.append(curr.val)

            # Go to right subtree
            curr = curr.right

        return result
