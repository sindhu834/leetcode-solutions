# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root):
        # Step 1: inorder traversal to collect sorted values
        inorder_vals = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: build balanced BST from sorted values
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(inorder_vals[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(inorder_vals) - 1)
