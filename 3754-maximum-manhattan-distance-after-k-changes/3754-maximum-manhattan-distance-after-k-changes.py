class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        # counts for dx, dy
        e = w = ncnt = scnt = 0
        ans = 0

        for i, ch in enumerate(s, start=1):
            if ch == 'E':
                e += 1
            elif ch == 'W':
                w += 1
            elif ch == 'N':
                ncnt += 1
            else:  # 'S'
                scnt += 1

            dx = e - w
            dy = ncnt - scnt
            curr = abs(dx) + abs(dy)

            flips_available = min(k, i)
            possible = curr + 2 * flips_available
            if possible > i:
                possible = i

            if possible > ans:
                ans = possible

        return ans
