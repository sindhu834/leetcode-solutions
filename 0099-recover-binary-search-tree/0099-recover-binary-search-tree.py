class Solution:
    def recoverTree(self, root):
        stack = []
        inorder = []
        curr = root

        # Step 1: Inorder traversal
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr)
            curr = curr.right

        # Step 2: Find two misplaced nodes
        first = second = None
        for i in range(len(inorder) - 1):
            if inorder[i].val > inorder[i + 1].val:
                if not first:
                    first = inorder[i]
                    second = inorder[i + 1]
                else:
                    second = inorder[i + 1]

        # Step 3: Swap values
        first.val, second.val = second.val, first.val
