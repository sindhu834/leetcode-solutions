from collections import defaultdict
import bisect

# ---------- DSU (Disjoint Set Union) ----------
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


# ---------- Solution Class ----------
class Solution:
    def processQueries(self, c, connections, queries):
        dsu = DSU(c)

        # Step 1: Union all connected stations
        for u, v in connections:
            dsu.union(u, v)

        # Step 2: Group stations by component root
        groups = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            groups[root].append(i)

        # Step 3: Initially all stations online
        online = [True] * (c + 1)

        # Step 4: Maintain sorted list of online stations per component
        comp_online = {}
        for root, nodes in groups.items():
            nodes.sort()
            comp_online[root] = nodes[:]

        # Step 5: Process each query
        res = []
        for t, x in queries:
            root = dsu.find(x)

            if t == 1:  # Maintenance check
                if online[x]:
                    res.append(x)
                else:
                    arr = comp_online[root]
                    if arr:
                        res.append(arr[0])  # smallest online id
                    else:
                        res.append(-1)

            elif t == 2:  # Go offline
                if online[x]:
                    online[x] = False
                    arr = comp_online[root]
                    idx = bisect.bisect_left(arr, x)
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)

        return res
