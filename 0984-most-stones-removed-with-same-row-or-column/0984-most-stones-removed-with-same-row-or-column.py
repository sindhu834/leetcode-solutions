class Solution:
    def removeStones(self, stones):
        from collections import defaultdict

        # Build graph: connect stones that share same row or column
        graph = defaultdict(list)
        n = len(stones)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # Count connected components
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        # Max stones removable = total stones - components
        return n - components
