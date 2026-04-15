class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}  # map: original → clone
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            # create clone
            clone = Node(node.val)
            visited[node] = clone
            
            # clone neighbors
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)