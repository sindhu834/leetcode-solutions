class Solution:
    def separateSquares(self, squares):
        total_area = 0.0

        for x, y, l in squares:
            total_area += l * l

        target = total_area / 2.0

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def area_below(H):
            area = 0.0
            for _, y, l in squares:
                if H <= y:
                    continue
                elif H >= y + l:
                    area += l * l
                else:
                    area += l * (H - y)
            return area

        # Binary search
        for _ in range(60):  # enough for 1e-5 precision
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid

        return low
