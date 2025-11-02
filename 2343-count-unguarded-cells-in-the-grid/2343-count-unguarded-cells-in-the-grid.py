class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        # convert to sets for O(1) lookup
        wall_set = set(map(tuple, walls))
        guard_set = set(map(tuple, guards))
        guarded = set()

        # four cardinal directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # For each guard, walk in each direction until a wall or another guard
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and (nr, nc) not in wall_set and (nr, nc) not in guard_set:
                    guarded.add((nr, nc))
                    nr += dr
                    nc += dc

        total_cells = m * n
        occupied = len(guards) + len(walls)     # cells that are not empty
        unguarded = total_cells - occupied - len(guarded)
        return unguarded


# --- quick test with the sample input you ran ---
if __name__ == "__main__":
    m = 4
    n = 6
    guards = [[0,0],[1,1],[2,3]]
    walls = [[0,1],[2,2],[1,4]]
    print(Solution().countUnguarded(m, n, guards, walls))  # expected output: 7
