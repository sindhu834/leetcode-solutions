from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        
        # DSU
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb
        
        # Step 1: build components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Step 2: group indices by root
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)
        
        # Step 3: calculate mismatch
        ans = 0
        
        for indices in groups.values():
            freq = Counter()
            
            for i in indices:
                freq[source[i]] += 1
            
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1
        
        return ans