class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            
            # Push left and right children
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        return stack2[::-1]
