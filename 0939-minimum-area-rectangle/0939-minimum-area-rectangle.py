class Solution:
    def minAreaRect(self, points):
        from collections import defaultdict

        # Map x -> list of y values
        x_to_ys = defaultdict(list)
        for x, y in points:
            x_to_ys[x].append(y)

        last_x = {}
        min_area = float('inf')

        # Traverse x in sorted order
        for x in sorted(x_to_ys):
            ys = sorted(x_to_ys[x])
            n = len(ys)

            # Consider all pairs of y at this x
            for i in range(n):
                for j in range(i + 1, n):
                    y1, y2 = ys[i], ys[j]
                    pair = (y1, y2)

                    if pair in last_x:
                        area = (x - last_x[pair]) * (y2 - y1)
                        min_area = min(min_area, area)

                    last_x[pair] = x

        return 0 if min_area == float('inf') else min_area
