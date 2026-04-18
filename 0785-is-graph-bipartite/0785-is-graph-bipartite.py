from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 = unvisited
        
        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0
                
                while queue:
                    node = queue.popleft()
                    
                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[node]
                            queue.append(nei)
                        
                        elif color[nei] == color[node]:
                            return False
        
        return True