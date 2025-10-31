# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            # Link the previous node to the current one
            node.left = None
            self.curr.right = node
            self.curr = node
            
            inorder(node.right)

        dummy = TreeNode(-1)  # temporary dummy node
        self.curr = dummy
        inorder(root)
        return dummy.right
