class Solution:
    def minTime(self, n, edges, hasApple):
        from collections import defaultdict
        graph = defaultdict(list)
        
        # Build adjacency list
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            total = 0
            for child in graph[node]:
                if child == parent:
                    continue
                cost = dfs(child, node)
                if cost > 0 or hasApple[child]:
                    total += cost + 2
            return total
        
        return dfs(0, -1)
