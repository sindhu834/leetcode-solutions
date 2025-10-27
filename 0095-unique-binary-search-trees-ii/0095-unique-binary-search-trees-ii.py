class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        return self.buildTrees(1, n)
    
    def buildTrees(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        
        for i in range(start, end + 1):
            left = self.buildTrees(start, i - 1)
            right = self.buildTrees(i + 1, end)
            
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
