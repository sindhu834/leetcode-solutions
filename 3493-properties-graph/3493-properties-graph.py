class Solution:
    def numberOfComponents(self, properties, k):
        n = len(properties)
        
        # convert to sets
        sets = [set(p) for p in properties]
        
        # DSU setup
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
        
        # check all pairs
        for i in range(n):
            for j in range(i + 1, n):
                if len(sets[i] & sets[j]) >= k:
                    union(i, j)
        
        # count unique components
        components = set()
        for i in range(n):
            components.add(find(i))
        
        return len(components)